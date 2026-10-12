class AzerbaijaniEngine:
    def __init__(self):
        # Comprehensive baseline dictionary mapping for all consonants.
        # Aligned with the 2001 Tehran Seminar orthography rules.
        # Note: This acts as a fallback phonetic layer; loanwords or contextual splits
        # will override this via Module 2 (Lexicon) and higher logic layers.
        self.consonant_map = {
            "b": "ب",
            "p": "پ",
            "ç": "چ",
            "j": "ژ",
            "x": "خ",
            "ş": "ش",
            "d": "د",
            "r": "ر",
            "f": "ف",
            "q": "ق",
            "l": "ل",
            "v": "و",
            "g": "گ",  # Will need contextual soft-g rules later
            "ğ": "غ",
            "k": "ک",
            "y": "ی",

            # --- SPECIAL CONSONANTS LAYER (Page 6 Exceptions) ---
            # The following characters represent phonetic baseline rules for native words.
            # In Arabic/Persian loanwords, these sounds split across multiple etymological characters.
            # These will be explicitly resolved via Module 2 (Lexicon Overrides).
            "z": "ز",  # Loanword variants: ز, ذ, ظ, ض
            "s": "س",  # Loanword variants: س, ث, ص
            "t": "ت",  # Loanword variants: ت, ط
            "h": "ه"   # Loanword variants: ه, ح
        }

    def convert_latin_to_arabic(self, text: str) -> str:
        """Module 3 Core: Converts explicit Latin letters to Arabic script characters."""
        if not text:
            return ""
        
        # Process the text character by character using our consonant mapping table
        output = [self.consonant_map.get(char.lower(), char) for char in text]
        return "".join(output)
