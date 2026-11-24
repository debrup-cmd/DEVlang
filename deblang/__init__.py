"""DebLang: My Own Flavour of Python, powered by DebVM."""
from .engine import DebLang
from .translator import DebTranslator, KEYWORDS
from .vm import DebVM

__version__ = "1.0.0"
__all__ = ["DebLang", "DebTranslator", "DebVM", "KEYWORDS"]
