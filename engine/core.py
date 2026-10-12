class AzerbaijaniEngine:
    def __init__(self):
        # Comprehensive baseline dictionary mapping for all consonants.
        # Aligned with the 2001 Tehran Seminar orthography rules.
        self.consonant_map = {
            "b": "ب",
            "p": "پ",
            "t": "ت",
            "m": "م",
            "n": "ن",
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
        """Module 3 Core: Converts Latin text to Arabic script with position-dependent logic."""
        if not text:
            return ""
        
        words = text.lower().split()
        processed_words = []
        
        for word in words:
            output = []
            word_len = len(word)
            
            for idx, char in enumerate(word):
                if char == "ə":
                    # Initial Position: Beginning of a word chunk maps to Alif (ا)
                    if idx == 0:
                        output.append("ا")
                    # Final Position: End of a word chunk maps to Heh (ه)
                    elif idx == word_len - 1:
                        output.append("ه")
                    # Medial Position: Middle of a word chunk remains traditionally unwritten
                    else:
                        continue
                elif char in self.consonant_map:
                    output.append(self.consonant_map[char])
                else:
                    output.append(char)
                    
            processed_words.append("".join(output))
            
        return " ".join(processed_words)
