"""
Author: Marcus Sweet
Date: 2025.04.30
Description:
    This program processes a given text to calculate word frequencies, filter out stop words, 
    and store the word frequencies in a Python dictionary. It provides options to display all word frequencies, 
    find the word with the highest frequency, or search for the frequency of a specific word. 
    The text can be input manually or read from a file.
"""
import sys
import time

def preprocess_text(text):
    """Preprocess the text by removing punctuation, numbers, and converting to lowercase."""
    cleaned_text = ''.join(char.lower() if char.isalpha() or char.isspace() else '' for char in text)
    return cleaned_text

def filter_stop_words(text, stop_words):
    """Filter out stop words from the text."""
    words = text.split()
    filtered_words = [word for word in words if word not in stop_words]
    return ' '.join(filtered_words)

def calculate_word_frequencies(text):
    """Calculate the frequency of each word and store it in a dictionary."""
    words = text.split()
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    return word_freq

def get_all_frequencies(word_freq):
    """Return all word frequencies as a dictionary."""
    return word_freq

def get_max_frequency_word(word_freq):
    """Return the word with the maximum frequency and its count."""
    if not word_freq:
        return None
    max_word = max(word_freq, key=word_freq.get)
    return (max_word, word_freq[max_word])

def search_word_frequency(word_freq, word):
    """Return the frequency of a specific word."""
    return word_freq.get(word, 0)

def process_text(text, stop_words):
    """Process the text to calculate word frequencies using a Python dictionary."""
    text = preprocess_text(text)
    text = filter_stop_words(text, stop_words)
    word_freq = calculate_word_frequencies(text)
    return word_freq

if len(sys.argv) > 1:
    # Read text from the file provided as a command-line argument
    with open(sys.argv[1], 'r') as file:
        text = file.read()
else:
    # Prompt the user to enter text
    text = input("Enter text: ")

stop_words = set(["the", "a", "is", "in", "it", "of", "and", "to", "with", "that", "as", "for", "on", "at", "by", "an"])

# Process the text
start_time = time.time()
word_freq = process_text(text, stop_words)
end_time = time.time()  
print(f"Processing time: {end_time - start_time:.4f} seconds")

# Output options
print("Choose an option:")
print("1. Display all word frequencies")
print("2. Display the word with the maximum frequency")
print("3. Search for a specific word frequency")
option = input("Enter your choice (1/2/3): ")

if option == "1":
    print("All word frequencies:", get_all_frequencies(word_freq))

elif option == "2":
    print("Maximum frequency word:", get_max_frequency_word(word_freq))

elif option == "3":
    word = input("Enter a word to search: ")
    print(f"Frequency of '{word}':", search_word_frequency(word_freq, word))
else:
    print("Invalid option")