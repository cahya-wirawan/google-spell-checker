# Google Spell Checker

It is a simple Spell Checker using Google Search Engine.

## Usage

GoogleSpellChecker.is_correct(word) returns a tuple, the first variable is the correctness of the text,
the second variable is the most possible correct word (or None if it is a correct word).
```
from google_spell_checker import GoogleSpellChecker

spell_checker = GoogleSpellChecker()
print(spell_checker.is_correct("developmnet"))
# (False, 'development')
print(spell_checker.is_correct("martialartz"))
# (False, 'martial arts')
print(spell_checker.is_correct("amoxicillin-clavulanic"))
# (True, None)
```