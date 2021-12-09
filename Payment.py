class Payment:
    """Class for handling payments
    """

    def __init__(self):
        self.flag_1 = 1

    def payment_process(self, dist, delivery_charge, bill, time_avg, delivery_time):
        """Print final invoice generated with details

        Args:
            dist (float): Distance b/w user and restaurant in KM
            delivery_charge (int): Delivery charges in INR
            bill (int): Bill amount in INR
            time_avg (int): Time in minutes
            delivery_time (int): Delivery time in minutes
        """

        print(f"Distance between User and Restaurant:  {dist} KM ")
        print(f"Delivery Charges: Rs. {delivery_charge}")
        print(f"Bill Amount to be paid by the USER: Rs. {bill} ")
        print(f"Estimated time for Preparing the food: {time_avg} minutes")
        print(
            f"Approaximate time taken by delivery executive: {delivery_time} minutes")
        total_time = time_avg + delivery_time
        total_amount = bill + delivery_charge
        print(f"Estimated time for Delivery: {total_time} minutes ")
        print(f"Total Amount to be paid: Rs. {total_amount} ")
        print("--------------------------------------------------------")
        print("Proceeding forward for Payment:")
        print("----------------------------")

    def Net_Banking(self, total):
        """Execute Net Banking for payment

        Args:
            total (int): Total amount in INR
        """

        print("ThankYou For using NET BANKING:")
        print(f"INR {total} has been debited from your account.")
        print("ENJOY YOUR MEAL!")

    def Bhim_upi(self, total):
        """Execute BHIM UPI for payment

        Args:
            total (int): Total amount in INR
        """

        print("ThankYou For using BHIM UPI:")
        print(f"INR {total} has been debited from your account.")
        print("ENJOY YOUR MEAL!")

    def Credit_Card(self, total):
        """Execute Credit Card for payment

        Args:
            total (int): Total amount in INR
        """

        print("ThankYou For using CREDIT CARD services:")
        print(f"INR {total} has been debited from your card.")
        print("ENJOY YOUR MEAL!")

    def Debit_Card(self, total):
        """Execute Debit Card for payment

        Args:
            total (int): Total amount in INR
        """

        print("ThankYou For using DEBIT CARD:")
        print(f"INR {total} has been debited from your account.")
        print("ENJOY YOUR MEAL!")

    def COD(self, total):
        """Execute COD for payment

        Args:
            total (int): Total amount in INR
        """

        print("ThankYou For the ORDER:")
        print(f"Please Pay INR {total} to the Delivery Executive.")
        print("ENJOY YOUR MEAL!")

    def payment_final(self, delivery_charge, bill, email, obj):
        """Finalise payment for order

        Args:
            delivery_charge (int): Delivery charges in INR
            bill (int): Bill amount in INR
            email (str): User email
            obj (object): Object of type Promocode

        Returns:
            bool: Boolean value True if promo1 used
            bool: Boolean value False if promo2 used
            bool: Boolean value for flag_1
        """

        self.promo1_used = False
        self.promo2_used = False
        if obj.show_promo1(email) == 1 and obj.show_promo2(email) == 1:
            new_bill = bill
            print("Sorry You Don't Have any Promocodes Left:")
        else:

            while True:
                print("Select the Promocode you would like to use:")
                print("1. SAVE20")
                print("2. SAVE50")
                x = int(input())
                if x == 1:
                    z = obj.show_promo1(email)
                    if z == 1:
                        print("Sorry You Already used this Promocode once:")
                    else:
                        self.promo1_used = True
                        new_bill = bill - 20
                        obj.update_promo1_to_1(email)
                        break
                elif x == 2:
                    z = obj.show_promo2(email)
                    if z == 1:
                        print("Sorry You Already used this Promocode once:")
                    else:
                        self.promo2_used = True
                        new_bill = bill - 50
                        obj.update_promo2_to_1(email)
                        break

        total = new_bill + delivery_charge
        print(f"Final Bill: Rs. {new_bill}")
        print(f"Delivery Charges: Rs. {delivery_charge}")
        print(f"Total Amount to be Paid: Rs. {total}")
        print("----------------------------------------")
        print("Select the Payment Method:")
        print("1. BHIM UPI")
        print("2. NET BANKING")
        print("3. CREDIT CARD")
        print("4. DEBIT CARD")
        print("5. CASH ON DELIVERY")
        pay = int(input())
        if pay == 1:
            self.Bhim_upi(total)
        elif pay == 2:
            self.Net_Banking(total)
        elif pay == 3:
            self.Credit_Card(total)
        elif pay == 4:
            self.Debit_Card(total)
        elif pay == 5:
            self.COD(total)

        return self.promo1_used, self.promo2_used, self.flag_1
