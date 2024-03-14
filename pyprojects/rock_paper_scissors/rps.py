"""
    Rock beats scissors, scissors beat paper, and paper beats rock.
    Agree ahead of time whether you’ll count off “rock, paper, scissors, shoot” or just 
    “rock, paper, scissors.”
    Use rock, paper, scissors to settle minor decisions or simply play to pass the time.

    user decide best of N tries

    @author::
    @datetime::
"""
import random


# declare global variables
# store computer choices as a list
COMPUTER_CHOICE = ['r', 'p', 's']

# track winner of each round, thus winner of game
WINNER = {
    'user': 0,
    'computer': 0
}


def main():
    print("Ready! Set! -> Rock!, Paper!, Sissors!")
    print("Start by entering the number of rounds to play.")

    rounds = get_rounds()
    play(rounds)


def get_rounds():
    '''
        Function to get the user's input for the number 
        of rounds of rock paper sissors to play. 
        User's input is also validated to prevent errors.

        @input::  none
        @output::int -> user's entered number of rounds to play
    '''

    # loop as long as an invalid input is entered by user.
    while(True):

        try:
            # try casts users input to integer
            rounds = int(input("Number of rounds: "))

            # only accepts positive whole numbers
            if rounds > 0:
                return rounds
            else:
                print("Invalid Input, Please enter a positive number.")

        except ValueError:
            print("Invalid Input, Please enter a numberic value.")


def get_user_choice():
    ''' 

    '''
    while True:
         # get user's choice
        print("Enter [r/R - Rock | p/P - Paper | s/S - Sissors]")
        user_choice = input("Your choice: ")

        if user_choice.strip().lower() in COMPUTER_CHOICE:
            return user_choice.strip().lower()


# Rock beats scissors, scissors beat paper, and paper beats rock.
def who_wins_round(user_choice, computer_choice):
    '''

    '''

    if user_choice == computer_choice:
        print("Round Tie!")
        print()

    elif (user_choice == "r" and computer_choice == "s") or \
         (user_choice == "s" and computer_choice == "p") or \
         (user_choice == "p" and computer_choice == "r"):

         # update user's round count
         WINNER['user'] += 1
         
         print("User wins!")
         print()
         
    else:
        # update computer's round count
         WINNER['computer'] += 1
         
         print("Computer wins!")
         print()


def who_wins_game():
    pass


def play(rounds):
    '''
        Function to start the rock paper sissors game for number
        of rounds specified as input.

        @input::int -> number of rounds to play.  
        @output::
    '''
    print()


    for i in range(rounds):

        # get user's choice
        user_choice = get_user_choice()

        # get the computer choice
        computer_choice = random.choice(COMPUTER_CHOICE)
        print("Computer's choice is: ", computer_choice)

        # determine winner
        who_wins_round(user_choice, computer_choice)

    # print out the winner of the Rock Paper Sissors Game


if __name__ == '__main__':
    main()
