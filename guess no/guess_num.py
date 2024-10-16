import random

def start_game():
        print("\t\tGUESS THE NUMBER!! (0 TO 20)")
        number = random.randint(0,20)
        ask_user(number)


def ask_user(num):
        user_input = int(input("\nGuess the number: "))
        #chances = 4
        if user_input != num:
                if user_input < num:
                        print("Your guess is low!")
                        ask_user(num)
                else:
                        print("Your guess is high!")
                        ask_user(num)
        else:
                print(f"You guessed it right!! The number was {num}")


start_game()
