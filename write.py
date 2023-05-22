import datetime

# Function to generate a bill for a customer who opts for delivery
def delivery_yes(name_of_product, laptop_brand, users_qty, price_per_unit, user_amount, total_amount, name, customer_number, delivery, delivery_cost):
    # Check if delivery option is selected
    if delivery == "y":
        delivery_cost = 100  # Set delivery cost to $100
        total_amount = str(float(total_amount) + delivery_cost)  # Add delivery cost to the total amount

        # Print bill header
        print("\n")
        print("*********************************************************")
        print("           ITEM HAS BEEN SUCCESSFULLY SOLD")
        print("*********************************************************")
        print("\n \n Your Bill is printed below")
        print("\n")

        date_time = datetime.datetime.now()  # Get current date and time

        # Print bill details in console
        print("\n\n\n-----------------------------------------------------------------------------------------------------------------------")
        print("                                                      Bill of Sale")
        print("-----------------------------------------------------------------------------------------------------------------------")
        print("                                                     Manix Store\n")
        print("                                                    Dhobidhara marg")
        print("-----------------------------------------------------------------------------------------------------------------------\n")
        print("\n CUSTOMER DETAILS:")
        print("-------------------------")
        print(" Date: " + str(date_time))
        print(" Name: " + name)
        print(" Contact customer_number: " + customer_number)
        print("-------------------------")
        print("\n")
        print("Your order:")
        print("-----------------------------------------------------------------------------------------------------------------------")
        print("Laptop Name \t\t laptop_brand \t\t Quantity \t\t Unit Price \t\t Net user_amount \t Total user_amount")
        print("-----------------------------------------------------------------------------------------------------------------------\n")
        print(name_of_product + " \t\t " + laptop_brand + " \t\t " + str(users_qty) + " \t\t " + str(price_per_unit) + " \t\t " + str(user_amount) + " \t\t " + total_amount)
        print("-----------------------------------------------------------------------------------------------------------------------\n")

        filename = str(name) + ".txt"
        with open(filename, 'w') as sell:
            # Write bill details to file
            sell.write("\n\n\n-----------------------------------------------------------------------------------------------------------------------\n")
            sell.write("                                                          Bill of Sale\n")
            sell.write("-----------------------------------------------------------------------------------------------------------------------\n")
            sell.write("                                                         Manix Store\n")
            sell.write("                                                        Dhobidhara marg\n")
            sell.write("-----------------------------------------------------------------------------------------------------------------------\n\n")
            sell.write("-------------------------")
            sell.write("\n CUSTOMER DETAILS:")
            sell.write("\n Date: " + str(date_time))
            sell.write("\n Name of customer: " + name + "\n")
            sell.write("Phone customer_number of customer: " + customer_number + "\n")
            sell.write("-------------------------")
            sell.write("\n\n")
            sell.write("Your order:\n")
            sell.write("-----------------------------------------------------------------------------------------------------------------------")
            sell.write("\nProduct name \t\t laptop_brand \t\t Quantity \t\t Unit Price \t\t Net user_amount \t Total user_amount\n")
            sell.write("-----------------------------------------------------------------------------------------------------------------------\n")
            sell.write(name_of_product + " \t\t " + laptop_brand + " \t\t " + str(users_qty) + " \t\t " + str(price_per_unit) + " \t\t " + str(user_amount) + " \t\t " + total_amount + "\n")
            sell.write("-----------------------------------------------------------------------------------------------------------------------")

