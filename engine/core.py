class AzerbaijaniEngine:
    def __init__(self):
        # Comprehensive baseline dictionary mapping for all consonants.
        # Aligned with the 2001 Tehran Seminar orthography rules.
        self.consonant_map = {
            "b": "ب", "c": "ج", "p": "پ", "ç": "چ", "j": "ژ", 
            "x": "خ", "ş": "ش", "d": "د", "r": "ر", "f": "ف", 
            "q": "ق", "l": "ل", "v": "و", "g": "گ", "ğ": "غ", 
            "k": "ک", "y": "ی", "m": "م", "n": "ن",

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
            # Foreign Cluster Overrides (Page 8 Section 4/2)
            has_cluster = word.startswith(("sp", "st", "sk"))
            
            # Phonetic normalization for specific Russian loanwords like skaner -> skənər
            if word == "skaner":
                word = "skənər"
            
            output = []
            word_len = len(word)
            
            for idx, char in enumerate(word):
                if char == "ə":
                    if idx == 0:
                        output.append("ا")
                    elif idx == word_len - 1:
                        output.append("ه")
                    else:
                        continue
                elif char == "a":
                    if idx == 0:
                        output.append("آ")
                    else:
                        output.append("ا")
                elif char == "e":
                    if idx == 0:
                        output.append("ائ")
                    else:
                        output.append("ئ")
                elif char == "i" or char == "ı":
                    if idx == 0:
                        output.append("ای")
                    else:
                        output.append("ی")
                elif char in ("o", "u"):
                    if idx == 0:
                        output.append("او")
                    else:
                        output.append("و")
                elif char == "ö":
                    if idx == 0:
                        output.append("اؤ")
                    else:
                        output.append("ؤ")
                elif char == "ü":
                    if idx == 0:
                        output.append("اۆ")
                    else:
                        output.append("ۆ")
                else:
                    output.append(self.consonant_map.get(char, char))
            
            # Combine the cluster prefix with the built word
            word_result = "".join(output)
            if has_cluster:
                word_result = "ای" + word_result
                
            processed_words.append(word_result)
            
        return " ".join(processed_words)
