# Vandrico Guessing Game
# January 31, 2016
# Author: Phelan Harris

import json
import requests

# assuming a 32-bit integer (max 2,147,483,647)
myGuess = 1073741824
upper = 2147483648
lower = 0

url = 'http://52.8.142.239:8080/guess'
headers = {'content-type': 'application/json'}

# binary search
while True:
	print "Trying guess: %d" % myGuess
	r = requests.post(url, data = json.dumps({'guess': myGuess}), headers=headers)
	print(r.json()['message'])
	
	if r.json()['message'] == "too low":
		lower = myGuess
		myGuess = (upper + lower)/2 
	elif r.json()['message'] == "too high":
		upper = myGuess
		myGuess = (upper + lower)/2
	else:
		break;

print "The hidden number is %d!" % myGuess