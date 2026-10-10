#!/usr/bin/env python3
"""Report broken internal links on the published Helvetic Poker tournament site.

Read-only and warning-only: network errors are reported separately and never
fail the workflow. Intentionally absent regional pages are not inferred from
a naming convention; a link is flagged only when a linked URL returns 4xx.
"""
from __future__ import annotations

from html.parser import HTMLParser
from urllib.error import HTTPError, URLError
from urllib.parse import urldefrag, urljoin, urlparse
from urllib.request import Request, urlopen
import time
import xml.etree.ElementTree as ET

BASE = "https://pokerturniere.helveticpoker.ch/"
HOST = urlparse(BASE).netloc
USER_AGENT = "HelveticPokerInternalLinkCheck/1.0 (+https://github.com/Helvetic-Poker/helveticpoker-pokerturniere)"
TIMEOUT = 12
DELAY_SECONDS = 0.08
MAX_LINKS = 1500


class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag.lower() not in {"a", "area"}:
            return
        href = dict(attrs).get("href")
        if href:
            self.links.append(href.strip())


def fetch(url: str):
    request = Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urlopen(request, timeout=TIMEOUT) as response:
            return response.status, response.read(2_000_000).decode("utf-8", "replace"), response.geturl()
    except HTTPError as error:
        return error.code, "", url
    except (URLError, TimeoutError, OSError) as error:
        return None, str(error), url


def canonical(url: str) -> str | None:
    absolute = urldefrag(urljoin(BASE, url))[0]
    parsed = urlparse(absolute)
    if parsed.scheme not in {"http", "https"} or parsed.netloc.lower() != HOST.lower():
        return None
    # Ignore query parameters when checking the same published resource.
    return parsed._replace(query="", fragment="").geturl()


def main():
    print(f"Checking published internal links at {BASE}")
    status, body, final_url = fetch(urljoin(BASE, "sitemap.xml"))
    if status is None or status >= 400:
        print(f"WARNING: sitemap could not be read (HTTP {status}): {body}")
        print("No link checks completed; workflow remains warning-only.")
        return

    try:
        root = ET.fromstring(body)
    except ET.ParseError as error:
        print(f"WARNING: sitemap XML could not be parsed: {error}")
        return

    sitemap_urls = []
    for node in root.iter():
        if node.tag.rsplit("}", 1)[-1] == "loc" and node.text:
            url = canonical(node.text.strip())
            if url:
                sitemap_urls.append(url)

    # Inspect the homepage and published regional landing pages, then check
    # every same-host link found there (including event/category destinations).
    candidates = {canonical(BASE)}
    for url in sitemap_urls:
        path = urlparse(url).path.lower()
        if any(segment in path for segment in ("/stadt/", "/kanton/", "/veranstalter/")):
            candidates.add(url)

    checked_pages = 0
    checked_targets = set()
    broken: dict[str, set[int]] = {}
    unavailable: list[tuple[str, str]] = []

    for page in sorted(candidates):
        page_status, html, landed = fetch(page)
        time.sleep(DELAY_SECONDS)
        if page_status is None:
            unavailable.append((page, html))
            continue
        if page_status >= 400:
            broken.setdefault(page, set()).add(page_status)
            continue
        checked_pages += 1
        parser = LinkParser()
        parser.feed(html)
        for raw_href in parser.links:
            target = canonical(urljoin(landed, raw_href))
            if target:
                checked_targets.add(target)

    if len(checked_targets) > MAX_LINKS:
        print(f"WARNING: found {len(checked_targets)} unique internal targets; limiting checks to {MAX_LINKS}.")
        checked_targets = set(sorted(checked_targets)[:MAX_LINKS])

    for target in sorted(checked_targets):
        code, detail, _ = fetch(target)
        time.sleep(DELAY_SECONDS)
        if code is None:
            unavailable.append((target, detail))
        elif code >= 400:
            broken.setdefault(target, set()).add(code)

    print(f"Pages inspected: {checked_pages}")
    print(f"Unique internal link targets checked: {len(checked_targets)}")
    print(f"URLs returning 4xx/5xx: {len(broken)}")
    print(f"Network/timeout issues: {len(unavailable)}")

    if broken:
        print("\nBROKEN INTERNAL URLS (review before changing anything):")
        for url, codes in sorted(broken.items()):
            print(f"  HTTP {','.join(map(str, sorted(codes)))}  {url}")
    if unavailable:
        print("\nUNVERIFIED (network/timeout; not counted as broken):")
        for url, reason in unavailable[:50]:
            print(f"  {url} — {reason}")
        if len(unavailable) > 50:
            print(f"  ... plus {len(unavailable) - 50} more")
    if not broken and not unavailable:
        print("No broken internal links found in the checked pages.")
    print("\nReport-only check: this script does not edit pages or fail deployment.")


if __name__ == "__main__":
    main()
