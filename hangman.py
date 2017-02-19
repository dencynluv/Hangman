import requests
import random

#stores the API url
url = ('http://linkedin-reach.hagbpyjegb.us-west-2.elasticbeanstalk.com/words')

#making a GET request call to the API to extract the data
# r is now a response object - I can get all the data I need from this object
# the data returns as one giant string, where every word is seperated by newline char (\n)
r = requests.get(url)

# .text is a parameter i can call on the r object to read the content
#returns a list of words
words = r.text.split()

# TESTING- looping through the list to pull out each word
# for word in words:
#     print word

#Welcom loop
while True:
    #prompt the user to start the game or quit
    start = raw_input("Press enter/return to start, or Q to quit ")
    #check if the player decides to quit
    if start.lower() == 'q':
        #breaks out of the loop
        break

    secret_word = random.choice(words)
    #empty list to hold bad guesses
    bad_guesses = []
    #empty list to hold good guesses
    good_guesses = []

    # Game play loop - runs during game play until the player losses
    #conditional while loop that limits the player to 7 guesses by comparing it to the
    #length of the bad_guesses list
    #AND
    #the length of good_guesses and length of the list of secret word can't be
    #the same length in order to keep the game going.
    #both conditions need to be true or the game ends
    while len(bad_guesses) < 7 and len(good_guesses) != len(list(secret_word)):
        # for loop iterates through every letter in secret word list
        for letter in secret_word:
            # if the letter is in the good_guesses list
            # print the letter (on the same line)
            # if not print an underscore (on the same line)
            if letter in good_guesses:
                print letter,
            else:
                print '_',

        # print blank space for spacing
        print('')
        # informs the player how many guesses they have left by counting the length of bad_guesses
        print('Strikes: {}/7'.format(len(bad_guesses)))
        # print blank space for spacing
        print('')

        # gets the player's guess and immediately lower cases the input letter
        guess = raw_input("Guess a letter: ").lower()

        # Checks:
        # the length of the input is only 1 letter, prints error message and continues
        if len(guess) != 1:
            print("You can only guess a single letter!")
            continue
        # checks both lists if the input letter exists, prints error message and continues
        elif guess in bad_guesses or guess in good_guesses:
            print("You've already guessed that letter!")
            continue
        # checks that the input characters are only letters, prints error message and continues
        elif not guess.isalpha():
            print("You can only guess letters!")
            continue

        # if the input letter exists in the secret_word
        if guess in secret_word:
            # append that letter to good_guesses list
            good_guesses.append(guess)
            # player wins if the lenght of both list match, prints success message and exist
            if len(good_guesses) == len(list(secret_word)):
                print("You win! The word was {}".format(secret_word))
                break
            else:
                # if it is a bad guess append it to the bad_letters list
                bad_guesses.append(guess)
    # ends the game playing while loop if player runs out of guesses
    else:
        print("You didn't guess it! My word was {}".format(secret_word))

# Welcome loop continues and player can play again or quit the entire program
