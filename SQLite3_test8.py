#Import the SQLite3 module:
import sqlite3













#set the var for dB connection [varName = class.method]; also creating test.db in the dir.
conn = sqlite3.connect('test.db')

#create a with loop for while we have this token open, perform these lines of code
with conn:
    #set the cursor var name to operate on the dB:
    cur = conn.cursor()
    #Create the execute command and code to create columns in the table:
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_persons( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT, \
        col_lname TEXT, \
        col_email TEXT \
        )")
    #commit while connected
    conn.commit()
#close connection
conn.close()



#use the dB connection var for execution, to write data to the table:
conn = sqlite3.connect('test.db')

#create a with loop for while we have this token open, perform these lines of code
with conn:
    #set the cursor var name to operate on the dB:
    cur = conn.cursor()
    #Create the execute command with SQL commands to write data:
    cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES (?,?,?)", \
                ('Sarah', 'Jones', 'sjones@gmail.com'))
    cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES (?,?,?)", \
                ('Sally', 'May', 'sallymay@gmail.com'))
    cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES (?,?,?)", \
                ('Kevin', 'Bacon', 'BAKE-DOG@AOL.COM'))
    #commit while connected
    conn.commit()
#close connection
conn.close()
    


#use the dB connection var for execution, to query the table:
conn = sqlite3.connect('test.db')

#create a with loop for while we have this token open, perform these lines of code
with conn:
    #set the cursor var name to operate on the dB:
    cur = conn.cursor()
    #Create the execute command with SQL queries:
    cur.execute("SELECT col_fname, col_lname, col_email FROM tbl_persons WHERE col_fname = 'Sarah'")
    #set a var to return all values from the query (thus the fetchall command):
    varPerson = cur.fetchall()
    for item in varPerson:
        #Display desired text alongside retrieved data:
        msg = "First Name: {}\nLast Name: {}\nEmail: {}".format(item[0], item[1], item[2])
    print(msg)











