"""DebLang source-to-Python translator.

Only identifiers outside strings and comments are translated. The translator
preserves Python's indentation and punctuation, so DebLang remains a
Python-compatible beginner language.
"""
from __future__ import annotations

KEYWORDS = {
    "agar": "if", "warna": "else", "warna_agar": "elif",
    "har": "for", "mein": "in", "jabtak": "while",
    "karya": "def", "wapas": "return",
    "sach": "True", "jhooth": "False", "kuch_nahi": "None",
    "aur": "and", "ya": "or", "nahi": "not", "hai": "is",
    "roko": "break", "aage": "continue", "khaali": "pass",
    "koshish": "try", "sivay": "except", "aakhir": "finally",
    "uthao": "raise", "lao": "import", "se": "from",
    "saath": "with", "jaisa": "as", "varg": "class",
    "vaishvik": "global", "sthaniya": "nonlocal",
    "chhota_karya": "lambda", "do": "yield",
    "bolo": "print", "pucho": "input",
}

class DebTranslator:
    def __init__(self, keywords=None):
        self.keywords = dict(KEYWORDS if keywords is None else keywords)

    def translate(self, code: str) -> str:
        out, i, n = [], 0, len(code)
        while i < n:
            ch = code[i]

            # Comments: copy unchanged to end of line.
            if ch == "#":
                j = code.find("\n", i)
                if j == -1:
                    out.append(code[i:])
                    break
                out.append(code[i:j])
                i = j
                continue

            # Single, double, and triple-quoted strings; keep contents untouched.
            if ch in ("'", '"'):
                quote = ch
                delimiter = quote * 3 if code[i:i+3] == quote * 3 else quote
                out.append(delimiter)
                i += len(delimiter)
                while i < n:
                    if code[i] == "\\":
                        out.append(code[i:i+2])
                        i += 2
                        continue
                    if code.startswith(delimiter, i):
                        out.append(delimiter)
                        i += len(delimiter)
                        break
                    out.append(code[i])
                    i += 1
                continue

            # Identifiers and DebLang keywords.
            if ch.isalpha() or ch == "_":
                j = i + 1
                while j < n and (code[j].isalnum() or code[j] == "_"):
                    j += 1
                word = code[i:j]
                out.append(self.keywords.get(word, word))
                i = j
                continue

            out.append(ch)
            i += 1
        return "".join(out)
