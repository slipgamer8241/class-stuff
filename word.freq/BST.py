"""
Author: Marcus Sweet
Date: 2025.03.31
Description:
    This program processes a given text to calculate word frequencies, filter out stop words, 
    and create a binary search tree of the words. It provides options to display all word frequencies, 
    find the word with the highest frequency, or search for the frequency of a specific word. 
    The text can be input manually or read from a file.
"""
import sys
import time

class TreeNode:
    """A node in a binary search tree that stores a word, its frequency, and references to left and right children."""
    def __init__(self, word):
        self.word = word
        self.frequency = 1
        self.left = None
        self.right = None

class BinarySearchTree:
    """A binary search tree for storing words and their frequencies."""
    def __init__(self):
        self.root = None

    def insert(self, word):
        """Insert a word into the BST or update its frequency if it already exists."""
        if self.root is None:
            self.root = TreeNode(word)
        else:
            self._insert_recursive(self.root, word)

    def _insert_recursive(self, node, word):
        if word == node.word:
            node.frequency += 1
        elif word < node.word:
            if node.left is None:
                node.left = TreeNode(word)
            else:
                self._insert_recursive(node.left, word)
        else:
            if node.right is None:
                node.right = TreeNode(word)
            else:
                self._insert_recursive(node.right, word)

    def get_all_frequencies(self):
        """Return all word frequencies as a dictionary."""
        frequencies = {}
        self._inorder_traversal(self.root, frequencies)
        return frequencies

    def _inorder_traversal(self, node, frequencies):
        if node is not None:
            self._inorder_traversal(node.left, frequencies)
            frequencies[node.word] = node.frequency
            self._inorder_traversal(node.right, frequencies)

    def get_max_frequency_word(self):
        """Return the word with the maximum frequency and its count."""
        max_word = None
        max_frequency = 0
        stack = [self.root]
        while stack:
            node = stack.pop()
            if node:
                if node.frequency > max_frequency:
                    max_frequency = node.frequency
                    max_word = node.word
                stack.append(node.left)
                stack.append(node.right)
        return (max_word, max_frequency)

    def search_word_frequency(self, word):
        """Return the frequency of a specific word."""
        return self._search_recursive(self.root, word)

    def _search_recursive(self, node, word):
        if node is None:
            return 0
        if word == node.word:
            return node.frequency
        elif word < node.word:
            return self._search_recursive(node.left, word)
        else:
            return self._search_recursive(node.right, word)


def preprocess_text(text):
    """Preprocess the text by removing punctuation and converting to lowercase."""
    cleaned_text = ''.join(char.lower() if char.isalpha() or char.isspace() else '' for char in text)
    return cleaned_text

def filter_stop_words(text, stop_words):
    """Filter out stop words from the text."""
    words = text.split()
    filtered_words = [word for word in words if word not in stop_words]
    return ' '.join(filtered_words)

def process_text(text, stop_words):
    """Process the text to calculate word frequencies and create a binary search tree."""
    text = preprocess_text(text)
    text = filter_stop_words(text, stop_words)

    words = text.split()
    bst = BinarySearchTree()
    for word in words:
        bst.insert(word)
    
    return bst


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
bst = process_text(text, stop_words)
end_time = time.time()
print("Processing time:", end_time - start_time, "seconds")

# Output options
print("Choose an option:")
print("1. Display all word frequencies")
print("2. Display the word with the maximum frequency")
print("3. Search for a specific word frequency")
option = input("Enter your choice (1/2/3): ")

if option == "1":
    print("All word frequencies:", bst.get_all_frequencies())

elif option == "2":
    print("Maximum frequency word:", bst.get_max_frequency_word())

elif option == "3":
    word = input("Enter a word to search: ")
    print(f"Frequency of '{word}':", bst.search_word_frequency(word))
else:
    print("Invalid option")