# Function to generate a bill for a customer who opts not to have delivery
def delivery_no(name_of_product, laptop_brand, users_qty, price_per_unit, user_amount, total_amount, name, customer_number, delivery):
    if delivery == "n":
        print("\n")
        print("*********************************************************")
        print("           ITEM HAS BEEN SUCCESSFULLY SOLD")
        print("*********************************************************")
        print("\n \n Your Bill is printed below:")
        print("\n")

        date_time = datetime.datetime.now()  # Get current date and time

        # Print bill details in console
        print("\n\n\n-----------------------------------------------------------------------------------------------------------------------")
        print("                                                      Bill of Sale")
        print("-----------------------------------------------------------------------------------------------------------------------")
        print("                                                     BibekShil Laptop Heaven\n")
        print("                                                    Manigram")
        print("-----------------------------------------------------------------------------------------------------------------------\n")
        print("\n CUSTOMER DETAILS:")
        print("-------------------------")
        print(" Date: " + str(date_time))
        print(" Name: " + name)
        print(" Contact customer_number: " + customer_number)
        print("-------------------------")
        print("\n")
        print("Your order:")
        print("-----------------------------------------------------------------------------------------------------------------------")
        print("Laptop Name \t\t laptop_brand \t\t Quantity \t\t Unit Price \t\t Net user_amount \t Total user_amount")
        print("-----------------------------------------------------------------------------------------------------------------------")
        print(name_of_product + " \t\t " + laptop_brand + " \t\t " + str(users_qty) + " \t\t " + str(price_per_unit) + " \t\t " + str(user_amount) + " \t\t " + total_amount)
        print("-----------------------------------------------------------------------------------------------------------------------")

        filename = str(name) + ".txt"
        with open(filename, 'w') as sell:
            # Write bill details to file
            sell.write("\n\n\n-----------------------------------------------------------------------------------------------------------------------\n")
            sell.write("                                                          Bill of Sale\n")
            sell.write("-----------------------------------------------------------------------------------------------------------------------\n")
            sell.write("                                                         BibekShil Laptop Heaven\n")
            sell.write("                                                        Manigram \n")
            sell.write("-----------------------------------------------------------------------------------------------------------------------\n\n")
            sell.write("-------------------------")
            sell.write("\n CUSTOMER DETAILS:")
            sell.write("\n Date: " + str(date_time))
            sell.write("\n Name of customer: " + name + "\n")
            sell.write(" Phone customer_number of customer: " + customer_number + "\n")
            sell.write("-------------------------")
            sell.write("\n\n")
            sell.write("Your order:\n")
            sell.write("-----------------------------------------------------------------------------------------------------------------------")
            sell.write("\nProduct name \t\t laptop_brand \t\t Quantity \t\t Unit Price \t\t Net user_amount \t Total user_amount\n")
            sell.write("-----------------------------------------------------------------------------------------------------------------------\n")
            sell.write(name_of_product + " \t\t " + laptop_brand + " \t\t " + str(users_qty) + " \t\t " + str(price_per_unit) + " \t\t " + str(user_amount) + " \t\t " + total_amount + "\n")
            sell.write("-----------------------------------------------------------------------------------------------------------------------")


# Function to generate a bill for an order placed by a dealer
def order_bill(name_of_product, laptop_brand, users_qty, price_per_unit, user_amount, vat_total_price, dealer_name, dealer_contact):
    print("\n")
    print("---------------------------------------------------------")
    print("           ITEM HAS BEEN SUCCESSFULLY RESTOCKED")
    print("---------------------------------------------------------")
    print("\n")
    print("\n")

    date_time = datetime.datetime.now()  # Get current date and time
        # Print order details in console
    print("\n\n\n-----------------------------------------------------------------------------------------------------------------------")
    print("                                                          Bill of Order")
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("                                                          BibekShil Laptop Heaven\n")
    print("                                                        Manigram")
    print("-----------------------------------------------------------------------------------------------------------------------\n")
    print("-------------------------")
    print(" DEALER DETAILS:")
    print(" Date: " + str(date_time))
    print(" Name of dealer: " + dealer_name)
    print(" Phone customer_number of dealer: " + dealer_contact)
    print("-------------------------")
    print("\n")
    print("Your order:")
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("Laptop Name \t\t laptop_brand \t\t Quantity \t\t Unit Price \t\t Net user_amount \t Total user_amount")
    print("-----------------------------------------------------------------------------------------------------------------------")
    print(name_of_product + " \t\t " + laptop_brand + " \t\t " + str(users_qty) + " \t\t " + str(price_per_unit) + " \t\t " + str(user_amount) + " \t\t " + str(vat_total_price))
    print("-----------------------------------------------------------------------------------------------------------------------\n\n")

    filename = str(dealer_name) + ".txt"
    with open(filename, 'w') as order:
        # Write order details to file
        order.write("\n\n\n-----------------------------------------------------------------------------------------------------------------------\n")
        order.write("                                                          Bill of Order\n")
        order.write("-----------------------------------------------------------------------------------------------------------------------\n")
        order.write("                                                         BibekShil Laptop Heaven\n")
        order.write("                                                        Tilottama\n")
        order.write("-----------------------------------------------------------------------------------------------------------------------\n\n")
        order.write("-------------------------")
        order.write("\n DEALER DETAILS:")
        order.write("\n Date: " + str(date_time))
        order.write("\n Name: " + dealer_name + "\n")
        order.write(" Phone customer_number: " + dealer_contact + "\n")
        order.write("-------------------------")
        order.write("\n\n")
        order.write("Your order:\n")
        order.write("-----------------------------------------------------------------------------------------------------------------------")
        order.write("\nProduct name \t\t laptop_brand \t\t Quantity \t\t Unit Price \t\t Net user_amount \t Total user_amount\n")
        order.write("-----------------------------------------------------------------------------------------------------------------------\n")
        order.write(name_of_product + " \t\t " + laptop_brand + " \t\t " + str(users_qty) + " \t\t " + str(price_per_unit) + " \t\t " + str(user_amount) + " \t\t " + str(vat_total_price) + "\n")
        order.write("-----------------------------------------------------------------------------------------------------------------------")

    
