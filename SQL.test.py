import sqlite3
connection = sqlite3.connect('MyTestBase.db')

cursor = connection.cursor()
# SQlite dataTypes
# Intiger
# Real
# Text
# Blobs
# Null

# -------------------------------------------------------------------------------
#cursor.execute('CREATE TABLE employees(name TEXT, surname TEXT, salary REAL)')

#connection.commit()

# -------------------------------------------------------------------------

#cursor.execute("INSERT INTO employees VALUES('Mark', 'Maxell', 200000)")

#connection.commit()


#cursor.execute("SELECT * FROM employees")

#dbs = cursor.fetchall()

# print(dbs)

# ------------------------------------------------------------------------





#for i in cursor.execute("SELECT * FROM employees"):
#    print(i)

# input records from variables ------------------------

#name = 'King'
#surname = 'Arthur'
#salary = 50000

#cursor.execute("INSERT INTO employees VALUES(?,?,?)", (name, surname, salary))

#cursor.execute("SELECT * FROM employees")

#connection.commit()

dbs1 = cursor.fetchall()

print(dbs1)

# -----------------------------------------

""" name = input('Provide a name: ')
surname = input('Provide a surname: ')
salary = float(input('Provide a salary: '))

cursor.execute("INSERT INTO employees VALUES(?,?,?)", (name, surname, salary))

cursor.execute("SELECT * FROM employees")

connection.commit()

dbs2 = cursor.fetchall()

print(dbs2) """

# Using a constructor (OOP) to fill tables ----------------------------------------------------------

class SQLinput:
    def __init__(self, name, surname,salary):
        self.name = name
        self.surname = surname
        self.salary = salary

inst = SQLinput('Denzel', 'Sullivan', 1000000)
name, surname, salary = inst.name, inst.surname, inst.salary



cursor.execute("INSERT INTO employees VALUES(?,?,?)", (name, surname, salary))

cursor.execute("SELECT * FROM employees")

connection.commit()

dbs2 = cursor.fetchall()

print(dbs2)
