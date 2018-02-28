from random import randint

class Die():

    def __init__(self):
        self.sides = 6
    
    def roll_die(self):
        self.sides = randint(1,6)
        print(self.sides)

die = Die()
die.roll_die()


        