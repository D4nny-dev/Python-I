def make_sandwich (*items):
    print("Making a sandwich: ")
    for item in items:
        print("\tadding... " + item)
    print("Enjoy! :P ")

make_sandwich("chess","eggs","bacon")


def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    
    for key, value in user_info.items():
        profile[key] = value

    return profile

print("\n")    
print("Info cliente: ")
print(build_profile('jose','martn',address='C/la piedra',phone='608515431'))
