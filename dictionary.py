import requests

def getWord():
    word_id = input("Enter a word: ")
    return word_id

def getAPIdata(word_id):
    app_id = 'YOUR APP_ID'
    app_key = 'YOUR APP_KEY'
    language = 'en'
    url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/'  + language + '/'  + word_id.lower()
    #url Normalized frequency
    urlFR = 'https://od-api.oxforddictionaries.com:443/api/v1/stats/frequency/word/'  + language + '/?corpus=nmc&lemma=' + word_id.lower()

    r = requests.get(url, headers = {'app_id' : app_id, 'app_key' : app_key})

    return r

def displayResults(word_id, data):
    print(word_id.capitalize()+':')
    #prints Phonetic Spelling
    print('Phonetic Spelling:\n-{}'.format(data['results'][0]['lexicalEntries'][0]['pronunciations'][0]['phoneticSpelling']))
    #prints parts of speech
    for i in range(len((data['results'][0]['lexicalEntries']))):
        print('Parts of Speech:\n-{}'.format(data['results'][0]['lexicalEntries'][i]['lexicalCategory']))
        print("Definition:")
        #prints each of the definitions of the word.
        for j in range(len(data['results'][0]['lexicalEntries'][i]['entries'])):
            print('{}. {}'.format((j+1),data['results'][0]['lexicalEntries'][i]['entries'][j]['senses'][0]['definitions'][0]))
 

def main():
    word_id = getWord()
    r = getAPIdata(word_id)
    while r.status_code == 404:
        print("Sorry, word not found.")
        word_id = getWord()
        r = getAPIdata(word_id)
    data = r.json()
    displayResults(word_id, data)
    

main()
