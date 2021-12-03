import sqlite3
import pandas as pd


class Restaurant:

    def __init__(self):
        pass

    def show_all(self):
        conn = sqlite3.connect('Restaurents.db')
        c = conn.cursor()

        c.execute("SELECT rowid, * FROM Restaurent")
        items = c.fetchall()
        print("INDEX" + "\t\t" + "RESTAURANT" + "\t\t" + "LATITUDE" + "\t" + "LONGITUDE")
        print("_________________________________________________________________")
        for i, j, k, l in items:
            if j == "KOLKATA KATHI ROLLS":
                print(str(i) + "\t\t" + j + "\t" + str(k) + "\t\t" + str(l))
            elif j == "UDUPI":
                print(str(i) + "\t\t" + j + "\t\t\t\t" + str(k) + "\t\t" + str(l))
            elif j == "MONGINI-BAKERY":
                print(str(i) + "\t\t" + j + "\t\t" + str(k) + "\t\t" + str(l))

            else:
                print(str(i) + "\t\t" + j + "\t\t\t" + str(k) + "\t\t" + str(l))

        conn.commit()
        conn.close()

    def read_one(self, x):
        conn = sqlite3.connect('Restaurents.db')
        c = conn.cursor()

        c.execute("SELECT rowid, * FROM Restaurent WHERE rowid = (?)", (x,))
        items = c.fetchall()
        x = items[0]
        return x[1], x[2], x[3]

    def show_kolkata(self):
        conn = sqlite3.connect('Restaurents.db')
        c = conn.cursor()

        c.execute("SELECT rowid, * FROM kolkata")
        items = c.fetchall()
        print("INDEX" + "\t\t" + "MENU" + "\t\t\t" + "PRICE" + "\t" + "PREPARATION TIME")
        print("_________________________________________________________________")
        for i, j, k, l in items:
            if j == "Veg Roll" or j == "Paneer Roll" or j == "Malai Chaap" or j == "Fried Rice":
                print(str(i) + "\t\t" + j + "\t\t\t" + str(k) + "\t\t" + str(l))
            else:
                print(str(i) + "\t\t" + j + "\t\t" + str(k) + "\t\t" + str(l))

        conn.commit()
        conn.close()

    def show_Haldiram(self):
        conn = sqlite3.connect('Restaurents.db')
        c = conn.cursor()

        c.execute("SELECT rowid, * FROM Haldiram")
        items = c.fetchall()
        print("INDEX" + "\t\t" + "MENU" + "\t\t\t" + "PRICE" + "\t" + "PREPARATION TIME")
        print("_________________________________________________________________")
        for i, j, k, l in items:
            if j == "Noodles":
                print(str(i) + "\t\t" + j + "\t\t\t\t" + str(k) + "\t\t" + str(l))
            elif j == "Raj Kachori" or j == "Pao Bhaaji":
                print(str(i) + "\t\t" + j + "\t\t\t" + str(k) + "\t\t" + str(l))
            elif j == "Executive Thaali":
                print(str(i) + "\t\t" + j + "\t" + str(k) + "\t\t" + str(l))
            else:
                print(str(i) + "\t\t" + j + "\t\t" + str(k) + "\t\t" + str(l))

        conn.commit()
        conn.close()

    def show_Bikaner(self):
        conn = sqlite3.connect('Restaurents.db')
        c = conn.cursor()

        c.execute("SELECT rowid, * FROM Bikaner")
        items = c.fetchall()
        print("INDEX" + "\t\t" + "MENU" + "\t\t\t" + "PRICE" + "\t" + "PREPARATION TIME")
        print("_________________________________________________________________")
        for i, j, k, l in items:
            if j == "Executive Thaali":
                print(str(i) + "\t\t" + j + "\t" + str(k) + "\t\t" + str(l))
            elif j == "Raaj Bhog" or j == "Raj Kachori" or j == "Papdi Chaat":
                print(str(i) + "\t\t" + j + "\t\t\t" + str(k) + "\t\t" + str(l))

            else:
                print(str(i) + "\t\t" + j + "\t\t" + str(k) + "\t\t" + str(l))

        conn.commit()
        conn.close()

    def show_Mongini(self):
        conn = sqlite3.connect('Restaurents.db')
        c = conn.cursor()

        c.execute("SELECT rowid, * FROM Mongini")
        items = c.fetchall()
        print("INDEX" + "\t\t" + "MENU" + "\t\t\t" + "PRICE" + "\t" + "PREPARATION TIME")
        print("_________________________________________________________________")
        for i, j, k, l in items:
            if j == "Choco Truffle" or j == "Buttorscotch" or j == "Paneer Pateez":
                print(str(i) + "\t\t" + j + "\t\t" + str(k) + "\t\t" + str(l))
            else:
                print(str(i) + "\t\t" + j + "\t\t\t" + str(k) + "\t\t" + str(l))
        conn.commit()
        conn.close()

    def show_Udupi(self):
        conn = sqlite3.connect('Restaurents.db')
        c = conn.cursor()

        c.execute("SELECT rowid, * FROM Udupi")
        items = c.fetchall()
        print("INDEX" + "\t\t" + "MENU" + "\t\t\t" + "PRICE" + "\t" + "PREPARATION TIME")
        print("_________________________________________________________________")
        for i, j, k, l in items:
            if j == "Sambhar Wada":
                print(str(i) + "\t\t" + j + "\t\t" + str(k) + "\t\t" + str(l))
            elif j == "Utappam" or j == "Appam":
                print(str(i) + "\t\t" + j + "\t\t\t\t" + str(k) + "\t\t" + str(l))
            else:
                print(str(i) + "\t\t" + j + "\t\t\t" + str(k) + "\t\t" + str(l))

        conn.commit()
        conn.close()

    def show_Om(self):
        conn = sqlite3.connect('Restaurents.db')
        c = conn.cursor()

        c.execute("SELECT rowid, * FROM Om")
        items = c.fetchall()
        print("INDEX" + "\t\t" + "MENU" + "\t\t\t" + "PRICE" + "\t" + "PREPARATION TIME")
        print("_________________________________________________________________")
        for i, j, k, l in items:
            if j == "Raaj Bhog" or j == "Raaj Thaali" or j == "Pao Bhaji":
                print(str(i) + "\t\t" + j + "\t\t\t" + str(k) + "\t\t" + str(l))
            else:
                print(str(i) + "\t\t" + j + "\t\t" + str(k) + "\t\t" + str(l))

        conn.commit()
        conn.close()
