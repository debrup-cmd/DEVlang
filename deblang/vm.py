"""DebVM execution engine.

DebVM currently compiles translated source to CPython bytecode and executes it.
It is a lightweight compatibility VM, not a standalone native bytecode engine.
"""
from __future__ import annotations
import sys
import traceback

class DebVM:
    def __init__(self, *, show_traceback=False):
        self.environment = {"__builtins__": __builtins__, "__name__": "__main__"}
        self.execution_count = 0
        self.show_traceback = show_traceback

    def execute(self, python_code: str, filename="<DebLang>") -> bool:
        try:
            code_object = compile(python_code, filename, "exec")
            exec(code_object, self.environment)
            self.execution_count += 1
            return True
        except SystemExit:
            raise
        except Exception as error:
            print(f"[DebVM Runtime Error] {type(error).__name__}: {error}", file=sys.stderr)
            if self.show_traceback:
                traceback.print_exc()
            return False
