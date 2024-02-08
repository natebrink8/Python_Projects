import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil
#New/Updated File Transfer Automation: ADDED import time & datetime modules.
import time
import datetime


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        #Sets title of GUI window
        self.master.title("File Transfer")

        #Creates button to select files from source directory
        self.sourceDir_btn = Button(text="Select Source", width=20, command=self.sourceDir)
        #Positions source button in GUI using tkinter grid()
        self.sourceDir_btn.grid(row=0, column=0, padx=(20, 10), pady=(30, 0))

        #Creates entry for source directory selection
        self.source_dir = Entry(width=75)
        #Positions entry in GUI using tkinter griod() padx and pady
        #are the same as the button to ensure they will line up
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20, 10), pady=(30, 0))

        #Creates button to select destination of files from destination directory
        self.destDir_btn = Button(text="Select Destination", width=20, command=self.destDir)
        #Positions destination button in GUI using tkinter grid()
        #on the next row under the Source button
        self.destDir_btn.grid(row=1, column=0, padx=(20, 10), pady=(15, 10))

        #Creates entry for destination directory selection
        self.destination_dir = Entry(width=75)
        #Positions entry in GUI using tkinter grid() padx and pady
        #are the same as the button to ensure they will line up
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=(15, 10))
    
        #Creates button to transfer files
        self.transfer_btn = Button(text="Transfer Files", width=20, command=self.transferFiles)
        #Positions Transfer Files button
        self.transfer_btn.grid(row=2, column=1, padx=(200, 0), pady=(0, 15))

        #Creates an Exit button
        self.exit_btn = Button(text="Exit", width=20, command=self.exit_program)
        #Positions the Exit button
        self.exit_btn.grid(row=2, column=2, padx=(10, 40), pady=(0, 15))


    #Creates function to select source directory.
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        #The .delete(0, END) will clear the content that is inserted in the Entry
        #widget, which allows the path to be inserted to the Entry widget properly.
        self.source_dir.delete(0, END)
        #The .insert method will insert the user selection to the source_dir Entry
        self.source_dir.insert(0, selectSourceDir)
    
    #Creates function to select destination directory.
    def destDir(self):
        selectDestDir = tkinter.filedialog.askdirectory()
        #The .delete(0, END) will clear the content that is inserted in the Entry
        #widget, which allows the path to be inserted to the Entry widget properly.
        self.destination_dir.delete(0, END)
        #The .insert method will insert the user selection to the destination_dir Entry
        self.destination_dir.insert(0, selectDestDir)
    
    #Creates function to transfer files from one directory to another
#//////////UPDATE this function to account for new//////////
#//////////and updated files to automatically transfer//////////
    def transferFiles(self):
        #Gets source directory
        source = self.source_dir.get()
        #Gets destination directory
        destination = self.destination_dir.get()
        #Gets a list of files in the source directory
        source_files = os.listdir(source)
        #Runs through each file in the source directory
        for i in source_files:
            #moves each file from the source to the destination
            shutil.move(source + '/' + i, destination)
            print(i + 'was successfully transferred.')

        #Creates function to exit the program
    def exit_program(self):
        #root is the main GUI window, the tkinter destroy method tells Python
        #to terminate root.mainloop and all widgets inside the GUI window
        root.destroy()


#New/Updated File Transfer Automation:
        #Set variables for the Source and Destination directories for automation:
        auto_source_dir = "C:\\Users\\ochob\\OneDrive\\Documents\\GitHub\\Python_Projects\\file_transfer\\Customer_Source"
        auto_destination_dir = "C:\\Users\\ochob\\OneDrive\\Documents\\GitHub\\Python_Projects\\file_transfer\\Customer_Destination"

        #Initialize variables for the new / updated file(s):
        auto_source_filename = None

        #Define variables for NOW:
        auto_time_now = datetime.datetime.now()
        #Create the variable for the 24 hour day in seconds:
        auto_day_in_seconds = 24 * 60 * 60
        #Create the variable for NOW minus 24 hour day in seconds:
        auto_time_before = auto_time_now - auto_day_in_seconds

        #For each new/updated file in the directory:
        for auto_source_newfile in os.scandir(auto_source_dir):
            if auto_source_newfile.is_file():
                #Get the modification time of the file:
                auto_lastmod_time = auto_source_newfile.stat().st_mtime_ns
                if auto_lastmod_time > auto_time_before:
                    auto_srcfile_path = os.path.join(auto_source_dir, auto_source_newfile.name)
                    auto_time_before = auto_lastmod_time
        
        #Move the file from the source directory to the destination directory:
        with open(auto_srcfile_path):
            shutil.move(auto_srcfile_path, auto_destination_dir)



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()





#//////////DATETIME CODE UPDATE FODDER//////////
"""
    COMMENTS TO INSERT:
        #New/Updated File Transfer Automation: 
    
    FODDER:
        datetime.timedelta
#//////////////THIS WON'T HAVE THE FILE NAME YET, IT IS JUST THE FOLDER
        def auto_file_path(auto_source_dir):
            return(os.path.basename(auto_source_dir).split('/')[-1])
    #Define any file names' last modified timestamps///////DO I NEED TO USE SYS VALUE FOR FNAME/FILE NAME?:
        def auto_lastmod_time(auto_file_path):
            return os.path.getmtime(auto_file_path)
    
    #OLD CODE:
        #Set the absolute path of the SOURCE file:
            auto_srcfile_path = os.path.join(auto_source_dir, auto_source_filename)
            #If the last modified date is greater than (1 day ago):
            if auto_lastmod_time(auto_source_filename) > auto_time_before:
                #then the absolute path of the SOURCE file is (JOIN: the source dir and the source file name):
                auto_srcfile_path = os.path.join(auto_source_dir, auto_source_filename)
                #and move the (absolute source file path) to the (destination directory):
                shutil.move(auto_srcfile_path, auto_destination_dir)
"""
