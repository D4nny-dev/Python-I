guest = ["Julio","Edgar","Charles"]
print("Invited: " + guest[0] + "," + guest[1] + "," + guest[2])
print("Number of guest : " + str(len(guest)))

#remove and add new guest
noAssist = guest.pop(1)
guest.insert(1,"Nor")
print("Guest " + noAssist + " cant`t make the diNner")
print("¡New guest " + guest[1] + " is invited! ")

print("Invited: " + guest[0] + "," + guest[1] + "," + guest[2])

#add more guest
guest.insert(0,"Luis")
guest.insert(2,"Marcos")
guest.append("Lucas")

print("Invited: " + guest[0] + "," + guest[1] + "," 
    + guest[2]+ "," + guest[3]+ "," + guest[4]+ "," + guest[5])

#cancel invitation

print("Sorry i can`t invite to dinner "+ guest.pop(0))
print("Sorry i can`t invite to dinner "+ guest.pop(0))
print("Sorry i can`t invite to dinner "+ guest.pop(0))
print("Sorry i can`t invite to dinner "+ guest.pop(0))

print("Invited: " + guest[0] + "," + guest[1] )

del guest[0]
del guest[0]

print("list guest: " + str(guest))

