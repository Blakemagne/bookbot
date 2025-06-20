"""
BookBot - A Text Analysis Tool

This program analyzes text files (like books) and provides statistics including:
- Total word count
- Character frequency analysis (sorted by most common first)

Usage: python3 main.py <path_to_book>
Example: python3 main.py books/frankenstein.txt
"""

# Import the sys module to access command-line arguments
import sys

# Import our custom functions from the stats module
# These functions handle the statistical analysis of the text
from stats import (
    get_num_words,           # Function to count words in text
    chars_dict_to_sorted_list,  # Function to sort character frequency data
    get_chars_dict,          # Function to count character frequencies
)


def main():
    """
    Main function that orchestrates the entire program flow.
    
    This function:
    1. Validates command-line arguments
    2. Reads the book file
    3. Performs statistical analysis
    4. Displays results in a formatted report
    """
    
    # Check if the user provided exactly one argument (the book file path)
    # sys.argv is a list: [script_name, argument1, argument2, ...]
    # We need at least 2 items: the script name and the book path
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)  # Exit with error code 1 to indicate failure
    
    # Get the book file path from the first command-line argument
    # sys.argv[0] is the script name, sys.argv[1] is our book path
    book_path = sys.argv[1]

    # Step 1: Read the entire book file into a string
    text = get_book_text(book_path)
    
    # Step 2: Count the total number of words in the text
    num_words = get_num_words(text)
    
    # Step 3: Create a dictionary counting how many times each character appears
    chars_dict = get_chars_dict(text)
    
    # Step 4: Convert the character dictionary to a sorted list (most frequent first)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    
    # Step 5: Display all the results in a nicely formatted report
    print_report(book_path, num_words, chars_sorted_list)


def get_book_text(path):
    """
    Reads a text file and returns its entire contents as a string.
    
    Args:
        path (str): The file path to the book/text file
        
    Returns:
        str: The complete text content of the file
        
    Note:
        Uses a 'with' statement to automatically close the file when done.
        This is Python best practice for file handling.
    """
    with open(path) as f:
        return f.read()  # Read the entire file content into memory


def print_report(book_path, num_words, chars_sorted_list):
    """
    Displays a formatted report of the text analysis results.
    
    Args:
        book_path (str): Path to the analyzed book file
        num_words (int): Total number of words found
        chars_sorted_list (list): List of dictionaries containing character counts,
                                 sorted by frequency (highest first)
    
    The report includes:
    - Header with the file being analyzed
    - Total word count
    - Character frequency analysis (alphabetic characters only)
    """
    
    # Print a nice header for the report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    
    # Display word count section
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    
    # Display character frequency section
    print("--------- Character Count -------")
    
    # Loop through each character and its count
    # chars_sorted_list contains dictionaries like: {"char": "e", "num": 12345}
    for item in chars_sorted_list:
        # Only display alphabetic characters (skip numbers, punctuation, etc.)
        if not item["char"].isalpha():
            continue  # Skip this iteration and go to the next character
        
        # Print the character and how many times it appeared
        print(f"{item['char']}: {item['num']}")

    # Print closing footer
    print("============= END ===============")


# This is a Python idiom that ensures main() only runs when this script
# is executed directly (not when imported as a module)
if __name__ == "__main__":
    main()
