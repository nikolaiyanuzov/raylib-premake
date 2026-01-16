import os 
import sys
import subprocess
from pathlib import Path

ROOT = Path(__file__).parent.resolve()

os.environ["ROOT"] = str(ROOT.parent)

premake = ROOT / "Premake" / "premake5.exe"

if not premake.exists():
    print(f"Premake not found: {premake}")
    sys.exit(1)

repoName = input("Type in your name\n")
os.environ["NAME"] = str(repoName)

version = input("Choose a version: vs2022   vs2019   vs2017\n")
if(version!="vs2022" and version!="vs2019" and version!="vs2017"):
    print("Not a correct version")
    sys.exit(1)

cmd = [str(premake), version]
print("Running: " , "".join(cmd))

subprocess.run(cmd, cwd=ROOT, check=True)