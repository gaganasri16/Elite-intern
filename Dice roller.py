import random

def roll_die():
    return random.randint(1, 6)  # Generates a random number between 1 and 6

def main():
    print("Welcome to the Die Rolling Simulator!")
    while True:
        roll = input("Press 'r' to roll the die, or 'q' to quit: ").lower()
        if roll == 'r':
            print(f"You rolled a {roll_die()}!")
        elif roll == 'q':
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid input. Please press 'r' to roll or 'q' to quit.")

if __name__ == "__main__":
    main()
