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
    Estimates reading time range based on reading speed variability and content complexity.
    
    Args:
        text (str): The text to analyze
        
    Returns:
        str: Formatted reading time range (e.g., "2h 30m - 4h 15m")
    """
    word_count = get_num_words(text)
    
    # Reading speed ranges for different scenarios
    if detect_technical_content(text):
        # Technical content: requires careful reading
        fast_speed = 250    # Quick scan for familiar concepts  
        slow_speed = 150    # Careful study with note-taking
    else:
        # General content: faster reading possible
        fast_speed = 350    # Executive skimming
        slow_speed = 200    # Thorough reading
    
    # Calculate time range
    fast_minutes = word_count / fast_speed
    slow_minutes = word_count / slow_speed
    
    # Helper function for time formatting
    def format_time(minutes):
        hours = int(minutes // 60)
        mins = int(minutes % 60)
        if hours > 0:
            return f"{hours}h {mins}m"
        else:
            return f"{mins}m"
    
    fast_time = format_time(fast_minutes)
    slow_time = format_time(slow_minutes)
    
    # Provide context-aware range
    if abs(fast_minutes - slow_minutes) < 30:  # Less than 30 minute difference
        avg_minutes = (fast_minutes + slow_minutes) / 2
        return f"~{format_time(avg_minutes)}"
    else:
        return f"{fast_time} - {slow_time}"


def detect_technical_content(text):
    """
    Enhanced technical content detection using weighted scoring and context analysis.
    
    Args:
        text (str): Text to analyze for technical indicators
        
    Returns:
        bool: True if technical content detected, False otherwise
    """
    # ENHANCED CONCEPT: Weighted technical indicators
    technical_indicators = {
        # High-weight: Very technical terms
        'algorithm': 3, 'architecture': 3, 'scalability': 3, 'optimization': 3,
        'implementation': 3, 'performance': 3, 'security': 3, 'protocol': 3,
        
        # Medium-weight: Programming and system terms  
        'api': 2, 'framework': 2, 'library': 2, 'database': 2, 'server': 2,
        'function': 2, 'method': 2, 'class': 2, 'object': 2, 'variable': 2,
        'coding': 2, 'programming': 2, 'development': 2, 'software': 2,
        
        # Lower-weight: Common tech terms
        'system': 1, 'network': 1, 'service': 1, 'platform': 1, 'application': 1
    }
    
    # Programming languages (high weight)
    programming_languages = [
        'python', 'java', 'javascript', 'go', 'rust', 'sql', 'html', 'css'
    ]
    
    text_lower = text.lower()
    score = 0
    
    # Score based on weighted indicators
    for term, weight in technical_indicators.items():
        if term in text_lower:
            score += weight
    
    # Bonus for programming languages
    for lang in programming_languages:
        if lang in text_lower:
            score += 3
    
    return score >= 10  # Enhanced threshold


def extract_key_concepts(text):
    """
    Extracts key technical concepts with focused, high-quality filtering.
    
    Args:
        text (str): The text to analyze for key concepts
        
    Returns:
        list: List of meaningful technical concepts, cleaned and deduplicated
    """
    # Specific technical terms we want to find (curated list)
    known_technical_terms = {
        # System Design
        'load balancer', 'microservice', 'monolith', 'api gateway', 'service mesh', 
        'caching', 'sharding', 'replication', 'consistency', 'availability',
        'cap theorem', 'horizontal scaling', 'vertical scaling',
        
        # Databases
        'mongodb', 'postgresql', 'mysql', 'redis', 'elasticsearch', 'dynamodb',
        'cassandra', 'neo4j', 'rdbms', 'nosql', 'acid', 'sql',
        
        # Cloud & Infrastructure  
        'aws', 'azure', 'gcp', 'kubernetes', 'docker', 'cloudfront', 'lambda',
        'ec2', 's3', 'rds', 'vpc', 'cdn',
        
        # Programming & Frameworks
        'python', 'java', 'javascript', 'typescript', 'go', 'rust',
        'react', 'angular', 'vue', 'spring', 'django', 'flask', 'express',
        
        # Protocols & APIs
        'http', 'https', 'tcp', 'udp', 'websocket', 'grpc', 'graphql', 
        'rest', 'api', 'json', 'xml', 'oauth', 'jwt',
        
        # Architecture Patterns
        'microservices', 'event driven', 'message queue', 'pub sub',
        'circuit breaker', 'bulkhead', 'saga pattern'
    }
    
    # Terms to absolutely exclude
    exclusions = {
        'afterword', 'chapter', 'section', 'figure', 'table', 'page',
        'introduction', 'conclusion', 'summary', 'appendix', 'index',
        'users', 'user', 'data', 'system', 'service', 'web', 'store', 'drive',
        'file', 'time', 'way', 'example', 'problem', 'solution', 'method',
        'information', 'result', 'process', 'work', 'team', 'company'
    }
    
    text_lower = text.lower()
    found_concepts = []
    
    # 1. Find known technical terms (most reliable)
    for term in known_technical_terms:
        if term in text_lower:
            # Count occurrences to gauge importance
            count = text_lower.count(term)
            if count >= 3:  # Must appear at least 3 times
                # Normalize capitalization
                if term.upper() in ['API', 'HTTP', 'HTTPS', 'TCP', 'UDP', 'SQL', 'JSON', 'XML', 'JWT', 'AWS', 'GCP', 'CDN', 'VPC', 'RDS', 'EC2', 'S3']:
                    found_concepts.append((term.upper(), count))
                elif term in ['nosql', 'grpc', 'graphql']:
                    found_concepts.append((term.replace('nosql', 'NoSQL').replace('grpc', 'gRPC').replace('graphql', 'GraphQL'), count))
                else:
                    found_concepts.append((term.title(), count))
    
    # 2. Find technology/product names (CamelCase, specific patterns)
    tech_names = re.findall(r'\b(?:MongoDB|PostgreSQL|MySQL|Redis|Elasticsearch|DynamoDB|Cassandra|Neo4j|CloudFront|WebSocket|JavaScript|TypeScript|Node\.js|Next\.js|Spring Boot|React Native)\b', text)
    for name in tech_names:
        count = text.count(name)
        if count >= 2:
            found_concepts.append((name, count))
    
    # 3. Clean and deduplicate
    # Group similar terms and keep the best version
    concept_groups = {}
    for concept, count in found_concepts:
        key = concept.lower().replace(' ', '').replace('.', '').replace('-', '')
        if key not in concept_groups or count > concept_groups[key][1]:
            concept_groups[key] = (concept, count)
    
    # Sort by frequency and relevance
    final_concepts = []
    for concept, count in concept_groups.values():
        if concept.lower() not in exclusions and len(concept) >= 3:
            final_concepts.append((concept, count))
    
    # Sort by count (descending) and return top 10
    final_concepts.sort(key=lambda x: x[1], reverse=True)
    return [concept for concept, _ in final_concepts[:10]]


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
