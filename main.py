import sqlite3
import pandas as pd
from geopy.distance import great_circle
import Restaurent
import User
from Wishlist import *
from Order import *
from Payment import *
from Tracking import *
from tabulate import tabulate

if __name__ == "__main__":
    while True:
        print("WELCOME TO THE APPLICATION:")
        print("FOR REGISTRATION PRESS 1:")
        print("FOR LOGIN PRESS 2:")
        flag = 0
        flag_1 = 0
        flag_wishlist = 0
        delivery_charge = 0
        delivery_time = 0
        x = int(input())

        if x == 1:
            # Use of Inheritance
            obj1 = User.Promocode()
            print("Welcome to the REGISTRATION PORTAL:")
            name = input("Enter your NAME: ")
            surname = input("Enter your SURNAME: ")
            email = input("Enter your EMAIL-ID: ")
            password = input("Enter your PASSWORD: ")
            print("Enter your location using GOOGLE MAPS:")
            lat = input("Enter LATITUDE: ")
            lon = input("Enter LONGITUDE: ")
            if obj1.User_Authentciation(email, password):
                print("The Entered Email or Password is already taken!")
            else:
                print("Your Account is Registered!")
                print("Now you can proceed Forward for Login:")
                print()
                print("_______________________________________")
                print()
                obj1.add_one(name, surname, email, password, lat, lon, 0, 0)

        elif x == 2:
            # Use of Inheritance
            obj2 = User.Promocode()
            print("----------------------------")
            print("Welcome to the LOGIN PORTAL:")
            print("----------------------------")
            email = input("Enter your EMAIL-ID: ")
            password = input("Enter your PASSWORD: ")
            if obj2.User_Authentciation(email, password):
                res_obj = Restaurent.Restaurant()
                user_lat_lon = obj2.lat_lon_user(email)
                print("Select the Restaurant of your choice:")
                res_obj.show_all()
                print("Enter the Index of Restaurant of your Choice: ")
                x = int(input())
                res_name, res_lat, res_lon = res_obj.read_one(x)
                res_locate = (res_lat, res_lon)
                # calculation of distance b/t user and restaurant
                dist = great_circle(user_lat_lon, res_locate).km
                if dist <= 5:
                    delivery_charge = 0
                    delivery_time = 10
                elif dist > 5 and dist <= 10:
                    delivery_charge = 30
                    delivery_time = 20
                elif dist > 10:
                    delivery_charge = 40
                    delivery_time = 30

                if res_name == "KOLKATA KATHI ROLLS":
                    res_obj.show_kolkata()
                    create_table()
                    x, y = order_input()
                    order_summary(x, y, fetch_kolkata)
                    time_avg, bill = avg_time_bill()
                    show_order()
                    while True:
                        Enter()
                        button = int(input())
                        if button == 1:
                            x = int(input("Enter the INDEX of ITEM you want to remove:"))
                            delete_item(x)
                            show_order()
                            time_avg, bill = avg_time_bill()

                        elif button == 2:
                            res_obj.show_kolkata()
                            x, y = order_input()
                            order_summary(x, y, fetch_kolkata)
                            show_order()
                            time_avg, bill = avg_time_bill()


                        elif button == 3:
                            time_avg, bill = avg_time_bill()
                            if bill < 100:
                                print("----------------------------")
                                print("The Minimum Cart Value should not be less than 100 rupees!!")
                                print("Please add more items:")
                                print("----------------------------")
                            else:
                                drop_table()
                                payment_process(dist, delivery_charge, bill, time_avg, delivery_time)
                                promo1, promo2, flag_1 = Payment(delivery_charge, bill, email, obj2)
                                Tracking(time_avg, delivery_time, promo1, promo2, email, obj2)
                                break


                        elif button == 4:
                            flag = 1
                            drop_table()
                            print("Discarding the Order")
                            break


                        elif button == 5:
                            flag_wishlist = 1
                            res_obj.show_kolkata()
                            create_table_wishlist()
                            q = order_input_wishlist()
                            Wishlist_summary(q, fetch_kolkata)
                            print("Your Wishlist:")
                            show_wishlist()


                elif res_name == "HALDIRAMS":
                    res_obj.show_Haldiram()
                    create_table()
                    x, y = order_input()
                    order_summary(x, y, fetch_Haldiram)
                    time_avg, bill = avg_time_bill()
                    show_order()
                    while True:
                        Enter()
                        button = int(input())
                        if button == 1:
                            x = int(input("Enter the INDEX of ITEM you want to remove:"))
                            delete_item(x)
                            show_order()
                            time_avg, bill = avg_time_bill()

                        elif button == 2:
                            res_obj.show_Haldiram()
                            x, y = order_input()
                            order_summary(x, y, fetch_Haldiram)
                            show_order()
                            time_avg, bill = avg_time_bill()


                        elif button == 3:
                            time_avg, bill = avg_time_bill()
                            if bill < 100:
                                print("----------------------------")
                                print("The Minimum Cart Value should not be less than 100 rupees!!")
                                print("Please add more items:")
                                print("----------------------------")
                            else:

                                drop_table()
                                payment_process(dist, delivery_charge, bill, time_avg, delivery_time)
                                promo1, promo2, flag_1 = Payment(delivery_charge, bill, email, obj2)
                                Tracking(time_avg, delivery_time, promo1, promo2, email, obj2)

                                break

                        elif button == 4:
                            flag = 1
                            drop_table()
                            print("Discarding the Order")
                            break

                        elif button == 5:
                            flag_wishlist == 1
                            res_obj.show_Haldiram()
                            create_table_wishlist()
                            q = order_input_wishlist()
                            Wishlist_summary(q, fetch_Haldiram)
                            print("Your Wishlist:")
                            show_wishlist()


                elif res_name == "BIKANERWALA":
                    res_obj.show_Bikaner()
                    create_table()
                    x, y = order_input()
                    order_summary(x, y, fetch_Bikaner)
                    time_avg, bill = avg_time_bill()
                    show_order()
                    while True:
                        Enter()
                        button = int(input())
                        if button == 1:
                            x = int(input("Enter the INDEX of ITEM you want to remove:"))
                            delete_item(x)
                            show_order()
                            time_avg, bill = avg_time_bill()

                        elif button == 2:
                            res_obj.show_Bikaner()
                            x, y = order_input()
                            order_summary(x, y, fetch_Bikaner)
                            show_order()
                            time_avg, bill = avg_time_bill()


                        elif button == 3:
                            time_avg, bill = avg_time_bill()
                            if bill < 100:
                                print("----------------------------")
                                print("The Minimum Cart Value should not be less than 100 rupees!!")
                                print("Please add more items:")
                                print("----------------------------")
                            else:

                                drop_table()
                                payment_process(dist, delivery_charge, bill, time_avg, delivery_time)
                                promo1, promo2, flag_1 = Payment(delivery_charge, bill, email, obj2)
                                Tracking(time_avg, delivery_time, promo1, promo2, email, obj2)
                                break


                        elif button == 4:
                            flag = 1
                            drop_table()
                            print("Discarding the Order")
                            break



                        elif button == 5:
                            flag_wishlist == 1
                            res_obj.show_Bikaner()
                            create_table_wishlist()
                            q = order_input_wishlist()
                            Wishlist_summary(q, fetch_Bikaner)
                            print("Your Wishlist:")
                            show_wishlist()

                elif res_name == "MONGINI-BAKERY":
                    res_obj.show_Mongini()
                    create_table()
                    x, y = order_input()
                    order_summary(x, y, fetch_Mongini)
                    time_avg, bill = avg_time_bill()
                    show_order()
                    while True:
                        Enter()
                        button = int(input())
                        if button == 1:
                            x = int(input("Enter the INDEX of ITEM you want to remove:"))
                            delete_item(x)
                            show_order()
                            time_avg, bill = avg_time_bill()

                        elif button == 2:
                            res_obj.show_Mongini()
                            x, y = order_input()
                            order_summary(x, y, fetch_Mongini)
                            show_order()
                            time_avg, bill = avg_time_bill()


                        elif button == 3:
                            time_avg, bill = avg_time_bill()
                            if bill < 100:
                                print("----------------------------")
                                print("The Minimum Cart Value should not be less than 100 rupees!!")
                                print("Please add more items:")
                                print("----------------------------")
                            else:

                                drop_table()
                                payment_process(dist, delivery_charge, bill, time_avg, delivery_time)
                                promo1, promo2, flag_1 = Payment(delivery_charge, bill, email, obj2)
                                Tracking(time_avg, delivery_time, promo1, promo2, email, obj2)
                                break


                        elif button == 4:
                            flag = 1
                            drop_table()
                            print("Discarding the Order")
                            break


                        elif button == 5:
                            flag_wishlist == 1
                            res_obj.show_Mongini()
                            create_table_wishlist()
                            q = order_input_wishlist()
                            Wishlist_summary(q, fetch_Mongini)
                            print("Your Wishlist:")
                            show_wishlist()



                elif res_name == "UDUPI":
                    res_obj.show_Udupi()
                    create_table()
                    x, y = order_input()
                    order_summary(x, y, fetch_Udupi)
                    time_avg, bill = avg_time_bill()
                    show_order()
                    while True:
                        Enter()
                        button = int(input())
                        if button == 1:
                            x = int(input("Enter the INDEX of ITEM you want to remove:"))
                            delete_item(x)
                            show_order()
                            time_avg, bill = avg_time_bill()

                        elif button == 2:
                            res_obj.show_Udupi()
                            x, y = order_input()
                            order_summary(x, y, fetch_Udupi)
                            show_order()
                            time_avg, bill = avg_time_bill()


                        elif button == 3:
                            time_avg, bill = avg_time_bill()
                            if bill < 100:
                                print("----------------------------")
                                print("The Minimum Cart Value should not be less than 100 rupees!!")
                                print("Please add more items:")
                                print("----------------------------")
                            else:

                                drop_table()
                                payment_process(dist, delivery_charge, bill, time_avg, delivery_time)
                                promo1, promo2, flag_1 = Payment(delivery_charge, bill, email, obj2)
                                Tracking(time_avg, delivery_time, promo1, promo2, email, obj2)
                                break


                        elif button == 4:
                            flag = 1
                            drop_table()
                            print("Discarding the Order")
                            break


                        elif button == 5:
                            flag_wishlist == 1
                            res_obj.show_Udupi()
                            create_table_wishlist()
                            q = order_input_wishlist()
                            Wishlist_summary(q, fetch_Udupi)
                            print("Your Wishlist:")
                            show_wishlist()

                elif res_name == "OM-SWEETS":

                    res_obj.show_Om()
                    create_table()
                    x, y = order_input()
                    order_summary(x, y, fetch_Om)
                    time_avg, bill = avg_time_bill()
                    show_order()
                    while True:
                        Enter()
                        button = int(input())
                        if button == 1:
                            x = int(input("Enter the INDEX of ITEM you want to remove:"))
                            delete_item(x)
                            show_order()
                            time_avg, bill = avg_time_bill()

                        elif button == 2:
                            res_obj.show_Om()
                            x, y = order_input()
                            order_summary(x, y, fetch_Om)
                            show_order()
                            time_avg, bill = avg_time_bill()


                        elif button == 3:
                            time_avg, bill = avg_time_bill()
                            if bill < 100:
                                print("----------------------------")
                                print("The Minimum Cart Value should not be less than 100 rupees!!")
                                print("Please add more items:")
                                print("----------------------------")
                            else:
                                drop_table()
                                payment_process(dist, delivery_charge, bill, time_avg, delivery_time)
                                promo1, promo2, flag_1 = Payment(delivery_charge, bill, email, obj2)
                                Tracking(time_avg, delivery_time, promo1, promo2, email,obj2)
                                break

                        elif button == 4:
                            flag = 1
                            drop_table()
                            print("Discarding the Order")
                            break

                        elif button == 5:
                            flag_wishlist == 1
                            res_obj.show_Om()
                            create_table_wishlist()

                            q = order_input_wishlist()
                            Wishlist_summary(q, fetch_Om)
                            print("Your Wishlist:")
                            show_wishlist()

                if flag == 1 or flag_1 == 1:
                    if flag_wishlist == 1:
                        drop_table_wishlist()
                    print("----------------------------")
                    print("Thanks For using the APP!!")
                    print("----------------------------")
                    break


            else:
                print("----------------------------")
                print("The User is not Registered!")
                print("----------------------------")
                break



        else:
            print("----------------------------")
            print("WRONG INPUT!!")
            print("----------------------------")
            break

