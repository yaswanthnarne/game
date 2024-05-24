import random

def get_computer_choice():
    # Generate a random choice (rock, paper, or scissors) for the computer
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_user_choice():
    # Prompt the user to choose rock, paper, or scissors
    choice = input("Choose rock, paper, or scissors: ")
    return choice.lower()

def determine_winner(user_choice, computer_choice):
    # Determine the winner based on the user's choice and the computer's choice
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

def main():
    # Initialize scores
    user_score = 0
    computer_score = 0

    while True:
        # Get the user's choice and the computer's choice
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        # Display the user's choice and the computer's choice
        print(f"User chose {user_choice}")
        print(f"Computer chose {computer_choice}")

        # Determine the winner and display the result
        winner = determine_winner(user_choice, computer_choice)
        if winner == 'user':
            print("User wins!")
            user_score += 1
        elif winner == 'computer':
            print("Computer wins!")
            computer_score += 1
        else:
            print("It's a tie!")

        # Display the scores
        print(f"User score: {user_score}")
        print(f"Computer score: {computer_score}")

        # Ask the user if they want to play another round
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            break

if __name__ == "__main__":
    main()