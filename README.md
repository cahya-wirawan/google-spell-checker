# Google Spell Checker

It is a simple multilingual Spell Checker using Google Text Completion.

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
### Different Language Code
The GoogleSpellChecker uses the default language code "en-EN", but you can change it by passing the parameter 
lang to GoogleSpellChecker() as follow:
```
# For example, we use lang="id" for Indonesian
spell_checker = GoogleSpellChecker(lang="id")
print(spell_checker.is_correct("sayalaparsekali, say ingn makn dirumha"))
# (False, 'saya lapar sekali, saya ingin makan di rumah')
```