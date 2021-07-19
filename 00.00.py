#phonebook
#sedaghat
import sqlite3

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
        cursor.execute(update_query, (name))
        connection.commit()
        print("deleted successfully")

        cursor.close()

    except sqlite3.Error as error:
        print("fialed to delet", error)




        connection.close()

deletesql("pani")
