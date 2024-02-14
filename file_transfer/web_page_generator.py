import tkinter as tk
from tkinter import *
import webbrowser


class ParentWindow(Frame):
    """
        # The below code will generate a default HTML file,
        # using Python modules and defining the desired values.
    """
    def __init__(self, master):
        Frame.__init__(self, master)
        # INSERT the desired default Title value in the quoted text:
        self.master.title("Web Page Generator")

    #Row 0 contains the text above the text field:
        self.customHtml = Label(justify=LEFT, text="Enter custom HTML in the field below or click the Default HTML Page button").grid(row=0, column=0, columnspan=3, padx=(10, 10), pady=(10, 10))

    #Row 1 contains the text field for custom HTML:
        self.customHtmlEntry = Text(root, height=1, width=60)
        self.customHtmlEntry.grid(row=1, column=0, columnspan=3, padx=(10, 10), pady=(0, 10))

    #Row 2 contains the buttons:
        #DEFAULT HTML Button
        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)      #ADD Command last
        self.btn.grid(row=2, column=1, padx=(200,0), pady=(0,15))

        #CUSTOM HTML Button
        self.btn = Button(self.master, text="Submit Custom HTML", width=30, height=2, command=self.customHTML)      #ADD Command last
        self.btn.grid(row=2, column=2, padx=(10,40), pady=(0,15))

    
    def defaultHTML(self):
        # SET the default 'h1' header value:
        htmlText = "Stay tuned for our amazing summer sale!"    #'h1' value.
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")


    def customHTML(self):
        # PROVIDE a field for the 'h1' header value:
        customHtml = self.customHtmlEntry.get("1.0", END)
        print(customHtml)
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + customHtml + "</h1>\n</body>\n</html>" 
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
