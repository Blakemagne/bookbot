def read_file(path_to_file):
    with open(path_to_file, 'r') as f:
        # returns .txt file as a string | saved as text varaiable in main()
        return f.read()

def count_words(text):
   # text parameter from read_file(): function
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()  # Convert all characters to lowercase
    char_count = {}
    for char in text:
        if char.isalpha():  # Only count alphabetic characters
            # .get() method returns the value of the key, if it exists in the dictionary
            char_count[char] = char_count.get(char, 0) + 1 
    return char_count


# main() convention is the shiz
def main():
    path_to_file = "books/frankenstein.txt"
    # .txt returned as string into text
    text = read_file(path_to_file)
    
    # BEGIN REPORT
    print(f"--- Begin report of {path_to_file} ---\n")
    # counts words in string from text
    word_count = count_words(text)
    print(f"The book contains {word_count} words.\n")

     # Count and display the frequency of each character
    char_count = count_characters(text)

    # loop through sorted dictionary, char_count and use .items() to return key-value pairs
    for char, count in sorted(char_count.items(), key=lambda item: item[1], reverse=True):
        print(f"The '{char}' character was found {count} times.")
    print("--- End of report ---")

if __name__ == "__main__":
    main()
