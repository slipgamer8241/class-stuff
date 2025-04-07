"""
Author: Marcus Sweet
Date: 2025.03.31
Description:
    This program processes a given text to calculate word frequencies, filter out stop words, 
    and create a linked list of the words. It provides options to display all word frequencies, 
    find the word with the highest frequency, or search for the frequency of a specific word. 
    The text can be input manually or read from a file.
"""
import sys

class LinkedListNode:
    """A node in a linked list that stores a word and a reference to the next node."""
    def __init__(self, word):
        self.word = word
        self.next = None

def preprocess_text(text):
    """Preprocess the text by removing punctuation and converting to lowercase."""
    cleaned_text = ''.join(char.lower() if char.isalpha() or char.isspace() else '' for char in text)
    return cleaned_text

def filter_stop_words(text, stop_words):
    """Filter out stop words from the text."""
    words = text.split()
    filtered_words = [word for word in words if word not in stop_words]
    return ' '.join(filtered_words)

def calculate_word_frequencies(text):
    """Calculate the frequency of each word in the text."""
    words = text.split()
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    return word_freq

def create_linked_list(words):
    """Create a linked list from a list of words."""
    head = None
    current = None
    for word in words:
        node = LinkedListNode(word)
        if head is None:
            head = node
            current = node
        else:
            current.next = node
            current = node
    return head

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
    """Process the text to calculate word frequencies and create a linked list."""
    text = preprocess_text(text)
    text = filter_stop_words(text, stop_words)
    word_freq = calculate_word_frequencies(text)
    
    words = text.split()
    linked_list_head = create_linked_list(words)
    
    return word_freq, linked_list_head


if len(sys.argv) > 1:
    # Read text from the file provided as a command-line argument
    with open(sys.argv[1], 'r') as file:
        text = file.read()
else:
    # Prompt the user to enter text
    text = input("Enter text: ")
stop_words = set(["the", "a", "is", "in", "it", "of", "and", "to", "with", "that", "as", "for", "on", "at", "by", "an"])

# Process the text
word_freq, linked_list_head = process_text(text, stop_words)

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
