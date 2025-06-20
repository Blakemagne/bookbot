# BookBot 📚

BookBot is a command-line text analysis tool that provides comprehensive statistics about books and other text files, with special focus on PDF analysis and executive insights for technical professionals. Originally started as my first [Boot.dev](https://www.boot.dev) project, it has evolved into a powerful tool for analyzing O'Reilly books and technical documentation.

## 🎯 Perfect For

- **CEOs & CTOs** - Get quick insights on technical books before assigning to teams
- **Engineering Managers** - Assess learning materials and estimate time commitments  
- **Software Engineers** - Quickly evaluate technical books and identify key concepts
- **Students** - Understand book complexity and plan study sessions
- **Anyone** - Analyze any text file or PDF for reading insights

## Features

### Core Analysis
- **Word Count**: Counts the total number of words in any text file
- **Character Frequency Analysis**: Analyzes how often each letter appears
- **Reading Time Ranges**: Provides realistic time estimates with ranges
- **Sorted Results**: Characters are displayed from most frequent to least frequent

### Executive Insights
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

### Real-World Examples

```bash
# Quick executive analysis of a technical book
pdf-get --analyze "system design"
# Output: 46,006 words, 3h 4m - 5h 6m reading time
# Key concepts: HTTP, API, Load Balancer, Consistency, CDN

# Analyze your O'Reilly collection
pdf-get --list                          # See all available PDFs
pdf-get --analyze "designing data"      # Finds "Designing Data-Intensive Applications"
pdf-get --copy "machine learning"       # Copy without analyzing

# Traditional file analysis
bookbot books/frankenstein.txt          # Classic literature analysis
bookbot pdfs/some-manual.pdf           # Any PDF analysis

# Batch operations
pdf-get --copy-all                      # Copy all PDFs for offline analysis
```

### Sample Output

#### Executive Analysis Report
```
==================================================
📊 EXECUTIVE BOOK ANALYSIS REPORT
==================================================
📖 File: pdfs/Alex Xu - System Design Interview.pdf
📝 Word Count: 46,006
⏱️  Reading Time: 3h 4m - 5h 6m

==================================================
🎯 EXECUTIVE SUMMARY
==================================================
• Technical content - requires focused reading time
• Recommended for technical team members and decision makers
• Concise content - can be completed in single session
• Focused on specific technology stack
• Contains practical examples - schedule hands-on practice time
• Includes best practices - extract actionable guidelines

==================================================
🔑 KEY CONCEPTS & TECHNOLOGIES
==================================================
• HTTP
• HTTPS
• API
• Consistency
• CDN
• Load Balancer
• Replication
• Message Queue
• Availability
• WebSocket

==================================================
📈 CHARACTER FREQUENCY (Top 10)
==================================================
'e': 29,962
't': 20,190
's': 17,697
'i': 17,189
'a': 16,846
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

### Architecture Overview

BookBot uses a modular design with clear separation of concerns:

- **main.py**: Entry point, file handling, PDF extraction, executive reporting
- **stats.py**: Statistical analysis, key concept extraction, executive insights  
- **pdf_transfer.py**: Windows/WSL PDF discovery and transfer utility
- **Shell Scripts**: `bookbot` and `pdf-get` provide Unix-style command experience
- **Virtual Environment**: Isolated Python dependencies for PDF processing

### Executive Analysis Pipeline

1. **File Discovery**: Robust scanning of Windows Desktop locations (including OneDrive variants)
2. **Content Extraction**: 
   - Text files: Direct reading with UTF-8 encoding
   - PDF files: `pdfplumber` library extracts text from all pages
3. **Intelligence Analysis**:
   - **Word Counting**: Accurate tokenization accounting for technical terms
   - **Reading Time**: Dynamic calculation based on content complexity
   - **Technical Detection**: Pattern matching for programming concepts
   - **Key Concepts**: Extraction of technologies, frameworks, methodologies
4. **Executive Reporting**: Professional format optimized for decision-makers

### Advanced Features Explained

#### PDF Text Extraction
- Uses `pdfplumber` for reliable text extraction from technical PDFs
- Handles complex layouts common in O'Reilly books
- Processes all pages and concatenates content
- Graceful error handling for corrupted or protected PDFs

#### Smart Content Analysis
- **Technical Content Detection**: Weighted scoring system for accurate classification
- **Concept Extraction**: Curated technical term matching with intelligent filtering
- **Reading Time Ranges**: Realistic time estimates accounting for reading speed variability
- **Executive Insights**: Generates actionable recommendations based on content analysis

#### Windows/WSL Integration
- **Desktop Discovery**: Scans multiple OneDrive configurations automatically
- **Path Resolution**: Handles various Windows user directory structures
- **Duplicate Detection**: Prevents copying same file from multiple locations
- **Filename Safety**: Proper escaping for files with spaces and special characters

### Key Programming Concepts Demonstrated

#### Beginner Concepts
- **Module Imports**: Both built-in (`os`, `sys`) and external (`pdfplumber`) libraries
- **Command-Line Arguments**: Using `argparse` for professional CLI interfaces
- **File I/O**: Reading text files and PDFs with proper resource management
- **Data Structures**: Dictionaries for counting, lists for sorting, sets for deduplication
- **String Processing**: Text splitting, character iteration, case conversion
- **Function Design**: Pure functions with clear inputs/outputs and docstrings

#### Intermediate Concepts  
- **Regular Expressions**: Pattern matching for technical term extraction
- **Error Handling**: Try/catch blocks with graceful degradation
- **Path Manipulation**: Cross-platform file system operations
- **Virtual Environments**: Dependency isolation and management
- **Shell Scripting**: Bash wrappers for Python applications

#### Advanced Concepts
- **Cross-Platform Integration**: WSL/Windows filesystem bridge
- **PDF Processing**: Binary file format parsing and text extraction  
- **Pattern Recognition**: Heuristic-based content classification
- **Executive Reporting**: Data presentation optimized for business users
- **Symlink Management**: Unix-style command installation

## Adding Content to Analyze

### For PDFs (Recommended)
1. **O'Reilly Books**: Place PDFs in your Windows Desktop or Desktop/Library folder
2. **Use pdf-get**: The tool automatically discovers and copies them
3. **Analyze**: `pdf-get --analyze "book name"` handles everything automatically

### For Text Files (Classic Method)
1. **Project Gutenberg**: Download free classics in `.txt` format
2. **Save to books/**: Place files in the `books/` directory  
3. **Analyze**: `bookbot books/filename.txt`

### Popular Technical Books to Try
- **System Design**: Alex Xu's System Design Interview
- **Data Engineering**: Designing Data-Intensive Applications
- **AI/ML**: Any O'Reilly AI or Machine Learning book
- **Programming**: Language-specific O'Reilly guides (Python, JavaScript, etc.)
- **DevOps**: Docker, Kubernetes, AWS books

### Classic Literature (for comparison)
- **Pride and Prejudice**: `https://www.gutenberg.org/files/1342/1342-0.txt`
- **Alice in Wonderland**: `https://www.gutenberg.org/files/11/11-0.txt` 
- **Moby Dick**: `https://www.gutenberg.org/files/2701/2701-0.txt`

## Technical Details

### Dependencies
- **Core:** Python 3.8+ (no external packages for basic text analysis)
- **PDF Support:** pdfplumber, pillow, nltk (auto-installed via `./install.sh`)
- **Environment:** Virtual environment isolation for clean dependency management

### Performance
- **Memory usage:** Loads entire file into memory (suitable for books up to ~100MB)
- **Analysis speed:** Optimized with curated technical term matching
- **PDF processing:** Efficient page-by-page text extraction
- **Cross-platform:** Seamless Windows/WSL file system integration

### File Format Support
- **Text files:** .txt with UTF-8 encoding (handles international characters)
- **PDF files:** Technical books, O'Reilly publications, academic papers
- **Robust parsing:** Handles complex PDF layouts and formatting

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
