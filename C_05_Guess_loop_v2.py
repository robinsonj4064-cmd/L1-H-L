# check for an integer with optional upper /
# lower limits and an optional exit code for infinite mode
# / quitting the game
def int_check(question, low=None, high=None, exit_code=None):

    if low is None and high is None:
        error = "Please enter an integer"

    # if the number needs to be more than an
    # integer (ie: rounds / 'high number'
    elif low is not None and high is None:
        error = (f"Please enter an integer that is"
                 f"more than / equal to {low}")

    #if the number needs to between low and high
    else:
        error = (f"Please enter an integer that "
                 f"is between {low} and {high} (inclusive)")

    while True:

        response = input(question).lower()

        # check for infinite mode / exit code
        if response == exit_code:
            return response

        try:
            response = int(response)

            # if response is valid, return it

            if low is None and high is None:
                return response

            # Check the integer is not too low...
            if low is not None and response < low:
                print(error)

            # check response is more than the low number
            elif high is not None and response > high:
                print(error)

            # if the response is valid, return it
            else:
                return response

        except ValueError:
                print(error)


# Guessing loop

# replace number below with random number between high / low values
secret = 7
# parameters that already exists in base game
low_num = 0
high_num = 10
guesses_allowed = 5
already_guessed = []
# Set guesses used to zero at the start of each round
guesses_used = 0

guess = ""
while guess != secret and guesses_used < guesses_allowed:
    guess = int_check("Guess ", low_num, high_num)

    if guess =="xxx":
        # set end_game to use so that outer loop can be broken
        end_game = "yes"
        break

    # check that guess is not a duplicate
    if guess in already_guessed:
        print(f"You've already guessed {guess}. You've *still* used"
              f"{guesses_used} / {guesses_allowed} guesses ")
        continue

    # if guess is not a duplicate, add it to the 'already guessed' list
    else:
        already_guessed.append(guess)

    guesses_used += 1

    if guess < secret and guesses_used < guesses_allowed:
        feedback = (f"Too low please guess a higher number"
                    f"You've use {guesses_used} / {guesses_allowed}")

    elif guess > secret and guesses_used < guesses_allowed:
        feedback = (f"Too high please guess a lower number"
                         f"You've use {guesses_used} / {guesses_allowed}")

    else:
        feedback = f"Congrats u guessed the number ❤️ You used {guesses_used}"

    print(feedback)

    if guesses_used == 1:
        feedback = "🍀🍀 Lucky! You got it first try!! 🍀🍀"
    elif guesses_used == guesses_allowed:
        feedback = f"Phew! You got it in {guesses_used} guesses."
    else:
        feedback = f"Well done! You guessed the secret number in {guesses_used} guesses"

# if no more guesses
else:
    feedback = "Sorry... You have no more guesses left. You lose try again next time! ^^"
    #print feedback to user
    print(feedback)

# Additional Feedback (warn user that they are running out of guesses)
if guesses_used == guesses_allowed - 1:
    print("\n💣💣💣 Careful - you have one last guess make it count!💣💣💣\n")

print()
print("End of round")