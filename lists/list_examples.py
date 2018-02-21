pizzas = ["Neapolitan","Chicago","Sicilian","California","Tomato Pie","Bbq chicken"]

#Slices
for pizza in pizzas[:3]:
    print(pizza)

print()

for pizza in pizzas[1:4]:
    print(pizza)

print()

for pizza in pizzas[3:]:
    print(pizza)

#My pizza, Your pizzas

friends_pizzas = pizzas[:]
pizzas.append("Crust")
friends_pizzas.append("Vegan")

print(pizzas)
print(friends_pizzas)

print()

for pizza in pizzas:
    print(pizza)

print()

for pizza in friends_pizzas:
    print(pizza)
