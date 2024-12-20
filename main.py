def main():
    path_to_file = "books/frankenstein.txt"
    try:
        with open(path_to_file, 'r') as f:
            file_contents = f.read()
        print(file_contents)
    except FileNotFoundError:
        print(f"Error: The file {path_to_file} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
