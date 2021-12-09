# Food Ordering App
Implementation of Food ordering system using command line interface.

## Requirements:
1. python 3.8
2. pandas
3. sqlite3
4. geopy
5. tabulate

## Conditions:
1. While running the code all the code files and database files must be present in the same directory.
2. For Cart: Space separated input is to be given i.e "ITEM-Index" "Quantity" eg. 1 2 and for getting out of the cart press "0" and ENTER.
3. For Wishlist: Just the "ITEM-Index" and ENTER and for getting out of the wishlist section press "0" and ENTER.

### Database Used:
1. User.db (STATIC)
2. Restaurents.db (STATIC)
3. Orders.db (DYNAMIC)

### Classes Used:
**1. User:**<br>
   **It's Methods:**<br>
   User_Verification(), User_Authentication()<br>
   add_one(), lat_lon_user()<br>

**2. Promocode:  (Inherits User class)** <br>
   **It's Methods:**<br>
   update_promo1_to_1(), update_promo1_to_0()<br>
   update_promo2_to_1(), update_promo2_to_0()<br>
   show_promo1(), show_promo2()<br>


**3. Restaurant:**<br>
   **It's Methods:**<br>
   show_all(), read_one(), show_kolkata(), show_Haldiram()<br>
   show_Bikaner(), show_Mongini(), show_Udupi(), show_Om()<br>

**4. Payment:**<br>
   **It's Methods:**<br>
   payment_process(), Net_Banking(), Bhim_upi()<br>
   Credit_Card(), Debit_Card(), COD(), payment_final() <br>  

**5. Order:**<br>
   **It's Methods:**<br>
   order_input(), create_table(), fetch_kolkata(), fetch_Haldiram()<br>
   fetch_Bikaner(), fetch_Mongini(), fetch_Udupi()<br>
   fetch_Om(), Add(), drop_table(), show_order()<br>
   order_summary(), avg_time_bill(), delete_item(), Enter()<br>
 
**6. Track_Order:**<br>
   **It's Methods:**<br>
   rate(), tracking()<br>
 
**7. Wishlist:**<br>
   **It's Methods:**<br>
   order_input_wishlist(), create_table_wishlist(), Add_wishlist()<br>
   drop_table_wishlist(), show_wishlist(), Wishlist_summary()<br>

**8. Working:**<br>
   **It's Methods:**<br>
   worker_func()<br>
