import math
import random


# functions go here

def yes_no(question):
    """Checks user response to a question is yes / no (y/n), return 'yes' or 'no'"""

    while True:

        response = input(question).lower()

        # check the user say yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes / no")


def instructions():
    """Shows user instructions"""

    print('''
    To begin, choose the number of rounds and either customise the game parameters or go with the default game (where
    secret number will be between 1 and 100).

    Then choose how many rounds you'd like to play <enter> for infinite mode.

    Your goal is to try to guess the secret number without running out of guesses

    Good luck my friend ( you need it trust me :p )


    ''')

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

def calc_guesses(low, high):
    num_range = high - low + 1
    max_raw = math.log2(num_range)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1
    return max_guesses

# parameters that already exists in base game
low_num = 0
high_num = 10
guesses_allowed = 5
# Set guesses used to zero at the start of each round
guesses_used = 0


# Main routine starts here

# Intialise game variables
mode = "regular"
rounds_played = 0
end_game = "no"
feedback = ""

game_history = []
all_scores = []


print("⬆️⬆️⬆️ Welcome to the Higher Lower Game 🔽🔽🔽")
print()

# ask the user if they want instructions (check they said yes / no)
want_instructions = yes_no("Do you want to see the instructions? ").lower()

# Display the instructions if the user want to see them...
if want_instructions == "yes":
    instructions()

# Ask user for number of rounds / infinite mode
num_rounds = int_check("Rounds <enter for infinite mode>: ",
                       low=1, exit_code="")

if num_rounds == "":
    mode = "infinite"
    num_rounds = 5


# Get Game parameters
low_num = int_check("Low Number? ")
high_num = int_check("High Number? ", low=low_num+1)



# Game loop starts here
while rounds_played < num_rounds:

    # Rounds heading
    if mode == "infinite":
        rounds_heading = f"\n♾️♾️♾️ Round {rounds_played + 1} (Infinite Mode) ♾️♾️♾️"
    else:
        rounds_heading = f"\n💿💿💿 Round {rounds_played + 1 } of {num_rounds} 💿💿💿"

    print(rounds_heading)
    print()

    # Round starts here
    # Set guesses used to zero at the start of each round
    guesses_used = 0
    already_guessed = []

    # Choose a 'secret' number between the low and high number
    secret = random.randint(low_num, high_num)

    guess = ""
    while guess != secret and guesses_used < guesses_allowed:
        guess = int_check("Guess ", low_num, high_num, exit_code="xxx")

        if guess == "xxx":
            # set end_game to use so that outer loop can be broken
            end_game = "yes"
            break

        # check that guess is not a duplicate
        if guess in already_guessed:
            print(f"You've already guessed {guess}. You've *still* used"
                  f" {guesses_used} / {guesses_allowed} guesses ")
            continue

        # if guess is not a duplicate, add it to the 'already guessed' list
        else:
            already_guessed.append(guess)

        guesses_used += 1

        if guess < secret and guesses_used <= guesses_allowed:
            feedback = (f"Too low please guess a higher number"
                        f"You've use {guesses_used} / {guesses_allowed}")

        elif guess > secret and guesses_used <= guesses_allowed:
            feedback = (f"Too high please guess a lower number"
                        f"You've use {guesses_used} / {guesses_allowed}")

        else:

            # three different win messages depending on number of guesses used
            if guesses_used == 1:
                feedback = "🍀🍀 Lucky! You got it first try!! 🍀🍀"
            elif guesses_used == guesses_allowed:
                feedback = f"Phew! You got it in {guesses_used} guesses."
            else:
                feedback = f"Well done! You guessed the secret number in {guesses_used} guesses"



        print(feedback)



    print()

    # Round ends here

    # if user has entered exit code, end game
    if end_game == "yes":
        break


    rounds_played += 1
    # if user are in infinite mode, increase number of rounds
    if mode == "infinite":
        num_rounds += 1

    all_scores.append(guesses_used)

    history_item = f"Round: {rounds_played} - {guesses_used} / {guesses_allowed} guesses"
    game_history.append(history_item)

else:
    feedback = "Sorry... You have no more guesses left. You lose try again next time! ^^"
    #print feedback to user
    print(feedback)

# Additional Feedback (warn user that they are running out of guesses)
if guesses_used == guesses_allowed - 1:
    print("\n💣💣💣 Careful - you have one last guess make it count!💣💣💣\n")

print()
print("End of round")

# Game loop ends here
if rounds_played > 0:

    # Game history / Statistics area
    all_scores.sort()
    best_score = all_scores[0]
    worst_score = all_scores[-1]
    average_score = sum(all_scores) / len(all_scores)

    # Output the statistics
    print("\n📊📊📊 Statistics 📊📊📊")
    print(f"Best:{best_score} | Worst{worst_score} | Average{average_score:.2f}")
    print()

    # Display the game history on request
    see_history = yes_no("Do you want to see your game history? ")
    if see_history == "yes":
        for item in game_history:
            print(item)

        print()
        print("Thanks for playing my game this took a while ❤️😭")