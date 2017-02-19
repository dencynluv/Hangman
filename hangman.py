#game play module

from setup import unique_letters, good_letters, bad_letters, guess_limit, secret_word
from endgame import is_game_over

#Welcome loop
while True:
    #prompt the user to start the game or quit
    start = raw_input("Press enter/return to start, or Q to quit ")
    #check if the player decides to quit
    if start.lower() == 'q':
        print "Goodbye!"
        #breaks out of the loop
        break

    while not is_game_over():
# draws the letter spaces (stand alone function?)
        # for loop iterates through every letter in secret word list
        for letter in secret_word:
            # if the letter is in the good_letters list
            # print the letter (on the same line)
            # if not print an underscore (on the same line)
            if letter in good_letters:
                print letter,
            else:
                print '_',

        # print blank space for spacing
        print " "
        # informs the player how many guesses they have left by counting the length of bad_letters
        print "You have {}/{} guesses remaining.".format(len(bad_letters), guess_limit)
        # print blank space for spacing
        print " "
        # print every letter in bad_letters list
        for letter in bad_letters:
            print letter,
        print " "

# gets the player's guess (stand alone function?)
        # gets the player's guess and immediately lower cases the input letter
        guess = raw_input("Guess a letter: ").lower()

        # Checks:
        # the length of the input is only 1 letter, prints error message and continues
        if len(guess) != 1:
            print("You can only guess a single letter!")
            continue
        # checks that the input characters are only letters, prints error message and continues
        elif not guess.isalpha():
            print("You can only guess letters!")
            continue
        # checks both lists if the input letter exists, prints error message and continues
        elif guess in good_letters or guess in bad_letters:
            print("You've already guessed that letter!")
            continue

        # if the input letter exists in the unique_letters list
        if guess in unique_letters:
            # append that letter to good_guesses list
            good_letters.append(guess)
        else:
            # if bad guess append it to the bad_letters list
            bad_letters.append(guess)
