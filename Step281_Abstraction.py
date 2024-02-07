# ///// IMPORT abstractmethod from the ABC module:
from abc import ABC, abstractmethod
# Create parent Class:
class Famm:
    fname = "Unknown"
    age = "Unknown"
    whodat = "Unknown"
    chore = "Unknown"

    # Create a regular parent class method to use from child object:
    def whodey(self):
        msg = "{} is the {}.".format(self.fname, self.whodat)
        return msg

    # /////CREATE an abstract parent class method to use from child object:
    def allowance(self, amount):
        print("Your monthly allowance is: ", amount)
    #this function is telling us to pass an argument without the data type
    @abstractmethod
    def  earned(self, amount):
        pass


# Create a child class:
class Chores(Famm):
    fname = "Nate"
    whodat = "Dad"
    chore = "cooking the meals"

    # Create a regular child class method to use from child object:
    def chores(self):
        msg = "{} has the chore of {}.".format(self.whodat, self.chore)
        return msg


# Create a child class that defines the implementation of the parent class' abstract method:
class Allowance(Famm):
#/////define how to implement allowance payment from the parent "allowance" class/////
    def earned(self, amount):
        print('Your earned allowance amount of {} exceeded your monthly $100 allowance'.format(amount))
# /////USE the parent class' abstract method from the child object:
obj = Allowance()
obj.allowance("$100")
obj.earned("$250")



if __name__ == "__main__":
    chore = Chores()
    print(chore.whodey())       # Child object using parent class' regular method.
    print(chore.chores())       # Child object using the child class' method.





"""
#WIP - child class ================================
class Shoes:
    def __init__(self, whoDat, brand, color):
        self.whoDat = whoDat
        self.brand = brand
        self.color = color
p1 = Shoes('April', 'Skechers', 'Grey')
p2 = Shoes('Nate', 'Nike', 'Blue')    
#WIP - abstract dealio ================================
from abc import ABC, abstractmethod
"""
