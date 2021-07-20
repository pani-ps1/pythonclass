#phonebook
#sedaghat
import sqlite3

class Phonbook():
    def __init__(self, read_phonbook, add_contact, show_phonbook, deletesql, menu):
        def menu(self):
            choice = input("ENTER CHOICE: ")
            choice_menu = {'1' : self.read_phonbook,
                            '2' : self.add_contact,
                            '3' : self.show_phonbook,
                            '4' : self.deletesql,
                            '5' : self.search_phonbook}
            if choice not in choice_menu.keys():
                print("PLEASE ENTER A VALID CHOICE")
            else:
                choice_menu[choice]()

        obj = Phonbook(self)
print("phone book is = ",(obj))



def read_phonbook():
    connection = sqlite3.connect("phonbook.db")

    cursor = connection.cursor()

    query = 'select * from phonebook '

    result = cursor.execute(query)


    for r in result:
        list = [r[0],    r[1],   r[2]]
        print(list)

    connection.commit()
    connection.close()

read_phonbook()





import sqlite3

def add_contact():
    connection = sqlite3.connect("phonbook.db")

    cursor = connection.cursor()

    query = 'insert into phonebook values("{}" ,"{}","{}")'


    name = input("enter your name\n:")
    number = input("enter your number\n:")
    adress = input("enter your adress\n:")


    cursor.execute(query.format(id, name, number, adress))

    connection.commit()
    connection.close()

add_contact()



import sqlite3

def show_phonbook():

    connection = sqlite3.connect("phonbook.db")

    cursor = connection.cursor()

    query = 'select * from phonebook '

    result = cursor.execute(query)


    for r in result:
        list = [r[0],    r[1],   r[2]]
        print(list)

    connection.commit()
    connection.close()

show_phonbook()



import sqlite3

def deletesql(name):
    try:
        connection = sqlite3.connect("phonbook.db")
        cursor = connection.cursor()

        update_query = """DELETE from phonebook where name = ?"""
        cursor.execute(update_query, (name,))
        connection.commit()
        print("deleted successfully")

        cursor.close()

    except sqlite3.Error as error:
        print("fialed to delet", error)




        connection.close()

deletesql("pani")




import sqlite3

def search_phonbook():
    try:
        connection = sqlite3.connect("phonbook.db")

        cursor = connection.cursor()

        search_query = """ select * form phonbook WHERE name = ?"""
        cursor.execute(serach_query, (name,))
        records = cursor.fetchall()
        print("showin name: ", name)
        for row in records:
            print("name = ",row[1])
            print("number = ",row[2])
            print("adress = ", row[3])

        cursor.close()

    except sqlite3.Error as erorr:
        print("faild to read data", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print(" the phonebook is closed")


search_phonbook()
phonbook()
