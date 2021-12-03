# from Promocode import *

def payment_process(dist, delivery_charge, bill, time_avg, delivery_time):
    print(f"Distance between User and Restaurant:  {dist} KM ")
    print(f"Delivery Charges: Rs. {delivery_charge}")
    print(f"Bill Amount to be paid by the USER: Rs. {bill} ")
    print(f"Estimated time for Preparing the food: {time_avg} minutes")
    print(f"Approaximate time taken by delivery executive: {delivery_time} minutes")
    total_time = time_avg + delivery_time
    total_amount = bill + delivery_charge
    print(f"Estimated time for Delivery: {total_time} minutes ")
    print(f"Total Amount to be paid: Rs. {total_amount} ")
    print("--------------------------------------------------------")
    print("Proceeding forward for Payment:")
    print("----------------------------")

def Net_Banking(total):
    print("ThankYou For using NET BANKING:")
    print(f"INR {total} has been debited from your account.")
    print("ENJOY YOUR MEAL!")
def Bhim_upi(total):
    print("ThankYou For using BHIM UPI:")
    print(f"INR {total} has been debited from your account.")
    print("ENJOY YOUR MEAL!")
def Credit_Card(total):
    print("ThankYou For using CREDIT CARD services:")
    print(f"INR {total} has been debited from your card.")
    print("ENJOY YOUR MEAL!")
def Debit_Card(total):
    print("ThankYou For using DEBIT CARD:")
    print(f"INR {total} has been debited from your account.")
    print("ENJOY YOUR MEAL!")
def COD(total):
    print("ThankYou For the ORDER:")
    print(f"Please Pay INR {total} to the Delivery Executive.")
    print("ENJOY YOUR MEAL!")


def Payment(delivery_charge, bill, email, obj):
    promo1_used = False
    promo2_used = False
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
                    promo1_used = True
                    new_bill = bill - 20
                    obj.update_promo1_to_1(email)
                    break
            elif x == 2:
                z = obj.show_promo2(email)
                if z == 1:
                    print("Sorry You Already used this Promocode once:")
                else:
                    promo2_used = True
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
        Bhim_upi(total)
    elif pay == 2:
        Net_Banking(total)
    elif pay == 3:
        Credit_Card(total)
    elif pay == 4:
        Debit_Card(total)
    elif pay == 5:
        COD(total)

    flag_1 = 1
    return promo1_used, promo2_used, flag_1