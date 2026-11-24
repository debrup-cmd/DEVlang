# Getting Started with DebLang

Welcome! This guide will help you run your first DebLang program. You do not need to know how DebLang works internally to get started.

## Step 1 — Download DebLang

1. Open the DebLang GitHub repository.
2. Click the green **Code** button.
3. Select **Download ZIP**.
4. Extract the ZIP file. Do not try to run DebLang from inside the compressed ZIP.

You should see files such as `START_DEBLANG.bat`, `README.md`, and the folders `deblang` and `examples`.

## Step 2 — Install Python

DebLang v1.0 needs Python 3.9 or newer.

1. Visit https://www.python.org/downloads/
2. Download and install Python.
3. On Windows, tick **Add Python to PATH** in the installer.
4. Finish installation.

DebLang does not need extra Python packages for normal use.

## Step 3 — Start DebLang (Windows)

Double-click:

`START_DEBLANG.bat`

A terminal window will open. You should see the DebLang welcome message and the `DebLang >>>` prompt.

If Windows says Python is missing, install Python using Step 2 and try again.

## Step 4 — Try an example

Open the `examples` folder. The project includes:

- `hello.deb` — asks for your name and greets you
- `conditions.deb` — demonstrates `agar`, `warna_agar`, and `warna`
- `loops.deb` — demonstrates loops
- `functions.deb` — demonstrates functions
- `classes.deb` — demonstrates classes

To run an example, either:

**Option A:** Open a terminal in the DebLang folder and run:

```powershell
py -m deblang examples\hello.deb
```

**Option B:** Drag a `.deb` file onto `RUN_DEBLANG_FILE.bat`.

## Step 5 — Write your first program

1. Open the DebLang folder.
2. Double-click `CREATE_MY_PROGRAM.bat`.
3. Open the created `my_first_program.deb` file in Notepad or VS Code.
4. Write or edit your code and save it.
5. Drag `my_first_program.deb` onto `RUN_DEBLANG_FILE.bat`.

Your first program can be:

```python
naam = pucho("What is your name? ")
bolo("Namaste", naam)
```

Expected interaction:

```text
What is your name? Debrup
Namaste Debrup
```

## Step 6 — Learn the DebLang keywords

| DebLang word | Meaning in Python |
|---|---|
| `agar` | if |
| `warna` | else |
| `warna_agar` | elif |
| `har` | for |
| `mein` | in |
| `jabtak` | while |
| `karya` | def |
| `wapas` | return |
| `sach` | True |
| `jhooth` | False |
| `kuch_nahi` | None |
| `aur` | and |
| `ya` | or |
| `nahi` | not |
| `bolo` | print |
| `pucho` | input |
| `varg` | class |
| `roko` | break |
| `aage` | continue |
| `khaali` | pass |

DebLang keeps much of Python's familiar syntax. For example, use a colon `:` after conditions and functions, and indent the statements inside them.

## Step 7 — Understand the interactive terminal

When you start DebLang, you will see:

```text
DebLang >>>
```

Type a small program:

```python
bolo("Hello from DebLang!")
bas
```

Type `bas` on a new line to execute the code block. Type `exit` at an empty prompt to close the shell.

## Troubleshooting

**'py' or 'python' is not recognized**

Install Python 3.9+ and enable **Add Python to PATH**. Restart the terminal after installation.

**The program window closes immediately**

Run the program through `START_DEBLANG.bat` or `RUN_DEBLANG_FILE.bat`, which keeps the terminal open where appropriate.

**SyntaxError**

Check spelling, colons, brackets, quotation marks, and indentation. Python syntax rules still apply.

**A DebLang word inside a string changed unexpectedly**

It should not: the translator is designed to leave quoted strings and comments unchanged. Please report a reproducible example in the GitHub Issues page.

## Important

DebLang v1.0 uses Python internally to compile and execute translated code. It is an experimental learning project, not a secure sandbox. Only run `.deb` files from people you trust.

## Need help?

Open the repository's **Issues** tab on GitHub and describe:
1. What command or file you ran.
2. What you expected to happen.
3. The complete error message you received.
