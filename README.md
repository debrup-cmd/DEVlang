# DebLang v1.0

**My Own Flavour of Python — Powered by DebVM**

DebLang is an experimental, beginner-friendly programming language project. It lets you write selected Python keywords using Hinglish words, then translates the source into Python for execution.

> **New here? Start with [GETTING_STARTED.md](GETTING_STARTED.md).** It explains how to download, install, launch, and run your first program step by step.

## Try DebLang in 3 steps

1. Install Python 3.9 or newer: https://www.python.org/downloads/
2. Download this repository using **Code → Download ZIP**, then extract it.
3. On Windows, double-click `START_DEBLANG.bat`.

To run an example from a terminal opened in the project folder:

```powershell
py -m deblang examples\hello.deb
```

## Your first DebLang program

Save this as `hello.deb`:

```python
naam = pucho("What is your name? ")
bolo("Namaste", naam)
```

Run it:

```powershell
py -m deblang hello.deb
```

## Documentation

- **[Getting Started](GETTING_STARTED.md)** — installation, first run, examples, troubleshooting
- **[Mini Tutorial](TUTORIAL.md)** — conditions, loops, functions, and more
- **[Examples](examples/)** — ready-to-run `.deb` programs

## Keyword reference

| DebLang | Python | DebLang | Python |
|---|---|---|---|
| `agar` | `if` | `warna` | `else` |
| `warna_agar` | `elif` | `har` | `for` |
| `mein` | `in` | `jabtak` | `while` |
| `karya` | `def` | `wapas` | `return` |
| `sach` | `True` | `jhooth` | `False` |
| `kuch_nahi` | `None` | `aur` | `and` |
| `ya` | `or` | `nahi` | `not` |
| `bolo` | `print` | `pucho` | `input` |
| `varg` | `class` | `roko` | `break` |
| `aage` | `continue` | `khaali` | `pass` |
| `koshish` | `try` | `sivay` | `except` |
| `aakhir` | `finally` | `uthao` | `raise` |
| `lao` | `import` | `se` | `from` |
| `saath` | `with` | `jaisa` | `as` |
| `vaishvik` | `global` | `sthaniya` | `nonlocal` |
| `chhota_karya` | `lambda` | `do` | `yield` |
| `hai` | `is` | | |

## Run commands

```bash
# Start interactive mode
python -m deblang

# Run a source file
python -m deblang examples/conditions.deb

# Preview translated Python
python -m deblang --translate examples/conditions.deb

# Show full traceback on runtime errors
python -m deblang --traceback examples/conditions.deb

# Run tests
python -m unittest discover -s tests -v
```

On Windows, `py` can be used instead of `python`. The included `.bat` launchers are also available.

## Project structure

```text
DebLang/
├── deblang/             # Translator, engine, DebVM, CLI
├── examples/            # Ready-to-run DebLang programs
├── tests/               # Unit tests
├── PVM/                 # Portability notes
├── GETTING_STARTED.md   # Beginner installation guide
├── TUTORIAL.md          # Language tutorial
├── START_DEBLANG.bat    # Windows interactive launcher
├── RUN_DEBLANG_FILE.bat # Windows .deb file launcher
├── CREATE_MY_PROGRAM.bat
├── pyproject.toml
└── LICENSE
```

## What is DebVM in v1.0?

DebVM is the execution layer. In this version it compiles translated Python source into CPython bytecode using Python's `compile()` and executes it. It is not yet an independent bytecode virtual machine. Building a dedicated DebLang bytecode format and interpreter is part of the roadmap.

## Safety

DebLang v1.0 executes code with the permissions of the current user. It is not a security sandbox. Do not execute untrusted `.deb` files.

## Roadmap

- [x] Hinglish keyword translator
- [x] Interactive terminal
- [x] Run `.deb` source files
- [x] Beginner examples and tests
- [ ] Dedicated DebLang bytecode
- [ ] Independent DebVM interpreter
- [ ] Standalone executable distribution

## Author

**Debrup Ghosh**

Licensed under the MIT License. See [LICENSE](LICENSE).
