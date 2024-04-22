'''
Katellyn Hyker
Chapter 5 Project 7
Input a text file and print the unique words in alphabetical order

'''

wordsFile = input("Please enter the name of the file: ")
with open(wordsFile) as file:
    unique_words = []
    for line in file:
        words = line.strip().split()
        for word in words:
            if not word in unique_words:
             unique_words.append(word)
    unique_words.sort()

    for word in unique_words:
        print(word)