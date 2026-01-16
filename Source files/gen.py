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


SRC = ROOT.parent / "src"
SRC.mkdir(exist_ok=True)

MAIN = SRC / "main.cpp"

if not MAIN.exists():
    MAIN.write_text("""
#include "raylib.h"

int main(void)
{
    const int screenWidth = 800;
    const int screenHeight = 450;

    InitWindow(screenWidth, screenHeight, "raylib [core] example - basic window");

    SetTargetFPS(60);

    while (!WindowShouldClose())  
    {
        BeginDrawing();

            ClearBackground(RAYWHITE);

            DrawText("Congrats! You created your first window!", 190, 200, 20, LIGHTGRAY);

        EndDrawing();
    }

    CloseWindow();

}
""".strip())

subprocess.run(cmd, cwd=ROOT, check=True)
