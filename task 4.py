import random

def get_cc():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(uc, cc):
    if uc == cc:
        return 'tie'
    elif (uc == 'rock' and cc == 'scissors') or \
         (uc == 'scissors' and cc == 'paper') or \
         (uc == 'paper' and cc == 'rock'):
        return 'user'
    else:
        return 'computer'

def display_result(uc, cc, winner):
    print(f"\nYou chose: {uc}")
    print(f"Computer chose: {cc}")
    
    if winner == 'tie':
        print("It's a tie!")
    elif winner == 'user':
        print("You win!")
    else:
        print("Computer wins!")

def main():
    user_score = 0
    computer_score = 0

    print("Welcome to Rock, Paper, Scissors!")
    while True:
        uc = input("\nEnter your choice (rock, paper, or scissors): ").lower()
        
        if uc not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue
        
        cc = get_cc()
        winner = determine_winner(uc, cc)
        display_result(uc, cc, winner)
        
        if winner == 'user':
            user_score += 1
        elif winner == 'computer':
            computer_score += 1
        
        print(f"\nScore: You {user_score} - Computer {computer_score}")
        
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break
    
    print("\nThanks for playing!")
    print(f"Final Score: You {user_score} - Computer {computer_score}")

if __name__ == "__main__":
    main()
