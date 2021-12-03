import requests
from pprint import pprint as print
import json
app_id = "72e0c319"
app_key = "c176e38e56492503618db74be48292c5"
language = "en-gb"

def getDefinitions(word_id):
    url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
    r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
    # print(r.status_code)
    res = r.json()

    if 'error' in res.keys():
        return False


    output = {}
    senses = res['results'][0]['lexicalEntries'][0]['entries'][0]['senses']
    definitions = []

    for sense in senses:
        definitions.append(f"👉 {sense['definitions'][0]}")
    output['definitions'] = "\n".join(definitions)

    if res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0].get('audioFile'):
        output['audio'] = res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile']
    return output

if __name__ == '__main__':
    print(getDefinitions('Uzbekistan'))
    print(getDefinitions('American'))



