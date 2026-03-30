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

def int_check(question):
    """Checks users enetr on integer more than / equal to 13"""

    while True:
        error = "Please enter an integer that is 1 or more."

        response = input(question)

        # check for infinite mode
        if response == "":
            return "infinite"

        try:
            response =int(response)

            #check that the number is more than / equal to 13
            if response < 1:
                print(error)

            else:
                return response

        except ValueError:
            print(error)


# Automated testing is below in the form (test_case, expected_value)
while True:
    num_rounds = int_check("How many rounds? ")
    print(f"you chose {num_rounds}")



# Main routine starts here

# Intialise game variables
mode = "regular"
rounds_played = 0


print("⬆️⬆️⬆️ Welcome to the Higher Lower Game 🔽🔽🔽")
print()

# ask the user if they want instructions (check they said yes / no)
want_instructions = yes_no("Do you want to see the instructions? ").lower()

# Display the instructions if the user want to see them...
if want_instructions == "yes":
    instructions()

# Ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like? Push <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# Game loop starts here
while rounds_played < num_rounds:

    # Rounds heading
    if mode == "infinite":
        rounds_heading = f"\n♾️♾️♾️ Round {rounds_played + 1} (Infinite Mode) ♾️♾️♾️"
    else:
        rounds_heading = f"\n💿💿💿 Round {rounds_played + 1 } of {num_rounds} 💿💿💿"

        print(rounds_heading)
        print()

    user_choice = input("Choose: ")

    if user_choice == "xxx":
        break


    rounds_played += 1
    # if user are in infinite mode, increase number of rounds
    if mode == "infinite":
        num_rounds += 1


# Game loop ends here

# Game history / Statistics area