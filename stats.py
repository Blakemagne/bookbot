"""
Statistics Module for BookBot

This module contains functions for analyzing text and generating statistics.
It handles word counting, character frequency analysis, executive insights,
and technical concept extraction.

Functions:
- get_num_words: Counts total words in a text
- get_chars_dict: Creates character frequency dictionary  
- chars_dict_to_sorted_list: Converts and sorts character data
- sort_on: Helper function for sorting by frequency
- extract_key_concepts: Identifies technical terms and concepts
- estimate_reading_time: Calculates reading time estimates
- generate_executive_summary: Creates actionable insights
"""

import re
from collections import Counter


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


def estimate_reading_time(text):
    """
    Estimates reading time based on average reading speed.
    
    Args:
        text (str): The text to analyze
        
    Returns:
        str: Formatted reading time estimate
    """
    word_count = get_num_words(text)
    
    # Average reading speeds (words per minute)
    speeds = {
        'executive': 300,    # Fast executive reading
        'technical': 200,    # Technical material
        'average': 250       # General reading
    }
    
    # Detect if content is technical
    is_technical = detect_technical_content(text)
    speed = speeds['technical'] if is_technical else speeds['executive']
    
    minutes = word_count / speed
    hours = int(minutes // 60)
    remaining_minutes = int(minutes % 60)
    
    if hours > 0:
        return f"{hours}h {remaining_minutes}m"
    else:
        return f"{remaining_minutes}m"


def detect_technical_content(text):
    """
    Detects if content is technical based on keyword density.
    
    Args:
        text (str): Text to analyze
        
    Returns:
        bool: True if technical content detected
    """
    technical_indicators = [
        'api', 'framework', 'library', 'algorithm', 'database',
        'function', 'method', 'class', 'object', 'variable',
        'code', 'programming', 'development', 'software',
        'python', 'javascript', 'java', 'sql', 'html', 'css'
    ]
    
    text_lower = text.lower()
    matches = sum(1 for indicator in technical_indicators if indicator in text_lower)
    
    return matches >= 5  # Threshold for technical content


def extract_key_concepts(text):
    """
    Extracts key technical concepts and important terms from text.
    
    Args:
        text (str): The text to analyze
        
    Returns:
        list: List of key concepts found in the text
    """
    # Technical terms commonly found in O'Reilly books
    tech_patterns = [
        r'\b[A-Z][a-z]+(?:[A-Z][a-z]+)*\b',  # CamelCase terms
        r'\b(?:API|REST|HTTP|JSON|XML|SQL|NoSQL|AWS|Docker|Kubernetes)\b',
        r'\b(?:Python|JavaScript|Java|React|Node\.js|Django|Flask)\b',
        r'\b(?:machine learning|artificial intelligence|data science)\b',
        r'\b(?:microservices|DevOps|CI/CD|agile|scrum)\b',
        r'\b(?:database|framework|library|algorithm|architecture)\b'
    ]
    
    concepts = set()
    
    for pattern in tech_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        concepts.update(matches)
    
    # Extract capitalized terms (likely proper nouns/technologies)
    capitalized = re.findall(r'\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b', text)
    
    # Filter for likely technical terms (2-20 characters)
    tech_terms = [term for term in capitalized if 2 <= len(term) <= 20 and not term.lower() in ['The', 'This', 'That', 'Chapter']]
    
    # Get most frequent terms
    term_counts = Counter(tech_terms)
    frequent_terms = [term for term, count in term_counts.most_common(20) if count >= 2]
    
    concepts.update(frequent_terms)
    
    return sorted(list(concepts))[:15]  # Return top 15


def generate_executive_summary(text):
    """
    Generates executive summary with actionable insights.
    
    Args:
        text (str): The text to analyze
        
    Returns:
        list: List of executive insights
    """
    insights = []
    
    word_count = get_num_words(text)
    is_technical = detect_technical_content(text)
    concepts = extract_key_concepts(text)
    
    # Content type assessment
    if is_technical:
        insights.append("Technical content - requires focused reading time")
        insights.append("Recommended for technical team members and decision makers")
    else:
        insights.append("General content - suitable for broader audience")
    
    # Scope assessment
    if word_count > 100000:
        insights.append("Comprehensive resource - plan multiple reading sessions")
        insights.append("Consider creating team reading schedule")
    elif word_count > 50000:
        insights.append("Substantial content - allocate dedicated time blocks")
    else:
        insights.append("Concise content - can be completed in single session")
    
    # Technology focus
    if len(concepts) > 10:
        insights.append("Covers multiple technologies - good for technology overview")
        insights.append("Identify relevant sections for your specific use case")
    elif len(concepts) > 5:
        insights.append("Focused on specific technology stack")
    
    # Implementation recommendations
    if any(term in text.lower() for term in ['example', 'tutorial', 'how to', 'step by step']):
        insights.append("Contains practical examples - schedule hands-on practice time")
    
    if any(term in text.lower() for term in ['best practice', 'pattern', 'architecture']):
        insights.append("Includes best practices - extract actionable guidelines")
    
    return insights[:6]  # Return top 6 insights
