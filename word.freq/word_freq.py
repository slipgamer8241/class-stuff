# Program: Word Frequencies
# Author: Gubanyi
# Date: 3/27/2025
#
# Description: Comparison of solutions to the word frequency problem using
#              multiple data structures.


class WordFreqNode:
    """A node in a linked list to store word frequency."""
    
    def __init__(self, word, freq=1):
        """Initialize the node with a word and its frequency."""
        self.word = word
        self.freq = freq
        self.next = None

    def __str__(self):
        """Return a string representation of the linked list."""
        lines = []
        current = self
        while current:
            lines.append(f'{current.word}: {current.freq}')
            current = current.next
        return '\n'.join(lines)


def word_freq_list(text):
    """
    Compute word frequency using a singly linked list.

    This method is inefficient (O(n^2) in the worst case) because each new word requires 
    searching through the entire list before adding or updating a node.
    """
    # Normalize text: Remove punctuation and convert to lowercase
    text = text.replace(",", "").replace(".", "").lower()
    words = text.split()

    # Create the first node with the first word
    first_node = WordFreqNode(words[0])

    # Process remaining words
    for w in words[1:]:
        current_node = first_node

        # Traverse the linked list to find or insert the word
        while current_node.next and current_node.word != w:
            current_node = current_node.next

        if current_node.word == w:
            # Word found, increment frequency and move on
            current_node.freq += 1
        else:
            # Word not found, add a new node at the end of list
            new_node = WordFreqNode(w)
            current_node.next = new_node

    return first_node


def word_freq_dict(text):
    """
    Compute word frequency using a built-in python dictionary (which is a hash map).

    This method is more efficient (O(n) on average) because dictionaries provide constant-time lookups.
    """
    # Normalize text: Remove punctuation and convert to lowercase
    text = text.replace(",", "").replace(".", "").lower()
    words = text.split()

    freq = {}

    for w in words:
        if w in freq:
            freq[w] = freq[w] + 1
        else:
            freq[w] = 1

    return freq


if __name__ == "__main__":
    print()
    print("-----Word Frequency Calculator-----")
    print("Counts the number of times each word")
    print("appears in a string. Compares solutions")
    print("that use different data structures.")
    print()
    print("Program compares outputs and execution times.")
    print()

    mode = input("Enter T to run time comparison: ")
    print()
    
    if mode == "T":
        print("Time Comparisons of Linked List and Dictionary Solutions")
        for portion in [0.001, 0.01, 0.1, 0.5, 1]:
            text = open("lorem_ipsum.txt").read()
            text = text[0:int(len(text) * portion)]

            # Time each function
            import timeit
            execution_time_list = timeit.timeit(lambda: word_freq_list(text), number=100)
            execution_time_dict = timeit.timeit(lambda: word_freq_dict(text), number=100)

            print(f"Length of Text: {len(text)}")
            print(f"  Linked List Execution Time: {execution_time_list}")
            print(f"  Dictionary Execution Time: {execution_time_dict}")
    else:
        text = "In the beginning was the Word, and the Word was with God, and the Word was God."
        # Compute word frequencies using both methods

        linked_list_result = word_freq_list(text)
        dict_result = word_freq_dict(text)

        # Print results
        print("Output Comparison of Linked List and Dictionary Solutions")
        print("Word Frequency (Linked List):")
        print(linked_list_result)
        print("\nWord Frequency (Dictionary):")
        for word, count in dict_result.items():
            print(f"{word}: {count}")

