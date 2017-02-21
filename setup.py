#setup module

# imports needed libraries
import requests
import random

url = ('http://linkedin-reach.hagbpyjegb.us-west-2.elasticbeanstalk.com/words')
#stores the API url

r = requests.get(url)
#making a GET request call to the API to extract the data
# r is now a response object - I can get all the data I need from this object
# the data returns as one giant string, where every word is seperated by newline char (\n)

words = r.text.split()
# calling text property to read the text of the r object
# using split method to split the giant string into a list of individual words

secret_word = random.choice(words)
# picks a random word from the list of words

unique_letters = set(secret_word)
# turns the secret word into a list of letters and removes any duplicates

good_letters = []
# empty list to collect good guesses made by the user

bad_letters = []
# empty list to collect bad guesses made by the user

guess_limit = 6
# setting the guessing limit to 6


#Debugging
# print secret_word
# print unique_letters
# print good_letters
# print bad_letters
# print guess_limit
