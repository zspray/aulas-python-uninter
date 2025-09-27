from cx_Freeze import setup, Executable
import os

path = "./asset"
asset_list = os.listdir(path)
asset_list_completa = [os.path.join(path, asset).replace("\\", "/") for asset in asset_list]
print(asset_list_completa)

executables = [Executable("main.py")]
files = {"include_files": asset_list_completa, "packages": ["pygame"]}

setup(
    name="CloudForces",
    version="1.0",
    description="A 2D Shooter game made with Pygame",
    options={"build_exe": files},
    executables=executables
)