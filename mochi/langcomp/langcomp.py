import json

file = open(f'./mochi/langcomp/langcomp.txt', 'r')
lines = file.readlines()

data = {
	'~:decks': [
		{
			'~:name': f'Language and Composition',
			'~:cards': {
				'~#list': lines
			}
		}
	], 
	'~:version': 2,
	"~:templates": {
            "~#list": [
                {
                    "~:id": "~:langcompreverse",
                    "~:name": "Lang/Comp Vocab Reverse",
                    "~:content": "> (<< Part of Speech >>) << Definition >>\n---\n## << Word >> ({{<< Synonym >>}})",
                    "~:fields": {
                        "~:name": {
                            "~:id": "~:name",
                            "~:name": "Word"
                        },
                        "~:J84Z7tBQ": {
                            "~:id": "~:J84Z7tBQ",
                            "~:name": "Part of Speech"
                        },
                        "~:Wp2SuJDX": {
                            "~:id": "~:Wp2SuJDX",
                            "~:name": "Definition"
                        },
                        "~:BFb7DTV7": {
                            "~:id": "~:BFb7DTV7",
                            "~:name": "Synonym"
                        }
                    }
                }
            ]
        }
	}

for i in range(len(lines)):
	lines[i].replace('\n', '')
	word, syn, pos, define = lines[i].split('| ')
	word, syn, pos, define = word.replace('\n', ''), syn.replace('\n', ''), pos.replace('\n', ''), define.replace('\n', '')

	card = {
		'~:content': '',
		'~:name': word,
		'~:fields': {
			'~:name': {
				'~:id': '~:name',
				'~:value': word
			},
			'~:BFb7DTV7': {
				'~:id': '~:BFb7DTV7',
				'~:value': syn
			},
            '~:J84Z7tBQ': {
				'~:id': '~:J84Z7tBQ',
				'~:value': pos
			},
            '~:Wp2SuJDX': {
				'~:id': '~:Wp2SuJDX',
				'~:value': define
			},
		},
		'~:template-id': '~:langcompreverse'
	}

	data['~:decks'][0]['~:cards']['~#list'][i] = card

with open('./mochi/langcomp/data.json', 'w') as output:
	json.dump(data, output)
output.close()

print('done')