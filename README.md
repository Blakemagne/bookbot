Bookbot: A Static Text Reader

- function: main()

    - variable: path_to_file
    holds path or link to the .txt being read

    - function: read_file 
    return string 

    - variable: text 
    holds string that readfile returns

    - function: count_words 
    split string into list of words
    return length of list

    - function: count_characters 
    turn text into lowercase
    create empty dictionary for each lower case letter
    loop through lower case string 
        if new alphabet character
            add new letter to dictionary 
        elif in dictionary 
            increment value + 1

    print f'strings for word_count
    print f' string for character_count
        
