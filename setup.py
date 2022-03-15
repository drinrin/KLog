import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {"packages": ["os", "pynput"], "include_files": {'six.py'}}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Klog",
    version="0.2",
    description="klog",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base)],
)