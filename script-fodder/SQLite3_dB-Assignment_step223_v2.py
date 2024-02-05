#Import the SQLite3 module:
import sqlite3

#set the var for dB connection:
conn = sqlite3.connect('n8Test.db')
with conn:
    cur = conn.cursor()
    #Create the table that does not exist, and
    #create the code for the table columns:
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_n8Files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fileName STRING \
        )")
    #commit while connected
    conn.commit()
#close connection
conn.close()

#set var for dB connection:
conn = sqlite3.connect('n8test.db')
#create a with loop for while we have this token open, perform these lines of code
with conn:
    #set the cursor var name to operate on the dB:
    cur = conn.cursor()
    #set var for fileList to use in the foreach/TXT file loop:
    fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
                'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

    #Create the foreach code to search the fileList set for TXT files
    #and to insert the file names to the dB:
    for x in fileList:
        if x.endswith(".txt"):
            cur.execute("INSERT INTO tbl_n8Files(col_fileName) VALUES(?)", (x,))
            #Print the TXT file names to the console:
            print(x)
    #commit while connected
    conn.commit()
#close connection
conn.close()

