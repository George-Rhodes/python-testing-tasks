import pytest
from applications import vowels



def test_word_vowels():
    assert vowels.vowels('sauceybegger') == 4

def test_predetermined_vowels():
    assert vowels.vowels('aaaauuuuoooo') == 12

def test_novowels():
    assert vowels.vowels('crypt') == 0