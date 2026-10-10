import pytest
from engine.core import AzerbaijaniEngine

def test_basic_consonant_mapping():
    engine = AzerbaijaniEngine()
    # Test a simple, unambiguous consonant conversion string
    assert engine.convert_latin_to_arabic("b") == "ب"
    assert engine.convert_latin_to_arabic("p") == "پ"
    
    # New unambiguous consonant tests
    assert engine.convert_latin_to_arabic("t") == "ت"
    assert engine.convert_latin_to_arabic("m") == "م"
    assert engine.convert_latin_to_arabic("n") == "ن"
