#Person
person = {
    'name':'Martin',
    'lastName':'Lopez',
    'city': 'Chumasera'
}

print("Name: " + person['name']+" \nLast name :" + 
    person['lastName'] + "\nCity: " + person['city'])


#Favorite number
numbers = {'Carlos':5 ,'Manuel': 7 ,'Maria':9}

for key,value in numbers.items():
    print("Number favorite "+ key +" : "+ str(value))

for value in numbers.keys():
    print(numbers[value])

if 'Jose' not in numbers.keys():
    print("your number is ? ... ")

#Glossary
worlds = {
    "argument":"A value passed to a function (or method) when calling the function",
    "class":"A template for creating user-defined objects."
}

print(worlds)

#Order dicionary
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward':'ruby',
    'phil':'python'
}

print("\nNames")
for name in sorted(favorite_languages.keys()):
    print(name.title())

print("\nLanguages")
for language in sorted(favorite_languages.values()):
    print(language.title())

print("\nLanguages no repeat")
for language in set(favorite_languages.values()):
    print(language.title())

#Nesting 

aliens = []

print(aliens)
for alien in range(10):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[:2]:
    print(alien['speed'])


for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = '10'
        alien['speed'] = 'medium'


#languages
languages = {
    'jen': ['english','german'],
    'sarah': ['spanish'],
    'edward':['spanish'],
    'phil':['ruso','english']
}

for name,languages in languages.items():
    print("\nMy name is " + name.title() + " and speak in : ")
    for language in languages:
       print("\t"+language.title())

       