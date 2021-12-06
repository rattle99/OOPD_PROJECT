import sqlite3
from tabulate import tabulate


class Order:

    def __init__(self):
        pass

    def fetch_kolkata(self, row):

        conn = sqlite3.connect('Restaurents.db')
        c = conn.cursor()
        c.execute("SELECT rowid, * FROM kolkata WHERE rowid = (?)", (row,))
        items = c.fetchall()
        self.x = items[0]
        return self.x[1], self.x[2], self.x[3]

    def fetch_Haldiram(self, row):

        conn = sqlite3.connect('Restaurents.db')
        c = conn.cursor()
        c.execute("SELECT rowid, * FROM Haldiram WHERE rowid = (?)", (row,))
        items = c.fetchall()
        self.x = items[0]
        return self.x[1], self.x[2], self.x[3]

    def fetch_Bikaner(self, row):

        conn = sqlite3.connect('Restaurents.db')
        c = conn.cursor()
        c.execute("SELECT rowid, * FROM Bikaner WHERE rowid = (?)", (row,))
        items = c.fetchall()
        self.x = items[0]
        return self.x[1], self.x[2], self.x[3]

    def fetch_Mongini(self, row):

        conn = sqlite3.connect('Restaurents.db')
        c = conn.cursor()
        c.execute("SELECT rowid, * FROM Mongini WHERE rowid = (?)", (row,))
        items = c.fetchall()
        self.x = items[0]
        return self.x[1], self.x[2], self.x[3]

    def fetch_Udupi(self, row):

        conn = sqlite3.connect('Restaurents.db')
        c = conn.cursor()
        c.execute("SELECT rowid, * FROM Udupi WHERE rowid = (?)", (row,))
        items = c.fetchall()
        self.x = items[0]
        return self.x[1], self.x[2], self.x[3]

    def fetch_Om(self, row):

        conn = sqlite3.connect('Restaurents.db')
        c = conn.cursor()
        c.execute("SELECT rowid, * FROM Om WHERE rowid = (?)", (row,))
        items = c.fetchall()
        self.x = items[0]
        return self.x[1], self.x[2], self.x[3]

    def order_input(self):
        print("Enter the Index of Item and the Quantity you want to order:")
        print("Enter 0 if you completed your cart:")
        x = list()
        while True:

            li = [int(x) for x in input().split()]
            if li[0] == 0:
                break
            x.append(li)
        self.index_li = list()
        self.quantity_li = list()
        for i, j in x:
            self.index_li.append(i)
            self.quantity_li.append(j)
        return self.index_li, self.quantity_li

    def create_table(self):
        conn = sqlite3.connect('Orders.db')
        c = conn.cursor()
        c.execute(""" CREATE TABLE Final_Order (
                Item DATATYPE,
                Quantity DATATYPE,
                Price DATATYPE,
                Time DATATYPE
               ) """)
        conn.commit()
        conn.close()

    def Add(self, name, quantity, price, time):
        conn = sqlite3.connect('Orders.db')
        c = conn.cursor()
        c.execute("INSERT INTO Final_Order VALUES (?,?,?,?)",
                  (name, quantity, price, time))

        conn.commit()

        conn.close()

    def drop_table(self):
        conn = sqlite3.connect('Orders.db')
        c = conn.cursor()
        c.execute("DROP TABLE Final_Order")
        conn.commit()
        conn.close()

    def show_order(self):
        conn = sqlite3.connect('Orders.db')
        c = conn.cursor()

        c.execute("SELECT rowid, * FROM Final_Order")
        items = c.fetchall()
        head = ['INDEX', 'ITEM', 'QUANTITY', 'PRICE', 'TIME (In Minutes)']
        idx = list()
        it = list()
        qua = list()
        pri = list()
        ti = list()
        for item in items:
            idx.append(item[0])
            it.append(item[1])
            qua.append(item[2])
            pri.append(item[3])
            ti.append(item[4])

        table_data = list(zip(idx, it, qua, pri, ti))
        table = tabulate(headers=head, tabular_data=table_data, tablefmt="rst")
        print(table)
        conn.commit()
        conn.close()

    def order_summary(self, x, y, func):
        for i in range(len(x)):
            mock_price = 0
            name, pri, time = func(x[i])
            mock_price = pri * y[i]
            self.Add(name, y[i], mock_price, time)

    def avg_time_bill(self):
        conn = sqlite3.connect('Orders.db')
        c = conn.cursor()

        c.execute("SELECT rowid, * FROM Final_Order")
        items = c.fetchall()
        self.bill_price = 0
        total_count = 0
        time = list()
        for item in items:
            mock_time = item[2] * item[4]
            self.bill_price = self.bill_price + item[3]
            time.append(item[4])

        self.time_required = max(time)
        return self.time_required, self.bill_price

    def delete_item(self, row):
        conn = sqlite3.connect('Orders.db')
        c = conn.cursor()
        c.execute("DELETE from Final_Order WHERE rowid = (?)", (row,))
        conn.commit()
        conn.close()

    def Enter(self):
        print("Select '1' if you want to Delete any Item:")
        print("Select '2' if you want to Add any Item:")
        print("Select '3' if you want to Proceed Forward for the Payment:")
        print("Select '4' for discarding the entire Order:")
        print("Select '5' for Adding any Item to the Wishlist:")
