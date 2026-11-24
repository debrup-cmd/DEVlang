# DebLang Portable VM (PVM)

This folder documents how to run DebLang on another computer. The runtime is the `deblang/` Python package; it requires Python 3.9+ on the target computer.

- Windows: run `run_deblang.bat` or `py -m deblang`.
- Linux/macOS: run `bash run_deblang.sh` or `python3 -m deblang`.

This is a portable source distribution, not a self-contained executable. A true standalone VM / executable would require packaging a Python runtime or implementing a native DebLang bytecode interpreter.
