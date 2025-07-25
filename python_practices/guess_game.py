import random

def main():

    attempts = 0
    max_attempts = 10

    while True:
        print("Welcome to my guessing game!")
        print("Guess the lucky number from 1-100!\n")
        print(f"Note: You only have {max_attempts} attempts, Goodluck!")
        target = random.randint(1,100)
        while attempts < max_attempts:
            try:
                guess = int(input(f"Attempt {attempts + 1}/{max_attempts} Guess: "))
                attempts += 1


                if guess == target:
                    print("You have won 1000 dollars!\n")
                    break
                elif guess > target:
                    print("Too High! Try another number\n")
                else:
                    print("Too Low! Try another number\n")
            except ValueError:
                print("Please enter a valid number!")

        else: 
            print(f"You have ran out of attempts! The lucky number was {target}")

        while True:

            choice = input("Do you want to play again? (y/n): ").lower()
            if choice in ['y']:
                break
            elif choice in ['n']:
                print("Thank you for playing")
                return
            else:
                print("Please enter a valid input y or n!")
                continue

if __name__ == "__main__":
    main()