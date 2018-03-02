def count_words(word,filename):
    """This method count words in a file"""
    try:
        with open(filename) as file:
            count=0
            for line in file:
                count +=line.count(word)
            print("The number of word '" + word + "' is: " + str(count))
    except FileNotFoundError:
        #Failing Silently example
        pass
    
filename = "files-exception/book.txt"
count_words('cat',filename)
count_words('I',filename)


