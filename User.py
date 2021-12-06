import sqlite3
import pandas as pd


class User:
    def __init__(self):
        pass

    def User_Registration(self):

        print("Welcome to the REGISTRATION PORTAL:")
        self.name = input("Enter your NAME: ")
        self.surname = input("Enter your SURNAME: ")
        self.email = input("Enter your EMAIL-ID: ")
        self.password = input("Enter your PASSWORD: ")
        print("Enter your location using GOOGLE MAPS:")
        self.lat = input("Enter LATITUDE: ")
        self.lon = input("Enter LONGITUDE: ")

        return self.name, self.surname, self.email, self.password, self.lat, self.lon

    def add_one(self, first, last, email, password, latitude, longitude, promo1=0, promo2=0):
        conn = sqlite3.connect('User.db')
        c = conn.cursor()
        c.execute("INSERT INTO users VALUES (?,?,?,?,?,?,?,?)",
                  (first, last, email, password, latitude, longitude, promo1, promo2))
        conn.commit()
        conn.close()

    def User_Verification(self, email):
        conn = sqlite3.connect('User.db')
        c = conn.cursor()

        df = pd.read_sql("SELECT * FROM users", conn)

        conn.commit()
        # Close our Connection
        conn.close()
        email_li = df["email"].tolist()

        if email in email_li:
            return True

        return False

    def User_Authentciation(self, email, password):
        conn = sqlite3.connect('User.db')
        c = conn.cursor()

        df = pd.read_sql("SELECT * FROM users", conn)

        conn.commit()
        # Close our Connection
        conn.close()
        email_li = df["email"].tolist()
        password_li = df["password"].tolist()

        if email in email_li:
            e = email_li.index(email)
            pas = password_li[e]
            if password == pas:
                return True

        return False

    def lat_lon_user(self, email):
        conn = sqlite3.connect('User.db')
        c = conn.cursor()

        df = pd.read_sql("SELECT * FROM users", conn)

        conn.commit()
        # Close our Connection
        conn.close()
        latitude_li = df["latitude"].tolist()
        longitude_li = df["longitude"].tolist()
        email_li = df["email"].tolist()
        e = email_li.index(email)
        lat = latitude_li[e]
        lon = longitude_li[e]
        return lat, lon


class Promocode(User):

    def __init__(self):
        super().__init__()

    def update_promo1_to_1(self, email):
        conn = sqlite3.connect('User.db')
        c = conn.cursor()

        c.execute(
            """UPDATE users SET promocode_1 = 1 WHERE email = (?)""", (email,))

        conn.commit()
        conn.close()

    def update_promo1_to_0(self, email):
        conn = sqlite3.connect('User.db')
        c = conn.cursor()

        c.execute(
            """UPDATE users SET promocode_1 = 0 WHERE email = (?)""", (email,))

        conn.commit()
        conn.close()

    def update_promo2_to_1(self, email):
        conn = sqlite3.connect('User.db')
        c = conn.cursor()

        c.execute(
            """UPDATE users SET promocode_2 = 1 WHERE email = (?)""", (email,))

        conn.commit()
        conn.close()

    def update_promo2_to_0(self, email):
        conn = sqlite3.connect('User.db')
        c = conn.cursor()

        c.execute(
            """UPDATE users SET promocode_2 = 0 WHERE email = (?)""", (email,))

        conn.commit()
        conn.close()

    def show_promo1(self, email):
        conn = sqlite3.connect('User.db')
        c = conn.cursor()

        c.execute("SELECT rowid, * FROM users WHERE email = (?)", (email,))
        self.items = c.fetchall()
        return self.items[0][7]

    def show_promo2(self, email):
        conn = sqlite3.connect('User.db')
        c = conn.cursor()

        c.execute("SELECT rowid, * FROM users WHERE email = (?)", (email,))
        self.items = c.fetchall()
        return self.items[0][8]
