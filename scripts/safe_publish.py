import subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
subprocess.run([sys.executable,str(ROOT/'scripts/preflight.py')],check=True)
print('SAFE PUBLISH CHECK PASSED')
