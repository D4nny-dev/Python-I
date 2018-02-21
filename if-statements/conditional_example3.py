#Hello Admin

users = ["Marcos","Luis","Ana","Carlos","Admin"]

if users:
    for user in users:
        if user == "Admin":
            print("Hello "+ user +" would you like to see a status report?")
        else:
            print("Hello "+ user + " thank you for logging in again.")
else:
    print("We need to  nd some users!")

#Checking Usernames
users = [user.lower() for user in users]
new_users = ["Paola","Marc","Ana","Carlos"]

for new_user in new_users:
    if new_user.lower() in users:
        print("Username: "+ new_user + " not available")
    else:
        print("Username: "+ new_user + " available")

#Ordinal Numbers
numbers = list(range(1,10))

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(str(number) + "th")