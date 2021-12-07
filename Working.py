class Working:
    """Class for creation and handling order execution.
    """

    def __init__(self):
        self.flag = 0
        self.flag_1 = 0
        self.flag_wishlist = 0
        pass

    def worker_func(self, pay_obj, res_obj, order_obj, wish_obj,
                    track_obj, obj2, delivery_charge,
                    delivery_time, count, dist, email, res_name):
        """Create and execute order.

        Args:
            pay_obj ([type]): [description]
            res_obj (object): Object of class restaurant
            order_obj (object): Object of class Order
            wish_obj (object): Object of class Wishlist
            track_obj (object): Object of class Track_Order
            obj2 ([type]): [description]
            delivery_charge (int): Delivery charge in INR
            delivery_time (int): Delivery time in minutes
            count (int): [description]
            dist ([type]): [description]
            email (str): User email
            res_name (str): Restaurant name

        Returns:
            [type]: [description]
        """

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
                        print(
                            "The Minimum Cart Value should not be less than 100 rupees!!")
                        print("Please add more items:")
                        print("----------------------------")
                    else:
                        order_obj.drop_table()
                        pay_obj.payment_process(
                            dist, delivery_charge, bill, time_avg, delivery_time)
                        promo1, promo2, self.flag_1 = pay_obj.payment_final(
                            delivery_charge, bill, email, obj2)
                        track_obj.tracking(
                            time_avg, delivery_time, promo1, promo2, email, obj2)
                        break

                elif button == 4:
                    self.flag = 1
                    order_obj.drop_table()
                    print("Discarding the Order")
                    break

                elif button == 5:
                    self.flag_wishlist = 1
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
                        print(
                            "The Minimum Cart Value should not be less than 100 rupees!!")
                        print("Please add more items:")
                        print("----------------------------")
                    else:

                        order_obj.drop_table()
                        pay_obj.payment_process(
                            dist, delivery_charge, bill, time_avg, delivery_time)
                        promo1, promo2, self.flag_1 = pay_obj.payment_final(
                            delivery_charge, bill, email, obj2)
                        track_obj.tracking(
                            time_avg, delivery_time, promo1, promo2, email, obj2)

                        break

                elif button == 4:
                    self.flag = 1
                    order_obj.drop_table()
                    print("Discarding the Order")
                    break

                elif button == 5:
                    self.flag_wishlist = 1
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
                        print(
                            "The Minimum Cart Value should not be less than 100 rupees!!")
                        print("Please add more items:")
                        print("----------------------------")
                    else:

                        order_obj.drop_table()
                        pay_obj.payment_process(
                            dist, delivery_charge, bill, time_avg, delivery_time)
                        promo1, promo2, self.flag_1 = pay_obj.payment_final(
                            delivery_charge, bill, email, obj2)
                        track_obj.tracking(
                            time_avg, delivery_time, promo1, promo2, email, obj2)
                        break

                elif button == 4:
                    self.flag = 1
                    order_obj.drop_table()
                    print("Discarding the Order")
                    break

                elif button == 5:
                    self.flag_wishlist = 1
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
                        print(
                            "The Minimum Cart Value should not be less than 100 rupees!!")
                        print("Please add more items:")
                        print("----------------------------")
                    else:

                        order_obj.drop_table()
                        pay_obj.payment_process(
                            dist, delivery_charge, bill, time_avg, delivery_time)
                        promo1, promo2, self.flag_1 = pay_obj.payment_final(
                            delivery_charge, bill, email, obj2)
                        track_obj.tracking(
                            time_avg, delivery_time, promo1, promo2, email, obj2)
                        break

                elif button == 4:
                    self.flag = 1
                    order_obj.drop_table()
                    print("Discarding the Order")
                    break

                elif button == 5:
                    self.flag_wishlist = 1
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
                        print(
                            "The Minimum Cart Value should not be less than 100 rupees!!")
                        print("Please add more items:")
                        print("----------------------------")
                    else:

                        order_obj.drop_table()
                        pay_obj.payment_process(
                            dist, delivery_charge, bill, time_avg, delivery_time)
                        promo1, promo2, self.flag_1 = pay_obj.payment_final(
                            delivery_charge, bill, email, obj2)
                        track_obj.tracking(
                            time_avg, delivery_time, promo1, promo2, email, obj2)
                        break

                elif button == 4:
                    self.flag = 1
                    order_obj.drop_table()
                    print("Discarding the Order")
                    break

                elif button == 5:
                    self.flag_wishlist = 1
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
                        print(
                            "The Minimum Cart Value should not be less than 100 rupees!!")
                        print("Please add more items:")
                        print("----------------------------")
                    else:
                        order_obj.drop_table()
                        pay_obj.payment_process(
                            dist, delivery_charge, bill, time_avg, delivery_time)
                        promo1, promo2, self.flag_1 = pay_obj.payment_final(
                            delivery_charge, bill, email, obj2)
                        track_obj.tracking(
                            time_avg, delivery_time, promo1, promo2, email, obj2)
                        break

                elif button == 4:
                    self.flag = 1
                    order_obj.drop_table()
                    print("Discarding the Order")
                    break

                elif button == 5:
                    self.flag_wishlist = 1
                    res_obj.show_Om()
                    if count == 1:
                        wish_obj.create_table_wishlist()

                    q = wish_obj.order_input_wishlist()
                    wish_obj.Wishlist_summary(q, order_obj.fetch_Om)
                    print("Your Wishlist:")
                    wish_obj.show_wishlist()
                    count = count + 1

        return self.flag, self.flag_1, self.flag_wishlist
