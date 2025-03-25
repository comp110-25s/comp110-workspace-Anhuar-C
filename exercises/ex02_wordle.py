"""Create a game similar to Wordle"""

__author__: str = "730705182"


def contains_char(word: str, char: str) -> bool:
    """Check if the single character is found in the given word"""
    assert len(char) == 1, f"len('{char}') is not 1"
    i: int = 0
    found: bool = False  # set False as default output

    while i < len(
        word
    ):  # word index cannot be longer than length of the word (mandatory)
        found = found or (
            word[i] == char
        )  # Return default False or search through word until char found
        i += 1

    return found


def emojified(guess: str, secret: str) -> str:
    """Return a string of emoji boxes representing the accuracy of the guess"""
    assert len(guess) == len(secret), "Guess must be the same length as secret"

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    result: str = ""  # Make str where boxes will be added
    i: int = 0  # Begim index at 0

    while i < len(secret):
        result += (
            (GREEN_BOX * (guess[i] == secret[i]))
            + (YELLOW_BOX * (contains_char(secret, guess[i]) and guess[i] != secret[i]))
            + (WHITE_BOX * (not contains_char(secret, guess[i])))
        )  # Add boxes to str according to placement and if they are matching/correct, otherwise go through index
        i += 1
    return result


def input_guess(expected_length: int) -> str:
    """Prompt the user to input a guess of the expected length"""
    guess: str = input(f"Enter a {expected_length} character word: ")
    while (
        len(guess) != expected_length
    ):  # Enter a word that matches to the corresponding input length
        guess = input(
            f"That wasn't {expected_length} chars! Try again: "
        )  # Try again if length does not match
    return guess


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"  # Set word that player must guess
    turn: int = 1
    won: bool = False
    while turn <= 6 and not won:  # Max 6 turns
        print(f"===Turn {turn}/6===")
        guess: str = input_guess(len(secret_word))  # Players guess/input
        print(emojified(guess, secret_word))  # Feedback of boxes
        if guess == secret_word:
            won = True  # If player guess matches set word, they win!
        else:
            turn += 1  # Otherwise, they are given another turn
    if won:
        print(f"You won in {turn}/6 turns!")  # Message for winning in N tries
    else:
        print(
            "X/6 - Sorry, try again tomorrow!"
        )  # Message for losing after all 6 attempts


if __name__ == "__main__":
    main(secret="codes")
