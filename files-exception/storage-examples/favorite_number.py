import json

filename ='favorite_number.json'

def storage_number():
    number = input("Your favorite number is: ")
    with open(filename,'w') as file_number:
        json.dump(number,file_number)
    return number

def read_number():
    try:
        with open(filename) as file_number:
            number = json.load(file_number)
    except FileNotFoundError:
        return None
    else:
        return number

def show_number():  
    if read_number():
        print("Your number is mmmMM... Oh! : " + read_number())
    else:
        storage_number()
        print("I remember your favorite number..." + str(read_number()))

show_number()