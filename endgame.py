# end game module

# imports global variables needed into this module
from setup import good_letters, bad_letters, unique_letters, secret_word, guess_limit


# function to end the game
def is_game_over():
    # both lists have to match in length in order to win the game
    # or else
    # bad letters and the guess limit have to match to lose the game
    # both statements return True which ends the game loop
    if len(unique_letters) == len(good_letters):
        print "\n" * 15
        print "You win! The word was {}".format(secret_word)
        print "\n" * 15
        return True
    elif len(bad_letters) == guess_limit:
        print "\n" * 15
        print "You didn't guess it! My word was {}".format(secret_word)
        print "\n" * 15
        return True
