class AzerbaijaniEngine:
    def __init__(self):
        # Expanded character-by-character mapping dictionary
        self.consonant_map = {
            "b": "ب",
            "p": "پ",
            "t": "ت",
            "m": "م",
            "n": "ن"
        }

    def convert_latin_to_arabic(self, text: str) -> str:
        """Module 3 Core: Converts explicit Latin letters to Arabic script characters."""
        if not text:
            return ""
        
        # Process the text character by character using our consonant mapping table
        output = [self.consonant_map.get(char.lower(), char) for char in text]
        return "".join(output)
