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
def __init__(self, name, email, password, account):
    self.name = name
    self.email = email
    self.password = password
    self.account = account

#The following could then be created in IDLE: New_user = User("Nate Brink", "natebrink@yahoo.com", "Password1", 1234)


#////////////////CLASS INHERITANCE////////////////
    #Inheritance is one of the primary concepts of object-oriented programming.
    #In some cases you may want all the attributes and methods of a class,
    #but with additional information that doesn’t necessarily belong to the
    #original class. The concept is that in some cases you may want to add
    #additional attributes or methods to a class without having to either
    #completely duplicate the class or modify the existing class. This would
    #be creating a child of a class and would inherit all the properties
    #and functions of the parent class.
    #As an example, let’s consider the User class. You will probably want to
    #track basic attributes like name, email, address, etc. about all users
    #for your site. However, if you have employees and customers using a site,
    #there are probably additional attributes you want to track for each that
    #don’t overlap. To make the code as concise as possible, you’d want to have
    #a parent class of User for the attributes and methods common to both.
    #You would also want a child class for Employee and Customer that track
    #the additional attributes and methods for those objects.
#Demonstrated with code:
class User:
    name = 'No Name Provided'
    email = ' '
    password = '1234abcd'
    account = 0

class Employee(User):
    base_pay = 11.00
    department = 'General'

class Customer(User):
    mailing_address = ' '
    mailing_list = True
    
#The User class now has 'Employee' and 'Customer' child classes,
#with their own added attributes that are unique to them. The child
#classes also inherit all attributes from the parent class ('User').

































