
#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        pass
        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
        
        # Initialise attributes 
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # Method to the cost of shoes  
    def get_cost(self):
        pass
        '''
        Add the code to return the cost of the shoe in this method.
        '''
        return self.cost

    # Method to the quantity of the shoes
    def get_quantity(self):
        pass
        '''
        Add the code to return the quantity of the shoes.
        '''
        return self.quantity
    
    # Returns the value of the attributes in string
    def __str__(self):
        pass
        '''
        Add a code to returns a string representation of a class.
        '''
        return f'''\n=============================================
\nCountry:\t{self.country}
Code:\t\t{self.code}
Product:\t{self.product}
Cost:\t\t{self.cost}
Quantity:\t{self.quantity}'''
                


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
# List to store shoe object created
shoe_list = []

#==========Functions outside the class==============
def read_shoes_data():
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''

    try:
        # Reads details from the txt
        inventory_file = open("inventory.txt", "r", encoding="utf-8")

        for count, data in enumerate(inventory_file):
            # Skips the first line of the inventory data
            if count != 0:
                data = data.strip("\n").split(",")
                inventory_data = Shoe(data[0], data[1], data[2], data[3], data[4])
                shoe_list.append(inventory_data)    # Appends the shoe object into the list shoe_list

        inventory_file.close()  # Close file
    except Exception as error:
        print(f"Try again! An error has occurred {error}")


def capture_shoes():
    pass
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    
    # Captures user information about the shoe
    while True:
        country = input("Enter the country you are in: ")

        if country:
            break
        else:
            print("Try again! Please fill the field.")
            continue

    while True:
        product_code = input("Enter the code of the shoe: ")

        if product_code:
            break
        else:
            print("Try again! Please fill the field.")
            continue
    
    # Validates User input
    while True:
        product_name = input("Enter the name of the shoe: ")
            
        if product_name:
            break
        else:
            print("Try again! Please fill the field.")
            continue
    
    # Validates User input
    while True:
        try: 
            product_cost = int(input("Enter the cost of the shoe: "))
        except ValueError:
            print("Try again! Enter numbers only!")
            continue
        break

    while True:
        try: 
            product_quantity = int(input("Enter the quantity of the shoe: "))
        except ValueError:
            print("Try again! Enter numbers only!")
            continue
        break
    

    # Store the list of updated shoe objects
    shoe_stock_update = ["Country,Code,Product,Cost,Quantity\n"]
    
    # Creates shoe object from the user input
    shoe = Shoe(country, product_code, product_name, product_cost, product_quantity)
    shoe_list.append(shoe)

    # Keeps shoe_list in sync with updates to the inventory,txt file 
    for data in shoe_list:
        shoe_data = f"{data.country},{data.code},{data.product},{data.cost},{data.quantity}\n"
        shoe_stock_update.append(shoe_data)
        
        # Updates inventory.txt file    
        update_inventory(shoe_stock_update)
    
    # Print out confirmation message
    print(f"\nThe shoe {product_name} with product code {product_code} from {country} has been added to the list\n")


def view_all():
    pass
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''
    for data in shoe_list:
        shoe = Shoe(data.country, data.code, data.product, data.cost, data.quantity)
        
        # Prints out all the list of shoes
        print(shoe)


def re_stock():
    pass
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    
    restock_shoe = ""

    # List to store the shoe object in reverse order 
    shoe_list_reverse = shoe_data_reverse()
    
    # Store the list of updated shoe objects 
    shoe_stock_update = []

    if shoe_list_reverse: 
        # Find out if use wants to restock with the same amount of quantity found in the list
        restock_shoe = input(f"Do you want to re-stock {shoe_list_reverse[0][2]} - {shoe_list_reverse[0][3]}, by {shoe_list_reverse[0][0]}"
                            " more items? Choose 'Y' for Yes or any other key to back to the menu: ").lower()
    
    if restock_shoe == "y":
        print(f"\nThe shoe {shoe_list_reverse[0][2]}, product number {shoe_list_reverse[0][3]}, has been restocked by {shoe_list_reverse[0][0]} more items")

        # # Reads details from the txt
        inventory_file = open("inventory.txt", "r", encoding="utf-8")
        
        # List shoe_list for it to updated with the latest list of shoe object
        shoe_list.clear()
        updated_data = []
        
        for count, data in enumerate(inventory_file):
            data = data.strip("\n").split(",")

            # Filters out the shoe with the lowest quantity using the product code
            if shoe_list_reverse[0][3] == data[1]:
                # Adds the same amount to the original quantity 
                data[-1] = str(int(data[-1]) + int(data[-1]))
            
            # Skips the first line of the inventory data
            if count != 0:
                updated_data = Shoe(data[0], data[1], data[2], data[3], data[4])
                
                # Store the list of updated shoe objects for the shoe_list
                shoe_list.append(updated_data)

            data = f"{data[0]},{data[1]},{data[2]},{data[3]},{data[4]}\n"
            
            # Store the list of updated shoes to be used to update inventory.txt file
            shoe_stock_update.append(data)


        # Updates inventory.txt file    
        update_inventory(shoe_stock_update)

        inventory_file.close()      # Close file


