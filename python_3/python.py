import random


def main():
    name = input("What's your name? ").strip() or "stranger"
    print(f"Hi {name}! Let's play a quick number game.")
    best = None

    while True:
        secret = random.randint(1, 20)
        tries = 0
        print("\nI'm thinking of a number from 1 to 20.")

        while True:
            try:
                guess = int(input("Your guess: "))
            except ValueError:
                print("  Enter a whole number.")
                continue
            tries += 1
            if guess < secret:
                print("  Higher!")
            elif guess > secret:
                print("  Lower!")
            else:
                print(f"  Correct in {tries} tries!")
                if best is None or tries < best:
                    best = tries
                    print("  New best score!")
                break

        if input("Play again? (y/n) ").strip().lower() != "y":
            break

    print(f"\nThanks for playing, {name}! Best score: {best or 'none yet'}.")


if __name__ == "__main__":
    main()