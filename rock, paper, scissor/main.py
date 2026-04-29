import random

emojis = {
    "r": "Rock 🪨",
    "p": "Paper 📄",
    "s": "Scissor ✂️"
}
while True:
    choice = input("Enter your choice - rock, paper, scissor(r,p,s): ").lower()
    if choice in ['r', 'p', 's']:
        print(f"Your choice: {emojis[choice]}")

        
        computer_choice = random.choice(["r", "p", "s"])
        print(f"Computer choice: {emojis[computer_choice]}")
        
        if choice == computer_choice:
            print("It's a Draw!")
        elif (choice == 'r' and computer_choice == 's') or (choice == 'p' and computer_choice == 'r') or (choice == 's' and computer_choice == 'p'):
            print("You Win!")
        else:
            print("Computer Wins!")
    else:
        print("Invalid choice. Please enter r, p, or s.")

    play_again = input("want to play again?(y/n): ").lower()
    if play_again == 'n':
        print("Thanks for playing!")
        break
    