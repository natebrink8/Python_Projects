class fandom:
    #define the Class' attributes
    name = "No Name Provided"
    email = ""
    sport = ""
    

    #Define the Class' methods
    def profile(self):
        entry_email = input("Enter your email: ")
        if (entry_email == self.email):
            print("Welcome back, {}".format(self.name))
        else:
            print("You aren't in the sportsball community yet!")



#Outside of the Class, create an instance of the 'fandom' Class:
new_fan = fandom()
#Call the 'profile' method using the new Object:
new_fan.profile()



#Create a new fan in the 'fandom' Class created above:
def __init__(self, name, email, sport):
    self.name = name
    self.email = email
    self.sport = sport



#Create new child Classes to the parent Class created above:
class pros(fandom):
    league = "NFL"
    city = "Seattle"

class faves(fandom):
    team = "Seahawks"
    player = "Bobby Wagner"
