import random


def get_valid_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("please choose integer number.")


def main():
    print("Number guessing game")

    min_range = get_valid_integer("please choose minimum integer number:")
    max_range = get_valid_integer("please choose maximum integer number:")
    if min_range >= max_range:
        print("wrong input")
        return
    secret_number = random.randint(min_range, max_range)
    attempts = 5

    print(f"please choose integer number between{min_range}and{max_range}and you have{attempts}chans to won.. ")

    while attempts > 0:
        guess = get_valid_integer("please Enter your guess number")

        if guess < min_range or guess > max_range:
            print(f"please choose integer number between{min_range}and{max_range}")
            continue

        attempts = attempts - 1
        if guess < secret_number:
            print("The number is larger")
        elif guess > secret_number:
            print("The number is smaller")
        else:
            print("congratulations! You guessed the correct number")
            break

        if attempts > 0:
            print(f"you have{attempts}selection")
        else:
            print(f"you lose..the number is {secret_number}")



ui = main()
