"""
Statistics Module for BookBot

This module contains functions for analyzing text and generating statistics.
It handles word counting, character frequency analysis, and data sorting.

Functions:
- get_num_words: Counts total words in a text
- get_chars_dict: Creates character frequency dictionary  
- chars_dict_to_sorted_list: Converts and sorts character data
- sort_on: Helper function for sorting by frequency
"""


def get_num_words(text):
    """
    Counts the total number of words in the given text.
    
    Args:
        text (str): The text to analyze
        
    Returns:
        int: The total number of words found
        
    How it works:
    1. Uses the split() method to break text into a list of words
    2. split() automatically handles multiple spaces, tabs, and newlines
    3. Returns the length of the resulting list
    
    Example:
        >>> get_num_words("Hello world! How are you?")
        5
    """
    # Split the text into words using whitespace as delimiters
    # This creates a list where each element is a word
    words = text.split()
    
    # Return the count of words (length of the list)
    return len(words)


def get_chars_dict(text):
    """
    Creates a dictionary that counts how many times each character appears in the text.
    
    Args:
        text (str): The text to analyze
        
    Returns:
        dict: A dictionary where keys are characters (lowercase) and values are counts
        
    How it works:
    1. Iterates through every character in the text
    2. Converts each character to lowercase for consistent counting
    3. Increments the count for each character in the dictionary
    
    Example:
        >>> get_chars_dict("Hello")
        {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    """
    # Initialize an empty dictionary to store character counts
    chars = {}
    
    # Loop through every single character in the text
    for c in text:
        # Convert character to lowercase so 'A' and 'a' are counted together
        lowered = c.lower()
        
        # Check if we've seen this character before
        if lowered in chars:
            # If yes, increment its count by 1
            chars[lowered] += 1
        else:
            # If no, add it to the dictionary with a count of 1
            chars[lowered] = 1
    
    # Return the completed dictionary
    return chars


def sort_on(d):
    """
    Helper function used for sorting character frequency data.
    
    Args:
        d (dict): A dictionary with "char" and "num" keys
        
    Returns:
        int: The frequency count (used as the sort key)
        
    Note:
        This function is used as a 'key' function for Python's sort() method.
        It tells sort() to sort based on the "num" value in each dictionary.
    """
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    """
    Converts a character frequency dictionary to a sorted list of dictionaries.
    
    Args:
        num_chars_dict (dict): Dictionary with characters as keys and counts as values
        
    Returns:
        list: List of dictionaries, each containing "char" and "num" keys,
              sorted by frequency (highest count first)
              
    How it works:
    1. Creates an empty list to store the results
    2. Converts each dictionary entry to a new format: {"char": "a", "num": 123}
    3. Sorts the list by frequency count (highest first)
    
    Example:
        Input:  {'a': 5, 'b': 2, 'c': 8}
        Output: [{"char": "c", "num": 8}, {"char": "a", "num": 5}, {"char": "b", "num": 2}]
    """
    # Create an empty list to hold our converted data
    sorted_list = []
    
    # Loop through each character and its count in the dictionary
    for ch in num_chars_dict:
        # Create a new dictionary with a standardized format
        # This makes it easier to work with in other parts of the program
        char_data = {"char": ch, "num": num_chars_dict[ch]}
        
        # Add this dictionary to our list
        sorted_list.append(char_data)
    
    # Sort the list by the "num" value in descending order (highest first)
    # reverse=True means highest numbers come first
    # key=sort_on tells Python to use our sort_on function to determine sort order
    sorted_list.sort(reverse=True, key=sort_on)
    
    # Return the sorted list
    return sorted_list
