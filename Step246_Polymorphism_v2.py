class fandom:
    #Constructor
    def __init__(self, name, email, sport):
        self.name = name
        self.email = email
        self.sport = sport

    #Define the parent Class' method:
    def message(self):
        msg = "WE LIKE SPORTS AND WE DON'T CARE WHO KNOWS!!"
        print(msg)


#//Two child Classes with two attributes each//
#Create a child Class with 2 attributes:
class pros(fandom):
    league = "NFL"
    city = "Seattle"

    #Child class' function for polymorphism to parent class:
    def message(self):
        if pros.league == "NFL":
            msg = "Omaha!"
            print(msg)
        elif pros.league == "NBA":
            msg = "Alley-oop-oop, Oop-oop..."
            print(msg)
        elif pros.league == "MLB":
            msg = "Swing, Batter!"
            print(msg)
        elif pros.league == "NHL":
            msg = "I went to a fight and a hockey game broke out."
            print(msg)
        else:
            print("We shant take you out to the ballgames.")


#Create a child Class with 2 attributes:
class faves(fandom):
    team = "Seahawks"
    player = "Bobby Wagner"

    #Child class' function for polymorphism to parent class:
    def message(self):
        msg = "Root, Root-root for your team!"
        print(msg)

