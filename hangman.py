#game play module
import random
from setup import unique_letters, good_letters, bad_letters, guess_limit, secret_word
from endgame import is_game_over

# counter = 6

# Welcome message (stand alone function?)
print "\n" * 15
print "Welcome to Hangman! A letter guessing game. Can you guess my secret word?"
print "\n" * 15

#Welcome loop
while True:
#prompt the user to start the game or quit(stand alone function?)
    start = raw_input("Press enter/return to start, or 'Q' to quit \n >>> ")
    #check if the player decides to quit
    if start.lower() == 'q':
        print "\n"
        print "Goodbye! I guess you don't like challenges."
        print "\n"
        #breaks out of the loop
        break
    print "\n" * 15

    # While the game is NOT over - keep going
    while not is_game_over():
        # list with messages a user sees when a correct guess is made, selected randomly
        toasts = ["Nice!", "You got this!", "Great guess!", "Good pick!", "Excellent choice!", "Good job!", "You got it right!"]
        right_message = random.choice(toasts)

        # list with messages a user sees when a wrong guess is made, selected randomly
        wrongs = ["Incorrect!", "Guess again", "Try again", "Keep trying!", "I don't think so!", "You got it wrong"]
        wrong_message = random.choice(wrongs)


# draws the letter spaces (stand alone function?)
        # informs the user of guesses remaining
        print "\n"
        print "You have {} guesses remaining. Make them count!".format(guess_limit)
        print "\n"

        # loop through bad_letters list and displays already guessed letters to the user
        for letter in bad_letters:
            print letter,
        print "\n"

        # loops through each letter in the secret word
        for letter in secret_word:
            # checks if the letter is in good letters list and display to the user
            if letter in good_letters:
                print letter,
            # prints an underscore for every letter in secret word
            else:
                print "_",
        print "\n"

# gets the player's guess (stand alone function?)
        # gets the player's guess and immediately lower cases the input letter
        guess = raw_input("Guess a letter: ").lower()

        print "\n" * 15

        # Checks:
        # the length of the input is only 1 letter, prints error message and continues
        if len(guess) != 1:
            print("You can only guess a single letter!")
            continue
        # checks that the input characters are only letters, prints error message and continues
        elif not guess.isalpha():
            print "It's a letter game you silly meerkat! You can only guess letters."
            continue
        # checks both lists if the input letter exists, prints error message and continues
        elif guess in good_letters or guess in bad_letters:
            print "You've already guessed that letter!"
            continue

        # if the input letter exists in the unique_letters list
        if guess in unique_letters:
            # append that letter to good_guesses list
            good_letters.append(guess)
            # correct guess random message displayed to user
            print right_message
        else:
            # append bad guesses to the bad_letters list
            bad_letters.append(guess)
            # decrement the guess limit everytime a bad guess is added to the bad_letters list
            guess_limit -= 1
            # counter -= 1 #use if I want to display guess left and the guess limit
            # wrong guess random message displayed to user
            print wrong_message
    # if game play loop ends due to win or loss
    else:
        # ask user if they want to play again and lower case the response
        play_again = raw_input("Play again? 'Y' for yes, 'N' for no \n >>> ").lower()
        # if the response is NOT 'n' - so it is 'y'
        if play_again != "n":
            # continue the loop and start the game again
            continue
        # if not break out of the loop and end game
        else:
            print "\n"
            print "Thanks for playing!"
            print "\n"
            break
