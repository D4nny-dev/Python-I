#Counting to Twenty
for count in range(1,21):
    print(count)


# Min,Max,Sum
numbers = list(range(1,21))
print(numbers)
print("Min: " + str(min(numbers)))
print("Max: " + str(max(numbers)))
print("Sum: " + str(sum(numbers)))

#Odd Numbers
odd = list(range(1,21,2))
print(odd)

#Threes
thress = list(range(3,31,3))
print(thress)

#Cubes
cubes = []
for value in range(1,11):
    cubes.append(value**3)

print(cubes)

#cubes comprehesion
cubes = [value**3 for value in range(1,11)]
print(cubes)


