import  requests

app_id = 'YOUR API ID'
app_key = 'YOUR API KEY'
language = 'en'
word_id = input("Enter a word: ")
url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/'  + language + '/'  + word_id.lower()
#url Normalized frequency
urlFR = 'https://od-api.oxforddictionaries.com:443/api/v1/stats/frequency/word/'  + language + '/?corpus=nmc&lemma=' + word_id.lower()

r = requests.get(url, headers = {'app_id' : app_id, 'app_key' : app_key})

while r.status_code == 404:
    print("Sorry, word not found.")
    word_id = input("Pleas enter another word: ")
    url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/'  + language + '/'  + word_id.lower()
    #url Normalized frequency
    urlFR = 'https://od-api.oxforddictionaries.com:443/api/v1/stats/frequency/word/'  + language + '/?corpus=nmc&lemma=' + word_id.lower()
    r = requests.get(url, headers = {'app_id' : app_id, 'app_key' : app_key})
    
else:
    data = r.json()

    definition = data['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]
    examples = data['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['examples']
    parts_of_speech = data['results'][0]['lexicalEntries'][0]['lexicalCategory']
    phoneticSpelling = data['results'][0]['lexicalEntries'][0]['pronunciations'][0]['phoneticSpelling']

    def show_examples(examples):
        for i in range(len(examples)):
            print('"{}"'.format(examples[i]['text']))

    print('Phonetic Spelling:\n-{}'.format(phoneticSpelling))
    print("Parts of Speech:\n-{}".format(parts_of_speech))
    print("Definition:\n-" + definition)
    print("Examples:")
    show_examples(examples)

#we get a KeyError: 'examples' when ninja is entered. try and figure this out.
