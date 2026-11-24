"""Public DebLang engine."""
from pathlib import Path
from .translator import DebTranslator
from .vm import DebVM

class DebLang:
    def __init__(self, *, show_traceback=False):
        self.translator = DebTranslator()
        self.vm = DebVM(show_traceback=show_traceback)

    def translate(self, source: str) -> str:
        return self.translator.translate(source)

    def run_code(self, source: str, filename="<DebLang>") -> bool:
        try:
            translated = self.translate(source)
        except Exception as error:
            print(f"[DebLang Translation Error] {type(error).__name__}: {error}")
            return False
        return self.vm.execute(translated, filename)

    def run_file(self, filename: str) -> bool:
        path = Path(filename)
        try:
            source = path.read_text(encoding="utf-8")
        except OSError as error:
            print(f"[DebLang File Error] {error}")
            return False
        return self.run_code(source, str(path))
