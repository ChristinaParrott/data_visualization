from random import randint

class Die:
    #Class representing a single die

    def __init__(self, num_sides=6):
        #Assume 6-sided unless otherwise noted
        self.num_sides = num_sides

    def roll(self):
        #Return a random value between 1 and the number of sides
        return randint(1, self.num_sides)