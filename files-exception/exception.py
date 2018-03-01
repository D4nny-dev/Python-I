cont=0
numbers=[]
while True:
    if cont<2:
        try:
            numbers.append(int(input("Give me a number :"))) 
            cont+=1
        except ValueError:
          print("Please introduce a number..")  
    else:
        for n in numbers:
            print(n, end="\t")
        break


       
        

