from geopy.distance import great_circle
import Restaurent
import User
import Payment
import Wishlist
import Order
import Tracking


if __name__ == "__main__":
    while True:
        print("WELCOME TO THE APPLICATION:")
        print("FOR REGISTRATION PRESS 1:")
        print("FOR LOGIN PRESS 2:")
        count = 1
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
                # Object of Payment Class
                pay_obj = Payment.Payment()
                # Object of Restaurant Class
                res_obj = Restaurent.Restaurant()
                # Object of Order Class
                order_obj = Order.Order()
                # Object of Wishlist Class
                wish_obj = Wishlist.Wishlist()
                # Object of Track_Order Class
                track_obj = Tracking.Track_Order()

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
                    order_obj.create_table()
                    x, y = order_obj.order_input()
                    order_obj.order_summary(x, y, order_obj.fetch_kolkata)
                    time_avg, bill = order_obj.avg_time_bill()
                    print("Your ORDER:")
                    order_obj.show_order()
                    while True:
                        order_obj.Enter()
                        button = int(input())
                        if button == 1:
                            x = int(input("Enter the INDEX of ITEM you want to remove:"))
                            order_obj.delete_item(x)
                            print("Your ORDER:")
                            order_obj.show_order()
                            time_avg, bill = order_obj.avg_time_bill()

                        elif button == 2:
                            res_obj.show_kolkata()
                            x, y = order_obj.order_input()
                            order_obj.order_summary(x, y, order_obj.fetch_kolkata)
                            print("Your ORDER:")
                            order_obj.show_order()
                            time_avg, bill = order_obj.avg_time_bill()


                        elif button == 3:
                            time_avg, bill = order_obj.avg_time_bill()
                            if bill < 100:
                                print("----------------------------")
                                print("The Minimum Cart Value should not be less than 100 rupees!!")
                                print("Please add more items:")
                                print("----------------------------")
                            else:
                                order_obj.drop_table()
                                pay_obj.payment_process(dist, delivery_charge, bill, time_avg, delivery_time)
                                promo1, promo2, flag_1 = pay_obj.payment_final(delivery_charge, bill, email, obj2)
                                track_obj.tracking(time_avg, delivery_time, promo1, promo2, email, obj2)
                                break


                        elif button == 4:
                            flag = 1
                            order_obj.drop_table()
                            print("Discarding the Order")
                            break


                        elif button == 5:
                            flag_wishlist = 1
                            res_obj.show_kolkata()
                            if count == 1:
                                wish_obj.create_table_wishlist()
                            q = wish_obj.order_input_wishlist()
                            wish_obj.Wishlist_summary(q, order_obj.fetch_kolkata)
                            print("Your Wishlist:")
                            wish_obj.show_wishlist()
                            count = count + 1


                elif res_name == "HALDIRAMS":
                    res_obj.show_Haldiram()
                    order_obj.create_table()
                    x, y = order_obj.order_input()
                    order_obj.order_summary(x, y, order_obj.fetch_Haldiram)
                    time_avg, bill = order_obj.avg_time_bill()
                    print("Your ORDER:")
                    order_obj.show_order()
                    while True:
                        order_obj.Enter()
                        button = int(input())
                        if button == 1:
                            x = int(input("Enter the INDEX of ITEM you want to remove:"))
                            order_obj.delete_item(x)
                            print("Your ORDER:")
                            order_obj.show_order()
                            time_avg, bill = order_obj.avg_time_bill()

                        elif button == 2:
                            res_obj.show_Haldiram()
                            x, y = order_obj.order_input()
                            order_obj.order_summary(x, y, order_obj.fetch_Haldiram)
                            print("Your ORDER:")
                            order_obj.show_order()
                            time_avg, bill = order_obj.avg_time_bill()


                        elif button == 3:
                            time_avg, bill = order_obj.avg_time_bill()
                            if bill < 100:
                                print("----------------------------")
                                print("The Minimum Cart Value should not be less than 100 rupees!!")
                                print("Please add more items:")
                                print("----------------------------")
                            else:

                                order_obj.drop_table()
                                pay_obj.payment_process(dist, delivery_charge, bill, time_avg, delivery_time)
                                promo1, promo2, flag_1 = pay_obj.payment_final(delivery_charge, bill, email, obj2)
                                track_obj.tracking(time_avg, delivery_time, promo1, promo2, email, obj2)

                                break

                        elif button == 4:
                            flag = 1
                            order_obj.drop_table()
                            print("Discarding the Order")
                            break

                        elif button == 5:
                            flag_wishlist = 1
                            res_obj.show_Haldiram()
                            if count == 1:
                                wish_obj.create_table_wishlist()
                            q = wish_obj.order_input_wishlist()
                            wish_obj.Wishlist_summary(q, order_obj.fetch_Haldiram)
                            print("Your Wishlist:")
                            wish_obj.show_wishlist()
                            count = count + 1


                elif res_name == "BIKANERWALA":
                    res_obj.show_Bikaner()
                    order_obj.create_table()
                    x, y = order_obj.order_input()
                    order_obj.order_summary(x, y, order_obj.fetch_Bikaner)
                    time_avg, bill = order_obj.avg_time_bill()
                    print("Your ORDER:")
                    order_obj.show_order()
                    while True:
                        order_obj.Enter()
                        button = int(input())
                        if button == 1:
                            x = int(input("Enter the INDEX of ITEM you want to remove:"))
                            order_obj.delete_item(x)
                            print("Your ORDER:")
                            order_obj.show_order()
                            time_avg, bill = order_obj.avg_time_bill()

                        elif button == 2:
                            res_obj.show_Bikaner()
                            x, y = order_obj.order_input()
                            order_obj.order_summary(x, y, order_obj.fetch_Bikaner)
                            print("Your ORDER:")
                            order_obj.show_order()
                            time_avg, bill = order_obj.avg_time_bill()


                        elif button == 3:
                            time_avg, bill = order_obj.avg_time_bill()
                            if bill < 100:
                                print("----------------------------")
                                print("The Minimum Cart Value should not be less than 100 rupees!!")
                                print("Please add more items:")
                                print("----------------------------")
                            else:

                                order_obj.drop_table()
                                pay_obj.payment_process(dist, delivery_charge, bill, time_avg, delivery_time)
                                promo1, promo2, flag_1 = pay_obj.payment_final(delivery_charge, bill, email, obj2)
                                track_obj.tracking(time_avg, delivery_time, promo1, promo2, email, obj2)
                                break


                        elif button == 4:
                            flag = 1
                            order_obj.drop_table()
                            print("Discarding the Order")
                            break



                        elif button == 5:
                            flag_wishlist = 1
                            res_obj.show_Bikaner()
                            if count == 1:
                                wish_obj.create_table_wishlist()
                            q = wish_obj.order_input_wishlist()
                            wish_obj.Wishlist_summary(q, order_obj.fetch_Bikaner)
                            print("Your Wishlist:")
                            wish_obj.show_wishlist()
                            count = count + 1

                elif res_name == "MONGINI-BAKERY":
                    res_obj.show_Mongini()
                    order_obj.create_table()
                    x, y = order_obj.order_input()
                    order_obj.order_summary(x, y, order_obj.fetch_Mongini)
                    time_avg, bill = order_obj.avg_time_bill()
                    print("Your ORDER:")
                    order_obj.show_order()
                    while True:
                        order_obj.Enter()
                        button = int(input())
                        if button == 1:
                            x = int(input("Enter the INDEX of ITEM you want to remove:"))
                            order_obj.delete_item(x)
                            print("Your ORDER:")
                            order_obj.show_order()
                            time_avg, bill = order_obj.avg_time_bill()

                        elif button == 2:
                            res_obj.show_Mongini()
                            x, y = order_obj.order_input()
                            order_obj.order_summary(x, y, order_obj.fetch_Mongini)
                            print("Your ORDER:")
                            order_obj.show_order()
                            time_avg, bill = order_obj.avg_time_bill()


                        elif button == 3:
                            time_avg, bill = order_obj.avg_time_bill()
                            if bill < 100:
                                print("----------------------------")
                                print("The Minimum Cart Value should not be less than 100 rupees!!")
                                print("Please add more items:")
                                print("----------------------------")
                            else:

                                order_obj.drop_table()
                                pay_obj.payment_process(dist, delivery_charge, bill, time_avg, delivery_time)
                                promo1, promo2, flag_1 = pay_obj.payment_final(delivery_charge, bill, email, obj2)
                                track_obj.tracking(time_avg, delivery_time, promo1, promo2, email, obj2)
                                break


                        elif button == 4:
                            flag = 1
                            order_obj.drop_table()
                            print("Discarding the Order")
                            break


                        elif button == 5:
                            flag_wishlist = 1
                            res_obj.show_Mongini()
                            if count == 1:
                                wish_obj.create_table_wishlist()
                            q = wish_obj.order_input_wishlist()
                            wish_obj.Wishlist_summary(q, order_obj.fetch_Mongini)
                            print("Your Wishlist:")
                            wish_obj.show_wishlist()
                            count = count + 1



                elif res_name == "UDUPI":
                    res_obj.show_Udupi()
                    order_obj.create_table()
                    x, y = order_obj.order_input()
                    order_obj.order_summary(x, y, order_obj.fetch_Udupi)
                    time_avg, bill = order_obj.avg_time_bill()
                    print("Your ORDER:")
                    order_obj.show_order()
                    while True:
                        order_obj.Enter()
                        button = int(input())
                        if button == 1:
                            x = int(input("Enter the INDEX of ITEM you want to remove:"))
                            order_obj.delete_item(x)
                            print("Your ORDER:")
                            order_obj.show_order()
                            time_avg, bill = order_obj.avg_time_bill()

                        elif button == 2:
                            res_obj.show_Udupi()
                            x, y = order_obj.order_input()
                            order_obj.order_summary(x, y, order_obj.fetch_Udupi)
                            print("Your ORDER:")
                            order_obj.show_order()
                            time_avg, bill = order_obj.avg_time_bill()


                        elif button == 3:
                            time_avg, bill = order_obj.avg_time_bill()
                            if bill < 100:
                                print("----------------------------")
                                print("The Minimum Cart Value should not be less than 100 rupees!!")
                                print("Please add more items:")
                                print("----------------------------")
                            else:

                                order_obj.drop_table()
                                pay_obj.payment_process(dist, delivery_charge, bill, time_avg, delivery_time)
                                promo1, promo2, flag_1 = pay_obj.payment_final(delivery_charge, bill, email, obj2)
                                track_obj.tracking(time_avg, delivery_time, promo1, promo2, email, obj2)
                                break


                        elif button == 4:
                            flag = 1
                            order_obj.drop_table()
                            print("Discarding the Order")
                            break


                        elif button == 5:
                            flag_wishlist = 1
                            res_obj.show_Udupi()
                            if count == 1:
                                wish_obj.create_table_wishlist()
                            q = wish_obj.order_input_wishlist()
                            wish_obj.Wishlist_summary(q, order_obj.fetch_Udupi)
                            print("Your Wishlist:")
                            wish_obj.show_wishlist()
                            count = count + 1

                elif res_name == "OM-SWEETS":

                    res_obj.show_Om()
                    order_obj.create_table()
                    x, y = order_obj.order_input()
                    order_obj.order_summary(x, y, order_obj.fetch_Om)
                    time_avg, bill = order_obj.avg_time_bill()
                    print("Your ORDER:")
                    order_obj.show_order()
                    while True:
                        order_obj.Enter()
                        button = int(input())
                        if button == 1:
                            x = int(input("Enter the INDEX of ITEM you want to remove:"))
                            order_obj.delete_item(x)
                            print("Your ORDER:")
                            order_obj.show_order()
                            time_avg, bill = order_obj.avg_time_bill()

                        elif button == 2:
                            res_obj.show_Om()
                            x, y = order_obj.order_input()
                            order_obj.order_summary(x, y, order_obj.fetch_Om)
                            print("Your ORDER:")
                            order_obj.show_order()
                            time_avg, bill = order_obj.avg_time_bill()


                        elif button == 3:
                            time_avg, bill = order_obj.avg_time_bill()
                            if bill < 100:
                                print("----------------------------")
                                print("The Minimum Cart Value should not be less than 100 rupees!!")
                                print("Please add more items:")
                                print("----------------------------")
                            else:
                                order_obj.drop_table()
                                pay_obj.payment_process(dist, delivery_charge, bill, time_avg, delivery_time)
                                promo1, promo2, flag_1 = pay_obj.payment_final(delivery_charge, bill, email, obj2)
                                track_obj.tracking(time_avg, delivery_time, promo1, promo2, email,obj2)
                                break

                        elif button == 4:
                            flag = 1
                            order_obj.drop_table()
                            print("Discarding the Order")
                            break

                        elif button == 5:
                            flag_wishlist = 1
                            res_obj.show_Om()
                            if count == 1:
                                wish_obj.create_table_wishlist()

                            q = wish_obj.order_input_wishlist()
                            wish_obj.Wishlist_summary(q, order_obj.fetch_Om)
                            print("Your Wishlist:")
                            wish_obj.show_wishlist()
                            count = count + 1

                if flag == 1 or flag_1 == 1:
                    if flag_wishlist == 1:
                        wish_obj.drop_table_wishlist()
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

