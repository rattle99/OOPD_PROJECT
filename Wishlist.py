import sqlite3
import pandas as pd
from tabulate import tabulate


def create_table_wishlist():
    conn = sqlite3.connect('Orders.db')
    c = conn.cursor()
    c.execute(""" CREATE TABLE Wishlist (
            Item DATATYPE,
            Price DATATYPE
           ) """)
    conn.commit()
    conn.close()

def order_input_wishlist():
    print("Enter the Index of Item you want to add to your Wishlist:")
    print("Enter 0 if you completed your cart:")
    li = list()
    while True:

        x = int(input())
        if x == 0:
            break
        li.append(x)
    return li


def Add_Wishlist(name, price):
    conn = sqlite3.connect('Orders.db')
    c = conn.cursor()
    c.execute("INSERT INTO Wishlist VALUES (?,?)", (name, price))

    conn.commit()

    conn.close()


def Wishlist_summary(x, func):
    for i in range(len(x)):
        name, pri, time = func(x[i])
        Add_Wishlist(name, pri)

def drop_table_wishlist():
    conn = sqlite3.connect('Orders.db')
    c = conn.cursor()
    c.execute("DROP TABLE Wishlist")
    conn.commit()
    conn.close()


def show_wishlist():
    conn = sqlite3.connect('Orders.db')
    c = conn.cursor()

    c.execute("SELECT rowid, * FROM Wishlist")
    items = c.fetchall()
    head = ['INDEX', 'ITEM', 'PRICE']
    idx = list()
    it = list()
    pri = list()
    for item in items:
        idx.append(item[0])
        it.append(item[1])
        pri.append(item[2])

    table_data = list(zip(idx, it, pri))
    table = tabulate(headers=head, tabular_data=table_data, tablefmt="rst")
    print(table)

    conn.commit()
    conn.close()
