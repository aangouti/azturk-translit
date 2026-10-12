import pytest
import pytest
from engine.core import AzerbaijaniEngine

def test_basic_consonant_mapping():
    engine = AzerbaijaniEngine()
    
    # Baseline tests
    assert engine.convert_latin_to_arabic("b") == "ب"
    assert engine.convert_latin_to_arabic("p") == "پ"
    assert engine.convert_latin_to_arabic("t") == "ت"
    assert engine.convert_latin_to_arabic("m") == "م"
    assert engine.convert_latin_to_arabic("n") == "ن"
    assert engine.convert_latin_to_arabic("ç") == "چ"
    assert engine.convert_latin_to_arabic("j") == "ژ"
    assert engine.convert_latin_to_arabic("x") == "خ"
    assert engine.convert_latin_to_arabic("ş") == "ش"
    assert engine.convert_latin_to_arabic("d") == "د"
    assert engine.convert_latin_to_arabic("r") == "ر"
    assert engine.convert_latin_to_arabic("z") == "ز"
    assert engine.convert_latin_to_arabic("s") == "س"
    assert engine.convert_latin_to_arabic("f") == "ف"
    assert engine.convert_latin_to_arabic("q") == "ق"
    assert engine.convert_latin_to_arabic("l") == "ل"
    assert engine.convert_latin_to_arabic("v") == "و"
    
    # Final consonant alphabet batch
    assert engine.convert_latin_to_arabic("g") == "گ"
    assert engine.convert_latin_to_arabic("ğ") == "غ"
    assert engine.convert_latin_to_arabic("h") == "ه"
    assert engine.convert_latin_to_arabic("k") == "ک"
    assert engine.convert_latin_to_arabic("y") == "ی"

