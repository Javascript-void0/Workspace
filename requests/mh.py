import requests

# get_words = requests.get('https://random-word-api.herokuapp.com/word?number=10')
# words = get_words.json()
words = []

for i in range(100):
    get_words = requests.get('https://random-words-api.vercel.app/word')
    json = get_words.json()
    words.append(json[0]['word'])

avaiable = []
for word in words:
    response = requests.get(f'https://api.minehut.com/server/{word}?byName=true')
    if response.status_code == 500:
        avaiable.append(word)
print(avaiable)