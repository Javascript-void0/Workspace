import json

unit = '1b'
file = open(f'./mochi/spanish/lists/{unit}.txt', 'r')
lines = file.readlines()

data = {
	'~:decks': [
		{
			'~:name': f'Unit {unit}',
			'~:cards': {
				'~#list': lines
			}
		}
	], 
	'~:version': 2,
	"~:templates": {
			"~#list": [
				{
					"~:id": "~:FuMxHcs7",
					"~:name": "Spanish Vocab",
					"~:content": "<< Spanish >>\n---\n<< English >>",
					"~:fields": {
						"~:name": {
							"~:id": "~:name",
							"~:name": "Spanish"
						},
						"~:vybf00dv": {
							"~:id": "~:vybf00dv",
							"~:name": "English"
						}
					}
				}
			]
		}
	}

for i in range(len(lines)):
	lines[i].replace('\n', '')
	spanish, english = lines[i].split('; ')
	spanish, english = spanish.replace('\n', ''), english.replace('\n', '')

	card = {
		'~:content': '',
		'~:name': english,
		'~:fields': {
			'~:name': {
				'~:id': '~:name',
				'~:value': english
			},
			'~:vybf00dv': {
				'~:id': '~:vybf00dv',
				'~:value': spanish
			}
		},
		'~:template-id': '~:FuMxHcs7'
	}

	data['~:decks'][0]['~:cards']['~#list'][i] = card

with open('./mochi/spanish/data.json', 'w') as output:
	json.dump(data, output)
output.close()

print('done')