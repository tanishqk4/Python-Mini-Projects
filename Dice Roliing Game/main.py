import random

while True:
    roll = input("Want to roll the dice? (y/n): ")
    if roll.lower() == "y":
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        print(f"({dice1}, {dice2})")
    else:
        print("Thankyou for playing!")
        break
