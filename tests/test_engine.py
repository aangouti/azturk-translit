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

def test_positional_vowel_ə():
    engine = AzerbaijaniEngine()
    
    # Test 'ə' at the beginning of a word (Initial -> Alif)
    # əl -> ا + ل = ال
    assert engine.convert_latin_to_arabic("əl") == "ال"
    
    # Test 'ə' inside a word (Medial -> Omitted) and at the end (Final -> Heh)
    # dədə -> د + (omitted) + د + ه = دده
    assert engine.convert_latin_to_arabic("dədə") == "دده"

def test_harmonic_velar_variations():
    engine = AzerbaijaniEngine()
    
    # ka maps to کا
    assert engine.convert_latin_to_arabic("ka") == "کا"
    assert engine.convert_latin_to_arabic("kə") == "که"
    
    # ga maps to گا
    assert engine.convert_latin_to_arabic("ga") == "گا"
    assert engine.convert_latin_to_arabic("gə") == "گه"

def test_vowel_a_positional():
    engine = AzerbaijaniEngine()
    
    # 'A' at start -> آ, inside/end -> ا
    assert engine.convert_latin_to_arabic("Ata") == "آتا"
    assert engine.convert_latin_to_arabic("Ada") == "آدا"
