import subprocess,sys
from pathlib import Path
R=Path(__file__).resolve().parents[1]
subprocess.run([sys.executable,str(R/'scripts/preflight.py')],check=True)
print('SAFE PUBLISH CHECK PASSED')
