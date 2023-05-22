def begin():
    # Read input from "info.txt" file and store in a dictionary
    with open("info.txt") as file:
        input_Dict = {}
        idforlaptop = 1
        for line in file:
            line = line.replace("\n","")
            input_Dict[idforlaptop] = line.split(",")
            idforlaptop += 1
    return input_Dict


def d_name_contact():
    # Get dealer name and contact information from the user
    dealer_name = input("Enter dealer name: ")
    dealer_contact = input("Enter dealer contact: ")
    return dealer_name, dealer_contact


def name_number():
    # Get customer name and phone number from the user
    print("\n CUSTOMER DETAILS:")
    print("-------------------------\n")
    name = input("Enter your name: ")
    customer_number = input("Enter your phone number: ")
    print("\n-------------------------\n")
    return name, customer_number
