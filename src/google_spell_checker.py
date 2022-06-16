import requests
import json
import re


class GoogleSpellChecker:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
    }

    def __init__(self, zone='en-EN'):
        self.zone = zone
        self.url = "https://www.google.com/complete/search?client=gws-wiz&xssi=t"
        self.response = self.result = None

    def check_spelling(self, word, zone=None):
        zone = zone if zone is not None else self.zone
        self.response = requests.get(f"{self.url}&hl={zone}&q={word}", headers=self.headers)
        if self.response.status_code == 200:
            self.result = json.loads(f"{self.response.text[5:]}")
        return self.result

    def is_correct(self, word, zone=None):
        zone = zone if zone is not None else self.zone
        suggestions = self.check_spelling(word, zone=zone)
        if suggestions is not None and len(suggestions[0]) > 0 and len(suggestions[0][0]) > 0:
            if re.sub(r"<b>.+</b>", "", suggestions[0][0][0]).lower() == word.lower():
                return True, None
            else:
                if 'o' in suggestions[1]:
                    return False, re.sub(r"</?sc>", "", suggestions[1]['o'])
                else:
                    replacement = re.sub(r"</?b>", "", suggestions[0][0][0])
                    if replacement != "":
                        return False, replacement
                    else:
                        return False, None
        else:
            return False, None

    def get_suggestions(self):
        """
        Returns a list of suggestions for the word
        :return:
        """
        return self.result[0]


# Following is an example how to use the Google Spell Checker.
def main():
    spell_checker = GoogleSpellChecker()
    result = spell_checker.check_spelling("az-zuhaili")
    print(result)
    print(spell_checker.is_correct("az-zuhaili"))


if __name__ == "__main__":
    main()