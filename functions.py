import datetime
import read

# Read the laptop details from the input file
input_Dict = read.begin()

# Function to display a welcome message
def hello():
    print("\n")
    print("----------------------------------------------------------")
    print("\t\t Hello to BibekShil Laptop Heaven")  # \t is used to give tabs
    print("----------------------------------------------------------")
    print("\t \t   Manigram")
    print("----------------------------------------------------------")
    print("\n")

# Function to display the laptop details
def laptop_details():
    print("\n")
    print("---------------------------------------------------------------------------------------------------------------------")
    print("S.N \t Name \t\t\t laptop_brand \t\t\t  Price \t Quantity \t Processor \t Graphics Card")
    print("---------------------------------------------------------------------------------------------------------------------")

    # Read the laptop details from the input file and display them
    with open("info.txt", "r") as file:
        a = 1
        for line in file:
            print(a, "\t" + line.replace(",", "\t\t"))
            a += 1
    print("---------------------------------------------------------------------------------------------------------------------")
    print("\n")

# Function to validate the laptop ID for buying


# Function to validate the quantity for buying
def valid_quantity():
    user_qty = int(input("\n Please provide the quantity of laptop you want to buy: "))

    while user_qty <= 0:
        print("Dear admin, please input more than one: ")
        print("\n")
        user_qty = int(input("Please provide the quantity of laptop you want to buy: "))
        print("\n")
    return user_qty

# Function to update the buy file with validated ID and quantity
def file_update(validated_ID, user_qty):
    input_Dict = read.begin()
    input_Dict[validated_ID][3] = int(input_Dict[validated_ID][3]) + int(user_qty)
    with open("info.txt", "w") as file:
        for values in input_Dict.values():
            file.write(str(values[0]) + "," + str(values[1]) + "," + str(values[2]) + "," + str(values[3]) + "," + str(values[4]) + "," + str(values[5]))
            file.write("\n")

# Function to validate the laptop ID for selling
def sell_validID():
    validated_ID = int(input("Enter the ID of the laptop customer wants to buy: "))
    while validated_ID <= 0 or validated_ID > len(input_Dict):
        print("Please provide a valid laptop id")
        print("\n")
        validated_ID = int(input("Enter the ID of the laptop customer wants to buy: "))
    print("\n")
    return validated_ID

# Function to validate the quantity for selling
def sell_valid_quantity():
    user_qty = int(input("Enter the quantity of laptop the customer wants to buy: "))

    while user_qty <= 0:
        print("Dear customer, the quantity you are looking for is not available in store: ")
        print("\n")
        user_qty = int(input("Please enter the quantity of laptop the customer wants to buy: "))
        print("\n")
    return user_qty

# Function to update the sell file with validated ID and quantity
def sell_file_update(validated_ID, user_qty):
    input_Dict = read.begin()
    input_Dict[validated_ID][3] = int(input_Dict[validated_ID][3]) - int(user_qty)
    with open("info.txt", "w") as file:
        for values in input_Dict.values():
            file.write(str(values[0]) + "," + str(values[1]) + "," + str(values[2]) + "," + str(values[3]) + "," + str(values[4]) + "," + str(values[5]))
            file.write("\n")

# Function to display the second laptop details in a file
def second_laptop(validated_ID, user_qty, name):
    prodct_name = str(input_Dict[validated_ID][0])
    laptop_brand = str(input_Dict[validated_ID][1])
    users_qty = str(user_qty)
    price_per_unit = str(input_Dict[validated_ID][2])
    item_markedprice = str(input_Dict[validated_ID][2].replace("$", ''))
    user_amount = str(int(item_markedprice) * int(users_qty))
    total_amount = str(float(int(user_amount)))

    filename = str(name) + ".txt"
    with open(filename, "a") as sell:
        sell.write(prodct_name + " \t\t " + laptop_brand + " \t\t " + str(users_qty) + " \t\t " + str(price_per_unit) + " \t\t " + str(user_amount) + " \t\t " + total_amount + "\n")
        sell.write("-----------------------------------------------------------------------------------------------------------------------")

# Function to display the second laptop details in the console
def secondlaptop_konsole(validated_ID, user_qty, name):
    prodct_name = str(input_Dict[validated_ID][0])
    laptop_brand = str(input_Dict[validated_ID][1])
    users_qty = str(user_qty)
    price_per_unit = str(input_Dict[validated_ID][2])
    item_markedprice = str(input_Dict[validated_ID][2].replace("$", ''))
    user_amount = str(int(item_markedprice) * int(users_qty))
    total_amount = str(float(int(user_amount)))

    print(prodct_name + " \t\t " + laptop_brand + " \t\t " + str(users_qty) + " \t\t " + str(price_per_unit) + " \t\t " + str(user_amount) + " \t\t " + total_amount)
    print("-----------------------------------------------------------------------------------------------------------------------\n \n \n")

# Function to update the dealer's file with validated ID and quantity
def dealer_second_laptop(validated_ID, user_qty, dealer_name):
    prodct_name = input_Dict[validated_ID][0]
    laptop_brand = input_Dict[validated_ID][1]
    users_qty = (user_qty)
    price_per_unit = (input_Dict[validated_ID][2])
    item_markedprice = (int(input_Dict[validated_ID][2].replace("$", '')))
    user_amount = (int(item_markedprice) * int(users_qty))
    vat_total_price = (float(int(user_amount) + (0.13) * (int(user_amount))))

    filename = str(dealer_name) + ".txt"
    with open(filename, "a") as order:
        order.write("\n" + prodct_name + " \t\t " + laptop_brand + " \t\t " + str(users_qty) + " \t\t " + str(price_per_unit) + " \t\t " + str(user_amount) +
                    " \t\t " + str(vat_total_price))
        
def validated_ID():
    validated_ID = int(input("\n Enter the ID of the laptop you want to buy: "))
    while validated_ID <= 0 or validated_ID > len(input_Dict):
        print("Please provide a valid laptop id")
        print("\n")
        validated_ID = int(input("Please Provide the id of the laptop you want to buy: "))
    print("\n")
    return validated_ID


# Function to sell a laptop
def sell_laptop():
    validated_ID = validated_ID()
    user_qty = input("Enter the quantity you want to sell: ")
    sell_file_update(validated_ID, user_qty)
    second_laptop(validated_ID, user_qty, "sales_report")
    secondlaptop_konsole(validated_ID, user_qty, "sales_report")
    dealer_name = input("Enter the dealer's name: ")
    dealer_second_laptop(validated_ID, user_qty, dealer_name)
    print("Laptop sold successfully!")

# Test the sell_laptop() function
sell_laptop()





