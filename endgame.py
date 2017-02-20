# end game module

from setup import good_letters, bad_letters, unique_letters, secret_word, guess_limit
# from hangman import guess

#removed guess from parameter
def is_game_over():
    # if guess in good_letters or guess in bad_letters:
    #     print "You've already guessed that letter!"
    #     return False

    # if guess in unique_letters:
    #     good_letters.append(guess)
    # else:
    #     bad_letters.append(guess)

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
