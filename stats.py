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
    Extracts key technical concepts and important terms from text using pattern matching.
    
    LEARNING NOTE: This function demonstrates advanced concepts:
    1. Regular expressions (regex) for pattern matching
    2. Set data structures for automatic deduplication  
    3. Counter objects for frequency analysis
    4. List comprehensions with filtering conditions
    5. String manipulation and cleaning
    6. Multiple analysis strategies combined
    
    This function is like having an expert skim through a technical book and
    highlight the most important terms and technologies mentioned. It uses
    multiple strategies to find different types of technical concepts.
    
    Args:
        text (str): The text to analyze for key concepts
        
    Returns:
        list: List of key concepts found in the text, sorted and limited to top 15
    """
    # BEGINNER CONCEPT: Regular expression patterns
    # Regular expressions (regex) are patterns that match text
    # These patterns are designed to find common technical terms
    tech_patterns = [
        # This pattern finds CamelCase terms like "JavaScript", "MongoDB", "GraphQL"
        r'\b[A-Z][a-z]+(?:[A-Z][a-z]+)*\b',  
        
        # This pattern finds specific technical acronyms and tools
        r'\b(?:API|REST|HTTP|JSON|XML|SQL|NoSQL|AWS|Docker|Kubernetes)\b',
        
        # This pattern finds programming languages and frameworks
        r'\b(?:Python|JavaScript|Java|React|Node\.js|Django|Flask)\b',
        
        # This pattern finds multi-word technical concepts
        r'\b(?:machine learning|artificial intelligence|data science)\b',
        
        # This pattern finds methodology and process terms
        r'\b(?:microservices|DevOps|CI/CD|agile|scrum)\b',
        
        # This pattern finds general technical terms
        r'\b(?:database|framework|library|algorithm|architecture)\b'
    ]
    
    # BEGINNER CONCEPT: Set data structure
    # Sets automatically prevent duplicates - if we find "Python" multiple times,
    # it only appears once in our final list
    concepts = set()
    
    # BEGINNER CONCEPT: Iterating over patterns and pattern matching
    for pattern in tech_patterns:
        # BEGINNER CONCEPT: Regular expression matching
        # re.findall() finds all text that matches the pattern
        # re.IGNORECASE makes it find "python", "Python", "PYTHON", etc.
        matches = re.findall(pattern, text, re.IGNORECASE)
        
        # BEGINNER CONCEPT: Set operations
        # .update() adds all the matches to our set (duplicates automatically removed)
        concepts.update(matches)
    
    # BEGINNER CONCEPT: Finding capitalized terms (likely proper nouns)
    # This pattern finds words that start with capital letters
    # These are often company names, product names, or technologies
    capitalized = re.findall(r'\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b', text)
    
    # BEGINNER CONCEPT: List comprehension with multiple conditions
    # This filters the capitalized terms to keep only likely technical terms
    tech_terms = [
        term for term in capitalized 
        if 2 <= len(term) <= 20                    # Reasonable length
        and not term.lower() in ['The', 'This', 'That', 'Chapter']  # Skip common words
    ]
    
    # BEGINNER CONCEPT: Frequency analysis with Counter
    # Counter counts how often each term appears
    term_counts = Counter(tech_terms)
    
    # BEGINNER CONCEPT: Filtering by frequency
    # .most_common(20) gets the 20 most frequent terms
    # We only keep terms that appear at least twice (count >= 2)
    frequent_terms = [
        term for term, count in term_counts.most_common(20) 
        if count >= 2
    ]
    
    # Add the frequent terms to our concepts set
    concepts.update(frequent_terms)
    
    # BEGINNER CONCEPT: Converting sets to sorted lists with slicing
    # Convert set to list, sort alphabetically, and take only top 15
    return sorted(list(concepts))[:15]  # Return top 15


def generate_executive_summary(text):
    """
    Generates executive summary with actionable insights for business decision-makers.
    
    LEARNING NOTE: This function demonstrates:
    1. Complex conditional logic and decision trees
    2. String searching and pattern detection
    3. Function composition (using results from other functions)
    4. Business logic implementation
    5. List management and limiting output
    6. Heuristic-based analysis (rule-based intelligence)
    
    This function is designed to answer the key questions executives ask:
    - Should I assign this to my team?
    - How much time will it take?
    - What will they learn?
    - Is it practical or theoretical?
    
    Args:
        text (str): The text to analyze for executive insights
        
    Returns:
        list: List of actionable executive insights (max 6)
    """
    # BEGINNER CONCEPT: Building a list incrementally
    # We'll add insights one by one based on our analysis
    insights = []
    
    # BEGINNER CONCEPT: Gathering data for decision making
    # Call our other functions to get the information we need
    word_count = get_num_words(text)
    is_technical = detect_technical_content(text)
    concepts = extract_key_concepts(text)
    
    # BEGINNER CONCEPT: Conditional logic for classification
    # Based on technical content detection, give appropriate advice
    if is_technical:
        insights.append("Technical content - requires focused reading time")
        insights.append("Recommended for technical team members and decision makers")
    else:
        insights.append("General content - suitable for broader audience")
    
    # BEGINNER CONCEPT: Numerical thresholds for categorization
    # Different word counts require different time management strategies
    if word_count > 100000:
        # Very long books (like comprehensive programming guides)
        insights.append("Comprehensive resource - plan multiple reading sessions")
        insights.append("Consider creating team reading schedule")
    elif word_count > 50000:
        # Medium-length technical books (most O'Reilly books fall here)
        insights.append("Substantial content - allocate dedicated time blocks")
    else:
        # Short guides, articles, or focused topics
        insights.append("Concise content - can be completed in single session")
    
    # BEGINNER CONCEPT: Using list length for analysis
    # More concepts = broader scope, fewer concepts = focused depth
    if len(concepts) > 10:
        insights.append("Covers multiple technologies - good for technology overview")
        insights.append("Identify relevant sections for your specific use case")
    elif len(concepts) > 5:
        insights.append("Focused on specific technology stack")
    
    # BEGINNER CONCEPT: String searching with any() function
    # any() returns True if ANY of the conditions are true
    # This checks if the text contains practical, hands-on content
    if any(term in text.lower() for term in ['example', 'tutorial', 'how to', 'step by step']):
        insights.append("Contains practical examples - schedule hands-on practice time")
    
    # BEGINNER CONCEPT: Detecting best practices and architectural content
    # This helps executives know if the book will help with strategic planning
    if any(term in text.lower() for term in ['best practice', 'pattern', 'architecture']):
        insights.append("Includes best practices - extract actionable guidelines")
    
    # BEGINNER CONCEPT: List slicing to limit output
    # [:6] takes only the first 6 insights to avoid overwhelming the reader
    # This keeps the summary concise and actionable
    return insights[:6]  # Return top 6 insights
