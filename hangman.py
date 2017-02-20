#game play module

from setup import unique_letters, good_letters, bad_letters, guess_limit, secret_word, right_message, wrong_message
from endgame import is_game_over

# counter = 6

#Welcome loop
while True:
#prompt the user to start the game or quit(stand alone function?)
    start = raw_input("Press enter/return to start, or Q to quit ")
    #check if the player decides to quit
    if start.lower() == 'q':
        print "\n"
        print "Goodbye!"
        print "\n"
        #breaks out of the loop
        break
    print "\n" * 15

    # While the game is NOT over - keep going
    while not is_game_over():
# draws the letter spaces (stand alone function?)
        print "\n"
        print "You have {} guesses remaining. Make them count!".format(guess_limit)
        print "\n"

        for letter in bad_letters:
            print letter,
        print "\n"

        for letter in secret_word:
            if letter in good_letters:
                print letter,
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
            print right_message
        else:
            # if bad guess append it to the bad_letters list
            bad_letters.append(guess)
            guess_limit -= 1
            # counter -= 1
            print wrong_message
    else:
        play_again = raw_input("Play again? Y/n ").lower()
        if play_again != 'n':
            continue
        else:
            print "\n"
            print "Thanks for playing!"
            print "\n"
            break
