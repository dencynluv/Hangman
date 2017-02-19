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


while True:
    start = raw_input("Press enter/return to start, or Q to quit ")
    if start.lower() == 'q':
        break

    secret_word = random.choice(words)
    bad_guesses = []
    good_guesses = []

    while len(bad_guesses) < 7 and len(good_guesses) != len(list(secret_word)):
        for letter in secret_word:
            if letter in good_guesses:
                print letter,
            else:
                print '_',

        print('')
        print('Strikes: {}/7'.format(len(bad_guesses)))
        print('')

        guess = raw_input("Guess a letter: ").lower()

        if len(guess) != 1:
            print("You can only guess a single letter!")
            continue
        elif guess in bad_guesses or guess in good_guesses:
            print("You've already guessed that letter!")
            continue
        elif not guess.isalpha():
            print("You can only guess letters!")
            continue

        if guess in secret_word:
            good_guesses.append(guess)
            if len(good_guesses) == len(list(secret_word)):
                print("You win! The word was {}".format(secret_word))
                break
        else:
            bad_guesses.append(guess)
    else:
        print("You didn't guess it! My word was {}".format(secret_word))

