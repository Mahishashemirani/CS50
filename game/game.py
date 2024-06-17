import random

def get_valid_level():
    while True:
        try:
            x = int(input("level: "))
            if x > 0:
                return x
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def get_valid_guess(level):
    while True:
        try:
            guess = int(input("guess: "))
            if 1 <= guess <= level:
                return guess
            else:
                print("Too large!")
        except ValueError:
            print(f"Invalid input. Please enter an integer between 1 and {level}.")

def main():
    level = get_valid_level()
    sol = random.randint(1, level)

    while True:
        guess = get_valid_guess(level)

        if guess < sol:
            print("Too small!")
        elif guess > sol:
            print("Too large!")
        else:
            print("Just right!")
            break


if __name__ == "__main__":
    main()
