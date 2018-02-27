def describe_city(city, country):
    msg="I was born in " + city + "," +country
    return msg

print(describe_city("Madrid","España"))

# Make a album ..
def make_album(title,author):
    album = {'title': title,'author':author}
    return album

while True:
    title = input("Set Title: ")
    if title == 'q':
        break
    else:
        author = input("Set author: ")
        print( make_album(title,author))
    


