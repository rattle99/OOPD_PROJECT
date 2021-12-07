class Track_Order:

    def __init__(self):
        pass

    def rate(self):
        """Rate order.
        """

        x = int(input("On the Scale of 5 Please rate the FOOD and APP SERVICE: "))
        if x == 1 or x == 2:
            print("We are really sorry for the your Unpleasing Experience")
        elif x == 3:
            print("Thanks for the review, we'll keep improving.")
        elif x == 4 or x == 5:
            print("Thats Great!!, Hope to see you again.")

    def tracking(self, time_avg, delivery_time, promo1, promo2, email, obj):
        """Track order delivery.

        Args:
            time_avg (int): Time of order
            delivery_time (int): Delivery time
            promo1 (int): 1 or 0
            promo2 (int): 1 or 0
            email (str): User email
            obj ([type]): [description]
        """

        x = int(input("Enter the time elasped (in minutes): "))
        z = time_avg + delivery_time
        if x > (1.1 * z):
            print("Do you want to cancel your order:")
            print("1. YES")
            print("2. NO")
            y = int(input())
            if y == 1:
                print("Sorry for the inconvenience:")
                print("Your Order has been cancelled and if any amount is")
                print("debited from your account, it'll be refunded within")
                print("3 hours.")

                if promo1:
                    obj.update_promo1_to_0(email)
                elif promo2:
                    obj.update_promo2_to_0(email)
            else:
                print("Hope you enjoyed the food..")
                print("Kindly take two minutes to rate the APP:")
                self.rate()
                print("----------------------------")
        else:
            print("----------------------------")
            print("Hope you enjoyed the food..")
            print("Kindly take two minutes to rate the APP:")
            print("----------------------------")
            self.rate()
            print("----------------------------")
