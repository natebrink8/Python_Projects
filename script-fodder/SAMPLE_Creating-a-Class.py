class User:
    #define the class' attributes
    name = "No Name Provided"
    email = ""
    password = "1234abcd"
    account = 0

    #Define the class' methods
    def login(self):
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}".format(self.name))
        else:
            print("You are not authorized for this page.")
#Outside of the Class, create an instance of the User class
new_user = User()
#Call the login method using the new object
new_user.login()


#Create a new user from the User class created above
#First, add the following dunder method to the definition of the class
#The def __init__() needs to be at the same indentation level as the
#attributes of the class so that it will be part of the class definition
def __init__(self, name, email, pwd, account):
    self.name = name
    self.email = email
    self.pwd = pwd
    self.account = account

#The following could then be created in IDLE: New_user = User("Nate Brink", "natebrink@yahoo.com", "Password1", 1234)
