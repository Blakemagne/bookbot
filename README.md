# BookBot 📚

BookBot is a command-line text analysis tool that provides comprehensive statistics about books and other text files. This is my first [Boot.dev](https://www.boot.dev) project!

## Features

### Core Analysis
- **Word Count**: Counts the total number of words in any text file
- **Character Frequency Analysis**: Analyzes how often each letter appears
- **Reading Time Estimates**: Calculates time needed based on content type
- **Sorted Results**: Characters are displayed from most frequent to least frequent

### Executive Insights (New!)
- **PDF Support**: Analyze O'Reilly books and technical PDFs
- **Key Concepts Extraction**: Identifies technical terms and technologies
- **Executive Summary**: Provides actionable insights for busy professionals
- **Technical Content Detection**: Auto-detects programming/technical content
- **Professional Reporting**: Clean, executive-friendly output format

### Workflow Tools
- **Windows/WSL Integration**: Easy PDF transfer from Windows Desktop
- **Command Line Interface**: Easy to use with any text file or PDF
- **Modular Design**: Clean separation between analysis and reporting

## Installation

1. Clone this repository:
   ```bash
   git clone <your-repo-url>
   cd bookbot
   ```

2. Install dependencies for PDF support:
   ```bash
   pip install -r requirements.txt
   ```

3. Install shell commands (optional but recommended):
   ```bash
   ./install.sh
   source ~/.bashrc
   ```

4. For basic text analysis only, no additional dependencies required!

## Usage

### Shell Commands (After installing with `./install.sh`)

```bash
# Analyze any file
bookbot <file>

# PDF management
pdf-get --list                    # List PDFs on Windows Desktop
pdf-get --analyze "python"        # Copy and analyze PDF
pdf-get --copy "docker"           # Copy PDF only
pdf-get --copy-all                # Copy all PDFs
```

### Direct Python Usage

```bash
# Text files
python3 main.py <path_to_text_file>

# PDF files  
python3 main.py <path_to_pdf_file>

# PDF transfer utility
python3 pdf_transfer.py --list
python3 pdf_transfer.py --analyze "learning python"
```

### Examples

```bash
# Shell commands (recommended)
bookbot books/frankenstein.txt
bookbot pdfs/learning_python.pdf
pdf-get --analyze "effective python"

# Direct Python
python3 main.py books/frankenstein.txt
python3 pdf_transfer.py --analyze "docker handbook"
```

### Sample Output

#### Executive Analysis Report
```
==================================================
📊 EXECUTIVE BOOK ANALYSIS REPORT
==================================================
📖 File: pdfs/learning_python.pdf
📝 Word Count: 125,430
⏱️  Reading Time: 10h 27m

==================================================
🎯 EXECUTIVE SUMMARY
==================================================
• Technical content - requires focused reading time
• Recommended for technical team members and decision makers
• Comprehensive resource - plan multiple reading sessions
• Contains practical examples - schedule hands-on practice time

==================================================
🔑 KEY CONCEPTS & TECHNOLOGIES
==================================================
• Python
• Django
• Flask
• API
• JSON
• Database
• Framework
• Object
• Function
• Algorithm

==================================================
📈 CHARACTER FREQUENCY (Top 10)
==================================================
'e': 44,538
't': 29,493
'a': 25,894
...
==================================================
```

## Project Structure

```
bookbot/
├── main.py              # Main program entry point and user interface
├── stats.py             # Statistical analysis and executive insights
├── pdf_transfer.py      # Windows Desktop to WSL PDF transfer utility
├── requirements.txt     # Python dependencies for PDF support
├── books/               # Directory for text files (git-ignored)
│   ├── frankenstein.txt
│   └── [other books you download]
├── pdfs/                # Directory for PDF files (git-ignored)
│   └── [PDF files copied from Windows Desktop]
├── .gitignore           # Comprehensive exclusions for development
└── README.md            # This file
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
