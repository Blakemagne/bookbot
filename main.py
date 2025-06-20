#!/usr/bin/env python3
"""
BookBot - A Text Analysis Tool for PDFs and Executive Analysis

This program analyzes text files and PDFs (like O'Reilly books) and provides:
- Total word count and reading time estimates
- Character frequency analysis
- Key concepts and technical terms extraction
- Executive summary with actionable insights

Usage: python3 main.py <path_to_book>
Example: python3 main.py books/frankenstein.txt
Example: python3 main.py oreilly_books/learning_python.pdf
"""

# Import the sys module to access command-line arguments
import sys
import os

# Import our custom functions from the stats module
# These functions handle the statistical analysis of the text
from stats import (
    get_num_words,           # Function to count words in text
    chars_dict_to_sorted_list,  # Function to sort character frequency data
    get_chars_dict,          # Function to count character frequencies
    extract_key_concepts,     # Function to extract technical terms
    estimate_reading_time,    # Function to calculate reading time
    generate_executive_summary, # Function to create executive insights
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
    
    # Step 2: Perform comprehensive analysis
    analysis_results = analyze_text(text)
    
    # Step 3: Display results in an executive-friendly report
    print_executive_report(book_path, analysis_results)


def get_book_text(path):
    """
    Reads a text file or PDF and returns its entire contents as a string.
    
    Args:
        path (str): The file path to the book/text file or PDF
        
    Returns:
        str: The complete text content of the file
        
    Note:
        Supports both .txt files and .pdf files.
        Uses appropriate extraction method based on file extension.
    """
    file_extension = os.path.splitext(path)[1].lower()
    
    if file_extension == '.pdf':
        return extract_pdf_text(path)
    else:
        with open(path) as f:
            return f.read()  # Read the entire file content into memory


def extract_pdf_text(pdf_path):
    """
    Extracts text content from a PDF file.
    
    Args:
        pdf_path (str): Path to the PDF file
        
    Returns:
        str: Extracted text content from all pages
    """
    try:
        import pdfplumber
        
        text = ""
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        return text
    except ImportError:
        print("Error: pdfplumber not installed. Run: pip install pdfplumber")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading PDF: {e}")
        sys.exit(1)


def analyze_text(text):
    """
    Performs comprehensive analysis of text for executive insights.
    
    Args:
        text (str): The text content to analyze
        
    Returns:
        dict: Dictionary containing all analysis results
    """
    results = {}
    
    # Basic metrics
    results['word_count'] = get_num_words(text)
    results['reading_time'] = estimate_reading_time(text)
    
    # Character analysis (for compatibility)
    chars_dict = get_chars_dict(text)
    results['char_analysis'] = chars_dict_to_sorted_list(chars_dict)
    
    # Executive insights
    results['key_concepts'] = extract_key_concepts(text)
    results['executive_summary'] = generate_executive_summary(text)
    
    return results


def print_executive_report(book_path, results):
    """
    Displays an executive-friendly analysis report.
    
    Args:
        book_path (str): Path to the analyzed book
        results (dict): Analysis results from analyze_text()
    """
    print("=" * 50)
    print("📊 EXECUTIVE BOOK ANALYSIS REPORT")
    print("=" * 50)
    print(f"📖 File: {book_path}")
    print(f"📝 Word Count: {results['word_count']:,}")
    print(f"⏱️  Reading Time: {results['reading_time']}")
    
    print("\n" + "=" * 50)
    print("🎯 EXECUTIVE SUMMARY")
    print("=" * 50)
    for insight in results['executive_summary']:
        print(f"• {insight}")
    
    print("\n" + "=" * 50)
    print("🔑 KEY CONCEPTS & TECHNOLOGIES")
    print("=" * 50)
    for concept in results['key_concepts'][:10]:  # Top 10
        print(f"• {concept}")
    
    print("\n" + "=" * 50)
    print("📈 CHARACTER FREQUENCY (Top 10)")
    print("=" * 50)
    for item in results['char_analysis'][:10]:
        if item["char"].isalpha():
            print(f"'{item['char']}': {item['num']:,}")
    
    print("=" * 50)


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
