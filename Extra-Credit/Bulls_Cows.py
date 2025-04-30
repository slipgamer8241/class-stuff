

def bulls_and_cows(secret, guess):

    bulls = 0
    cows = 0

    secret_count = {}
    guess_count = {}

    for i in range(len(secret)):
        if secret[i] == guess[i]:
            bulls += 1
        else:

            secret_count[secret[i]] = secret_count.get(secret[i], 0) + 1
            guess_count[guess[i]] = guess_count.get(guess[i], 0) + 1

    for digit in guess_count:
        if digit in secret_count:
            # Count cows as the minimum of unmatched digit occurrences
            cows += min(secret_count[digit], guess_count[digit])

    return f"{bulls}A{cows}B"
