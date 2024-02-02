#
#Python:     3.11.7
#
#Author:     Nate Brink
#
#Purpose:    Learning to code a game in Python.
#



def start(nice=0, mean=0, name=""):
    # get user's name
    name = describe_game(name)
    nice, mean, name = nice_mean(nice, mean, name)


def describe_game(name):
    """
        check if this is a new game
        If it is new, get the user's name.
        If it is not new, thank the player for
        playing again and continue with the game.
    """
    #meaning, if we do not already have the user's name,
    #then they are a new player and we need to get their name.

    if name != "":
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>> ").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be greeted \nby a bunch of freaks. \nYou can choose to be nice or mean")
                    print("but, at the end of the game, your fate \nwill be sealed by your actions.")
                    stop = False
    return name


def nice_mean(nice, mean, name):
    stop = True
    while stop:
        show_score(nice, mean, name)
        pick = input("\nA stranger approaches you for a \nconversation. Will you be nice \nor be mean? (N/M) \n>>>: ").lower()
        if pick == "n":
            print("\nThe stranger turns around and skips away...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\nThe stranger glares at you \nand says ALL YOUR BASES ARE BELONG TO US.")
            mean = (mean + 1)
            stop = False
    score(nice, mean, name)     # Pass the 3 variables to the score


def show_score(nice, mean, name):
    print("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name, nice, mean))


def score(nice, mean, name):
    # score function is being passed the values stored within the 3 variables
    if nice > 2:    # if condition is valid, call WIN function to pass the variables to use
        win(nice, mean, name)
    if mean > 2:    # if condition is valid, call LOSE function to pass the variables to use
        lose(nice, mean, name)
    else:           # else call nice_mean function to pass variables to use
        nice_mean(nice, mean, name)


def win(nice, mean, name):
    # substitute the {} placeholders with variable values
    print("\nNice job {}, you win! \nEveryone loves you and you've \nmade lots of friends along the way!".format(name))
    # call again function and pass in the variables
    again(nice, mean, name)



def lose(nice, mean, name):
    # substitute the {} placeholders with variable values
    print("\nAhhh too bad, game over! \n{}, you live in a dirty beat-up \nvan down by the river, wretched and alone!".format(name))
    # call again function and pass in the variables
    again(nice, mean, name)



def again(nice, mean, name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n):\n>>> ").lower()
        if choice == "y":
            stop = False
            reset(nice, mean, name)
        if choice == "n":
            print("\nOk, BEAT IT. No, seriously, kick rocks!")
            stop = False
            quit()
        else:
            print("\nEnter ( Y ) for 'YES', ( N ) for 'NO':\n>>> ")
            ##WITH BREAKS print("\nEnter \( Y \) for \'YES\', \( N \) for \'NO\':\n>>> ")


def reset(nice, mean, name):
    nice = 0
    mean = 0
    # notice the name variable is not reset as the same user is playing again
    start(nice, mean, name)




if __name__ == "__main__":
    start()
