#get the data from the tables and do the analysis

import sqlite3
import sys 
import os 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


conn = sqlite3.connect('lead.db')
c = conn.cursor()

def analysis():
    conn = sqlite3.connect('lead.db')
    c = conn.cursor()
    c.execute("SELECT * FROM leads")
    data = c.fetchall()
    df = pd.DataFrame(data, columns=['id', 'name', 'phone', 'email', 'message'])
    return df

def analysis_menu():
    print("1. View all leads")
    print("2. Exit")
    print("\n")
    choice = input("Enter your choice: ")
    return choice


def main():
    while True:
        choice = analysis_menu()
        if choice == "1":
            print("\n")
            for i in analysis():
                print(i)
            print("\n")
        elif choice == "2":
            print("\n")
            print("Bye")
            print("\n")
            sys.exit()
        else:
            print("\n")
            print("Invalid choice")
            print("\n")


if __name__ == '__main__':
    main()


    