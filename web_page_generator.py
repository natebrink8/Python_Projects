import tkinter as tk
from tkinter import *

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        #Sets title of GUI window
        self.master.title("Web Page Generator")




if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()







"""
        #Creates function to exit the program
    def exit_program(self):
        #root is the main GUI window, the tkinter destroy method tells Python
        #to terminate root.mainloop and all widgets inside the GUI window
        root.destroy()
"""
