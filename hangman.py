import requests
import random
url = ('http://linkedin-reach.hagbpyjegb.us-west-2.elasticbeanstalk.com/words')
#stores the API url

r = requests.get(url)
#making a GET request call to the API to extract the data
# r is now a response object - I can get all the data I need from this object
# the data returns as one giant string, where every word is seperated by newline char (\n)

words = r.text.split()
# .text is a parameter i can call on the r object to read the content
#returns a list of words

# TESTING- looping through the list to pull out each word
# for word in words:
#     print word

secret_word = random.choice(words)
