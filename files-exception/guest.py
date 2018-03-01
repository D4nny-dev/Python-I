
while True:
    name = input("Your name is : ")
    break

#append to guest_book
with open('guest_book.txt','a') as file_object:
    file_object.write(name+"\n")

#write to name
with open('name.txt','w') as file_object:
    file_object.write(name)

#read from name
with open('name.txt') as file_object:
    print(file_object.read())

#read from guest_book
with open('guest_book.txt') as file_object:
    print(file_object.read())
    
with open('guest_book.txt') as file_object:
    for line in file_object:
        print("Hello "+ line.strip()+"!")

