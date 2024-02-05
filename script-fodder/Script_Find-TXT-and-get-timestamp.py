##Step 214: SCRIPT ASSIGNMENT
#CONVERTING the timestamp:  https://www.easydevguide.com/posts/file_time


import os
import sys
import time


fPath = "C:\\Yucky\\"



def deets():
    go = True
    while go:
        try:
            for file in os.listdir("{}".format(fPath)):
                if (file.endswith(".txt")):
                    print(os.path.join("{}".format(fPath), file))
                    go = False
        except OSError:
            print("No File!")



def fileDates():
    go = True
    while go:
        try:
            for file in os.listdir("{}".format(fPath)):
                if os.path.getmtime(os.path.join("{}".format(fPath), file)) != "":
                    print("\nLast Modified: ", os.path.getmtime(os.path.join("{}".format(fPath), file)))
                    go = False
        except OSError:
            print("No Time Magruber!")
    



if __name__ == "__main__":
    deets()
    fileDates()


