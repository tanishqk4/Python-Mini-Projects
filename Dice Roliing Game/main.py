import random

count = 0
while True:
    
    roll = input("Want to roll the dice? (y/n): ")
    if roll.lower() == "y":
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        print(f"({dice1}, {dice2})")
        count += 1

    elif roll.lower() == "n":
        print("Thankyou for playing!")
        print(f"You rolled the dice {count} times.")
        break
    else:
        print("Invalid Input")
