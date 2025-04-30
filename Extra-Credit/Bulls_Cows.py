def bulls_and_cows(secret, guess):
    # Initialize bulls and cows counters
    bulls = 0
    cows = 0

    # Dictionary to store the frequency of unmatched digits in the secret
    secret_count = {}
    guess_count = {}

    # First pass: Determine bulls and record unmatched digits
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            bulls += 1  # Correct digit in the correct position
        else:
            # Count unmatched digits in the secret and guess
            secret_count[secret[i]] = secret_count.get(secret[i], 0) + 1
            guess_count[guess[i]] = guess_count.get(guess[i], 0) + 1

    # Second pass: Determine cows by comparing unmatched digits
    for digit in guess_count:
        if digit in secret_count:
            # Count cows as the minimum of unmatched digit occurrences
            cows += min(secret_count[digit], guess_count[digit])

    # Return the result as a string in the format "xAyB"
    return f"{bulls}A{cows}B"