def seach_shoe():
    pass
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    
    # Stores shoes found from the list shoe_list
    is_found = []
    
    # Gets user product input
    shoe_code = input("Enter shoe code: E.g 'SKU20207' ").lower()

    for data in shoe_list:
        if shoe_code == data.code.lower():
            shoe = Shoe(data.country, data.code, data.product, data.cost, data.quantity)
            
            # Appends found shoe into the list is_found
            is_found.append(f"{shoe}")

            # Prints out the item found
            print(f"\nYour item has been found:\n{shoe}")

    if len(is_found) < 1:        
        print(f"\nNo shoe were found with the product code {shoe_code}\n")

def value_per_item():
    pass
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    # Initializes variable
    total_value_per_item  = 0

   
    # Calculates the total value for each shoe
    for data in shoe_list:
        shoe = Shoe(data.country, data.code, data.product, data.cost, data.quantity)
        total_value_per_item = int(data.cost) * int(data.quantity)
        
        # Prints the total value for each shoe
        print(shoe, f"\nTotal Value:\t{total_value_per_item}")

def highest_qty():
    pass
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''

    # List to store the shoe object in reverse order 
    shoe_list_reverse = shoe_data_reverse()
  
    if shoe_list_reverse:
        # Stores shoe object with the highest quantity of shoe
        shoe_list_info = shoe_list_reverse[-1]

        # Revert the list back to the original value
        shoe_list_info = shoe_list_info[::-1]

        shoe = Shoe(shoe_list_info[0], shoe_list_info[1], shoe_list_info[2], shoe_list_info[3], shoe_list_info[4])

        # Prints out the highest quantity of shoe
        print(f"\nThe shoe below is for sale:")
        print(f"{shoe}\n")
    else:
        print(f"\nThe no shoe found!")



# Reserves the order of the Shoe Object
def shoe_data_reverse():
    # List to store the latest data from inventory.txt file
    shoe_data_list = []

    try:
        # Reads details from the txt
        inventory_file = open("inventory.txt", "r", encoding="utf-8")

        for count, data in enumerate(inventory_file):

            # Skips the first line of the inventory data
            if count != 0:
                data = data.strip("\n").split(",")
                inventory_data = Shoe(data[0], data[1], data[2], data[3], data[4])
                shoe_data_list.append(inventory_data)    # Appends the shoe object into the list shoe_list

        inventory_file.close()  # Close file
    except Exception as error:
        print(f"Try again! An error has occurred {error}")
        
    # List to store the shoe object in reverse order 
    shoe_list_reverse = []

    for data in shoe_data_list:
        # Stores data from shoe_list and sets the value for data.quantity to an integer 
        shoe_data = [data.country, data.code, data.product, data.cost, int(data.quantity)]
        
        # Stores reveres data from the shoe_list
        shoe_data_reverse = shoe_data[::-1]
        
        # Appends shoe object in reverse order to the list shoe_list_reverse
        shoe_list_reverse.append(shoe_data_reverse)

    # Sort the shoe_list_reverse based on the data.quantity from lowest value to highest
    shoe_list_reverse.sort()

    return shoe_list_reverse


# Updates the inventory.txt file with the updated information
def update_inventory(shoe_stock):
    inventory_file_write = open("inventory.txt", "w", encoding="utf-8")
    
    for updated_shoe_data in shoe_stock:
        inventory_file_write.writelines(updated_shoe_data)

    inventory_file_write.close()      # Close file


#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''

inventory_program = '''
Welcome to the inventory system! Please select from the menu below.

va - List all the shoe inventory.
a - Add shoe information.
r - Restock shoe.
s - Search for shoe.
v - View the value of all shoe items.
h - List the highest quantity of shoe.
e - exit this program.
'''

# Reads data from inventory.txt and appends data to the shoe_list
read_shoes_data()


while True:
    selection = input(inventory_program ).strip().lower()

    if selection == 'va':
        # Gets all the shoe info in the inventory
        view_all()
    
    elif selection == 'a':
        # Gets users data input for the shoes and adds to the shoe list
        capture_shoes()

    elif selection == 'r':
        # Finds the lowest quantity of shoes and gives users the option of re-stocking it 
        re_stock()

    elif selection == 's':
        # Finds shoe and display shoe information
        seach_shoe()

    elif selection == 'v':
        # Calculates and displays the total value of each shoe
        value_per_item()

    elif selection == 'h':
        # Finds the highest quantity of shoes in the inventory
        highest_qty()

    elif selection == 'e':
        print("You have exited the program")
        break
    else:
        print("Oops! You chose the wrong option.")
