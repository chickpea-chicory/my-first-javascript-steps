import random

# Start the player with some cash
balance = 100


print("Welcome to the Python Casino!")
while balance > 0:
        print(f"Your starting balance is: ${balance}")


        # Step 1: Get the player's bet
        bet = int(input("How much do you want to bet?$"))

        # Step 2: Get their guess (odd or even)
        guess = input("Predict if the dice roll is odd or even): ").lower()

        rand = random.randint(1,6)

        if rand % 2 == 0 and guess == "even":
            print("You got it!")
            balance += bet
            print(f"You now have ${balance}")
        elif rand % 2 != 0 and guess == "odd":
            print("You got it!")
            balance += bet
            print(f"You now have ${balance}")
        else:
            print(f"Oh noes you did not get it, try again! The roll was {rand}.")
            balance -= bet
            print(f"You now have ${balance}")
            if balance == 0:
                print("shucks! you went broke! sorry!") and exit()











