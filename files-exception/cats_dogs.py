filename_cats = 'files-exception/cat.txt'
filename_dogs = 'files-exception/dogs.txt'

try:
    with open(filename_cats) as cats:
        for cat in cats:
            print(cat.strip())
    
    print("\n")
    with open(filename_dogs) as dogs:
        for cat in dogs:
            print(cat.strip())

except FileNotFoundError as f:
    print("File " + str(f.filename)+" no exit, or is in another rute")
