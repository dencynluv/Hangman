#setup module
import requests
import random

url = ('http://linkedin-reach.hagbpyjegb.us-west-2.elasticbeanstalk.com/words')
#stores the API url

r = requests.get(url)
#making a GET request call to the API to extract the data
# r is now a response object - I can get all the data I need from this object
# the data returns as one giant string, where every word is seperated by newline char (\n)

words = r.text.split()

secret_word = random.choice(words)
unique_letters = set(list(secret_word))
good_letters = []
bad_letters = []
guess_limit = 6

print secret_word
print unique_letters
print good_letters
print bad_letters
print guess_limit
