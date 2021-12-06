from geopy.distance import great_circle
import Restaurent
import User
import Payment
import Wishlist
import Order
import Tracking
import Working


if __name__ == "__main__":
    while True:
        print("WELCOME TO THE APPLICATION:")
        print("FOR REGISTRATION PRESS 1:")
        print("FOR LOGIN PRESS 2:")
        count = 1
        delivery_charge = 0
        delivery_time = 0
        x = int(input())

        if x == 1:
            # Use of Inheritance
            obj1 = User.Promocode()
            name, surname, email, password, lat, lon = obj1.User_Registration()

            if obj1.User_Verification(email):
                print("The Entered Email ID is already Registered!")
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
                elif dist > 10 and dist <= 16:
                    delivery_charge = 50
                    delivery_time = 30
                elif dist > 16:
                    delivery_charge = 70
                    delivery_time = 50

                # Object of Working Class:
                work_obj = Working.Working()
                flag, flag_1, flag_wishlist = work_obj.worker_func(pay_obj, res_obj, order_obj, wish_obj,track_obj, obj2,
                                                                   delivery_charge,delivery_time, count, dist, email, res_name)


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

