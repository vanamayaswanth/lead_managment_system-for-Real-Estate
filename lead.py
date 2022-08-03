#lead management system for real estate
import sqlite3
import os
import sys
import time
import datetime


def create_table():
    conn = sqlite3.connect('lead.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS lead(id INTEGER PRIMARY KEY, name TEXT, phone TEXT, email TEXT, message TEXT, date TEXT)")
    conn.commit()
    conn.close()


def insert(name, phone, email, message):
    conn = sqlite3.connect('lead.db')
    c = conn.cursor()
    c.execute("INSERT INTO lead VALUES (NULL, ?, ?, ?, ?, ?)", (name, phone, email, message, datetime.datetime.now()))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect('lead.db')
    c = conn.cursor()
    c.execute("SELECT * FROM lead")
    rows = c.fetchall()
    conn.close()
    return rows


def search(name = "", phone = "", email = "", message = ""):
    conn = sqlite3.connect('lead.db')
    c = conn.cursor()
    c.execute("SELECT * FROM lead WHERE name = ? OR phone = ? OR email = ? OR message = ?", (name, phone, email, message))
    rows = c.fetchall()
    conn.close()
    return rows



def delete(id):
    conn = sqlite3.connect('lead.db')
    c = conn.cursor()
    c.execute("DELETE FROM lead WHERE id = ?", (id,))
    conn.commit()
    conn.close()


def update(id, name, phone, email, message):
    conn = sqlite3.connect('lead.db')
    c = conn.cursor()
    c.execute("UPDATE lead SET name = ?, phone = ?, email = ?, message = ? WHERE id = ?", (name, phone, email, message, id))
    conn.commit()
    conn.close()

def check_duplicate_leads():
    conn = sqlite3.connect('lead.db')
    c = conn.cursor()
    c.execute("SELECT * FROM lead")
    rows = c.fetchall()
    conn.close()
    return rows

create_table()
insert("John Doe", "0712345678", "" , "I want to buy a house")



def lead_menu():
    print("1. Insert a new lead")
    print("2. View all leads")
    print("3. Search lead")
    print("4. Delete lead")
    print("5. Update lead")
    print("6. Check for duplicate leads")
    print("7. Exit")
    print("\n")
    choice = input("Enter your choice: ")
    return choice


def main():
    while True:
        choice = lead_menu()
        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            message = input("Enter message: ")
            insert(name, phone, email, message)
            print("\n")
            print(f"Lead inserted successfully")
            print("\n")
        elif choice == "2":
            print("All leads: ")
            print("\n")
            for i in view():
                print(i)
            print("\n")
        elif choice == "3":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            message = input("Enter message: ")
            print("\n")
            for i in search(name, phone, email, message):
                print(i)
            print("\n")
        elif choice == "4":
            id = int(input("Enter id: "))
            delete(id)
            print("\n")
            print(f"Lead deleted successfully")
            print("\n")
        elif choice == "5":
            id = int(input("Enter id: "))
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            message = input("Enter message: ")
            update(id, name, phone, email, message)
            print("\n")
            print(f"Lead updated successfully")
            print("\n")
        elif choice == "6":
            #check for duplicate leads
            for i in check_duplicate():
                if i[1] in check_duplicate_phone():
                    print("Duplicate lead found")
                    print("\n")
                    delete(i[0])
                    print("\n")
                    print("Lead deleted successfully")
                    print("\n")
        elif choice == "7":
            print("\n")
            print("Bye")
            print("\n")
            sys.exit()
        else:
            print("\n")
            print("Invalid choice")
            print("\n")


#check for the duplicate leads
def check_duplicate():
    conn = sqlite3.connect('lead.db')
    c = conn.cursor()
    c.execute("SELECT * FROM lead")
    rows = c.fetchall()
    conn.close()
    return rows



#check for duplicate leads using the phone number
def check_duplicate_phone():
    conn = sqlite3.connect('lead.db')
    c = conn.cursor()
    c.execute("SELECT * FROM lead")
    rows = c.fetchall()
    conn.close()
    return rows



if __name__ == '__main__':
    main()










