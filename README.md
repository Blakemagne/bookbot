# BookBot 📚

BookBot is a command-line text analysis tool that provides comprehensive statistics about books and other text files. This is my first [Boot.dev](https://www.boot.dev) project!

## Features

- **Word Count**: Counts the total number of words in any text file
- **Character Frequency Analysis**: Analyzes how often each letter appears
- **Sorted Results**: Characters are displayed from most frequent to least frequent
- **Command Line Interface**: Easy to use with any text file as input
- **Modular Design**: Clean separation between main program logic and statistical functions

## Installation

1. Clone this repository:
   ```bash
   git clone <your-repo-url>
   cd bookbot
   ```

2. Ensure you have Python 3 installed on your system

3. No additional dependencies required! BookBot uses only Python standard library.

## Usage

### Basic Usage
```bash
python3 main.py <path_to_text_file>
```

### Examples
```bash
# Analyze Frankenstein (included)
python3 main.py books/frankenstein.txt

# Analyze Pride and Prejudice (if downloaded)
python3 main.py books/prideandprejudice.txt

# Analyze any text file
python3 main.py /path/to/your/textfile.txt
```

### Sample Output
```
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------
e: 44538
t: 29493
a: 25894
o: 24494
...
============= END ===============
```

## Project Structure

```
bookbot/
├── main.py           # Main program entry point and user interface
├── stats.py          # Statistical analysis functions
├── books/            # Directory for text files (git-ignored)
│   ├── frankenstein.txt
│   └── [other books you download]
├── .gitignore        # Excludes books directory from version control
└── README.md         # This file
```

## How It Works

### Architecture
BookBot follows a modular design with clear separation of concerns:

- **main.py**: Handles user interaction, file I/O, and program flow
- **stats.py**: Contains all statistical analysis logic

### Algorithm Overview

1. **Input Validation**: Checks command-line arguments
2. **File Reading**: Loads the entire text file into memory
3. **Word Counting**: Splits text on whitespace and counts resulting words
4. **Character Analysis**: 
   - Iterates through every character
   - Converts to lowercase for case-insensitive counting
   - Builds frequency dictionary
5. **Data Processing**: Converts dictionary to sorted list by frequency
6. **Output**: Displays formatted results

### Key Programming Concepts Demonstrated

- **Module Imports**: Both built-in (`sys`) and custom (`stats`) modules
- **Command-Line Arguments**: Using `sys.argv` for user input
- **File I/O**: Reading text files with proper resource management
- **Data Structures**: Dictionaries for counting, lists for sorting
- **String Processing**: Text splitting, character iteration, case conversion
- **Function Design**: Pure functions with clear inputs/outputs
- **Error Handling**: Input validation and graceful exit codes

## Adding New Books

1. Visit [Project Gutenberg](https://www.gutenberg.org/)
2. Find a book in plain text format
3. Download the `.txt` file to the `books/` directory
4. Run BookBot with your new file

Popular choices:
- Pride and Prejudice: `https://www.gutenberg.org/files/1342/1342-0.txt`
- Alice in Wonderland: `https://www.gutenberg.org/files/11/11-0.txt` 
- Moby Dick: `https://www.gutenberg.org/files/2701/2701-0.txt`

## Technical Details

### Dependencies
- Python 3.x (tested with Python 3.8+)
- No external packages required

### Performance
- Memory usage: Loads entire file into memory (suitable for books up to ~100MB)
- Time complexity: O(n) where n is the number of characters in the text
- Space complexity: O(k) where k is the number of unique characters

### File Format Support
- Plain text files (.txt)
- UTF-8 encoding recommended
- Handles various character sets including accented characters

## Learning Objectives

This project demonstrates fundamental programming concepts:

- **File I/O**: Reading and processing text files
- **Data Structures**: Using dictionaries and lists effectively
- **Algorithms**: Counting, sorting, and frequency analysis
- **Modular Programming**: Separating concerns across multiple files
- **Command-Line Interfaces**: Processing user arguments
- **Documentation**: Writing clear code comments and docstrings
- **Version Control**: Using Git with appropriate .gitignore patterns

## Contributing

This is a learning project, but suggestions and improvements are welcome!

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is for educational purposes. The books in the `books/` directory are from Project Gutenberg and are in the public domain.

## Acknowledgments

- [Boot.dev](https://www.boot.dev) for the excellent Python course
- [Project Gutenberg](https://www.gutenberg.org/) for providing free public domain books
- Mary Shelley for writing Frankenstein (our default test case!)

---

*Happy analyzing! 🔍📖*
