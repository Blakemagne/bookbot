def read_file(path_to_file):
    with open(path_to_file, 'r') as f:
        # returns .txt file as a string | saved as text varaiable in main()
        return f.read()

def count_words(text):
   # text parameter from read_file(): function
    words = text.split()
    return len(words)

# main() convention is the shiz
def main():
    path_to_file = "books/frankenstein.txt"
    # .txt returned as string into text
    text = read_file(path_to_file)
    # counts words in string from text
    word_count = count_words(text)
    print(f"The book contains {word_count} words.")

if __name__ == "__main__":
    main()
