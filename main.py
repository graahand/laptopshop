import functions
import read
from read import begin
import write

# Read input dictionary
input_Dict = read.begin()

# Call hello function
functions.hello()

# Set the continuation loop flag to True
continuation_loop = True

# Main loop for program execution
while continuation_loop:
    print("1. For selling")
    print("2. For Buying")
    print("3. For exiting")
    print("\n")
    print("----------------------------------------------------------")

    # Set the exception loop flag to True
    except_loop = True
    while except_loop:
        try:
            # Get user input for selected option
            input_user = int(input("Enter from above option: "))
            except_loop = False
        except:
            print("Enter from only given options")

    if input_user == 1:
        # Initialize customer dictionary
        customer_Dict = {}

        # Call laptop_details function
        functions.laptop_details()

        # Read name and customer number from input
        name, customer_number = read.name_number()

        # Validate product ID for selling
        validated_ID = functions.sell_validID()

        # Validate quantity for selling
        user_qtty = functions.sell_valid_quantity()

        # Update sell file with validated ID and quantity
        functions.sell_file_update(validated_ID, user_qtty)

        # Get product details for the validated ID
        # converted to a string because it is being used in a string concatenation operation.
        name_of_product = str(input_Dict[validated_ID][0])
        laptop_brand = str(input_Dict[validated_ID][1])
        users_qty = str(user_qtty)
        price_per_unit = str(input_Dict[validated_ID][2])
        item_markedprice = str(input_Dict[validated_ID][2].replace("$",''))
        user_amount = str(int(item_markedprice) * int(users_qty))
        total_amount = str(float(int(user_amount)))
        delivery_cost = 0

        # Update customer dictionary with product details
        customer_Dict = [name_of_product, laptop_brand, users_qty, price_per_unit, item_markedprice, user_amount, total_amount]

        # Check if user wants to place another order
        next_purchase = input("\n Dear user do you want to order more? (y/n) \n").lower()
        if next_purchase == "y":
            next_order = True
            while next_order:
                # Validate product ID for selling
                validated_ID = functions.sell_validID()

                # Validate quantity for selling
                user_qtty = functions.sell_valid_quantity()

                # Update sell file with validated ID and quantity
                functions.sell_file_update(validated_ID, user_qtty)

                # Get delivery preference from user
                delivery = input("\n Dear user do you want your laptop to be shipped? (y/n)").lower()

                # Write delivery details to file
                write.delivery_yes(name_of_product, laptop_brand, users_qty, price_per_unit, user_amount, total_amount, name, customer_number, delivery, delivery_cost)

                # Call functions for second laptop
                functions.secondlaptop_konsole(validated_ID, user_qtty, name)
                functions.second_laptop(validated_ID, user_qtty, name)

                next_order = False

        elif next_purchase == "n":
            # Get delivery preference from user
            delivery = input("\n Dear user do you want your laptop to be shipped? (y/n)").lower()

            # Write delivery details to file
            write.delivery_yes(name_of_product, laptop_brand, users_qty, price_per_unit, user_amount, total_amount, name, customer_number, delivery, delivery_cost)

            next_order = False

        else:
            print("--------------------------------------------------------------------------------------------")
            print("                           Please give the appropriate value.")
            print("--------------------------------------------------------------------------------------------")
           
    elif input_user == 2:
        # Initialize customer dictionary
        customer_Dict = {}

        # Call laptop_details function
        functions.laptop_details()

        # Read dealer name and contact from input
        dealer_name, dealer_contact = read.d_name_contact()

        # Validate product ID for buying
        validated_ID = functions.validID()

        # Validate quantity for buying
        user_qtty = functions.valid_quantity()

        # Update buy file with validated ID and quantity
        functions.file_update(validated_ID, user_qtty)

        # Get product details for the validated ID
        name_of_product = input_Dict[validated_ID][0]
        laptop_brand = input_Dict[validated_ID][1]
        users_qty = user_qtty
        price_per_unit = input_Dict[validated_ID][2]
        item_markedprice = int(input_Dict[validated_ID][2].replace("$", ''))
        user_amount = int(item_markedprice) * int(users_qty)
        vat_total_price = float(int(user_amount) + (0.13) * (int(user_amount)))

        # Update customer dictionary with product details
        customer_Dict = [name_of_product, laptop_brand, users_qty, price_per_unit, item_markedprice, user_amount, vat_total_price]

        # Check if user wants to place another order
        next_purchase = input("\n Dear user do you want to order more? (y/n) \n").lower()
        if next_purchase == "y":
            next_order = True
            while next_order:
                # Validate product ID for buying
                validated_ID = functions.validID()

                # Validate quantity for buying
                user_qtty = functions.valid_quantity()

                # Update buy file with validated ID and quantity
                functions.file_update(validated_ID, user_qtty)

                # Write order bill
                write.order_bill(name_of_product, laptop_brand, users_qty, price_per_unit, user_amount, vat_total_price, dealer_name, dealer_contact)

                # Call functions for dealer's second laptop
                functions.dealer_second_laptop(validated_ID, user_qtty, dealer_name)
                functions.dealer_secondlaptop_konsole(validated_ID, user_qtty, dealer_name)

                next_order = False

        elif next_purchase == "n":
            # Write order bill
            write.order_bill(name_of_product, laptop_brand, users_qty, price_per_unit, user_amount, vat_total_price, dealer_name, dealer_contact)

            next_order = False

        else:
            print("--------------------------------------------------------------------------------------------")
            print("                           Please give the appropriate value.")
            print("--------------------------------------------------------------------------------------------")

    elif input_user == 3:
            print("Dhanyabadh, For choosing us.")
            continuation_loop = False
name_of_product, laptop_brand, users_qty, price_per_unit, user_amount, total_amount, name, customer_number, delivery, delivery_cost