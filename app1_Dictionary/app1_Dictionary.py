'''
Description: A program that outputs the definition of a word.
Features: uses python command lines,
Name: LenC

'''

import json
from difflib import get_close_matches

data=json.load(open('app1_data.json'))

def translate(word):
	word=word.lower()
	if word in data:
		return data[word]
	elif len(get_close_matches(word,data.keys()))>0:
		ans=input("Did you mean '%s' instead? Enter Y/N: " % (get_close_matches(word,data.keys()))[0])
		if ans.lower()=='y':
			return data[get_close_matches(word,data.keys())[0]]
		elif ans.lower()=='n':
			return "The word doesn't exist. Please double check it."
		else:
			return "We didn't understand your response."
	else:
		return "The word doesn't exist. Please double check it."

word=input('Enter word: ')

output = translate(word)

if type(output) ==list:
	for item in output:
		print(item)
else:
	print(output)
