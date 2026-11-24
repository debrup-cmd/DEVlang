"""Command-line interface and interactive shell."""
from __future__ import annotations
import argparse
import sys
from .engine import DebLang

BANNER = r"""
================================================
                    DEBLANG
                     v1.0
             My Own Flavour of Python
                 Powered by DebVM
================================================
"""

def repl():
    lang = DebLang()
    print(BANNER)
    print("Write DebLang code. Enter 'bas' on a new line to run.")
    print("Enter 'exit' on an empty prompt to quit.")
    while True:
        print("\nDebLang >>>")
        lines = []
        while True:
            try:
                line = input("... " if lines else "")
            except EOFError:
                print("\nDebLang closed.")
                return 0
            except KeyboardInterrupt:
                print("\nInput cancelled.")
                lines = []
                break
            if not lines and line.strip() == "exit":
                print("Thank you for using DebLang!")
                return 0
            if line.strip() == "bas":
                if lines:
                    lang.run_code("\n".join(lines))
                break
            lines.append(line)

def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="deblang",
        description="Run DebLang (.deb) programs or start the interactive shell."
    )
    parser.add_argument("file", nargs="?", help="DebLang source file")
    parser.add_argument("--translate", action="store_true",
                        help="print translated Python without executing")
    parser.add_argument("--traceback", action="store_true",
                        help="show full Python traceback for runtime errors")
    args = parser.parse_args(argv)

    if not args.file:
        if args.translate:
            parser.error("--translate requires a source file")
        return repl()

    lang = DebLang(show_traceback=args.traceback)
    if args.translate:
        try:
            print(lang.translate(open(args.file, encoding="utf-8").read()))
            return 0
        except OSError as error:
            print(f"DebLang File Error: {error}", file=sys.stderr)
            return 1
    return 0 if lang.run_file(args.file) else 1

if __name__ == "__main__":
    raise SystemExit(main())
