import sqlite3

try:
    # Connects to the database
    db = sqlite3.connect('ebookstore')
    cursor = db.cursor()  # Get a cursor object
    
    # Creates a table called books
    cursor.execute('''
        CREATE TABLE books(
        id INTEGER PRIMARY KEY, 
        book_title varchar(225) not null,
        book_author varchar(225) not null,
        book_qty INTEGER not null)
    ''')
    db.commit()     # Saves Changes to the database
    
    # Book List
    book_list = [
        (3001, "A Tale of Two Cities", "Charles Dickens", 30),
        (3002, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", 40),
        (3003, "TheLion, the Witch and the Wardrobe", "C.S. Lewis", 25),
        (3004, "The Lord of the Rings", "J.R.R Tolkien", 37),
        (3005, "Alice in Wonderland", "Lewis Carroll", 12)
    ]

    # Insert students into table books
    cursor.executemany('''INSERT INTO books(id, book_title, book_author, book_qty) VALUES(?,?,?,?)''', book_list)

    db.commit()     # Saves Changes to the database
   
# Handle errors
except sqlite3.Error as error:
    print('Error occurred - ', error)

   
# Gets user's input
def user_details():
    # Ensures sure does empty an empty value
    while True:
        bk_title = input("Please enter the book title: ")

        if bk_title:
            break
        else:
            print("Try again. Please don't leave the field empty.")
            continue

        # Ensures sure does empty an empty value
    while True:
        author = input("Please enter the book's author: ") 

        if author:
            break
        else:
            print("Try again. Please don't leave the field empty.")
            continue
        
    # Ensures sure does empty an empty value
    while True:
        try:
            qty = int(input("Please enter the quantity of the book, from 1 and above: "))

            if qty > 0:
                break
            
        except ValueError:
            print("Try again! Please empty numbers only.")
            continue
            
    return  bk_title, author, qty

def get_user_id():
    # Ensures sure does empty an empty value
    while True:
        try:
            bk_id = int(input("Please enter book ID or select '-1' to return to the main menu:  "))
            
            # Gets records for id entered
            cursor.execute('''SELECT * FROM books WHERE id = ? ''', (bk_id,))
            
            if cursor.fetchone() == None:
                
                # Allows users the option of returning to the main when item is not found, by selecting -1
                # Gives the users the option of continuing to look for the item or go back to the main when items are not found.
                if bk_id == -1:
                    return bk_id
                else:
                    print(f"\nNo book was found with ID: {bk_id}.")
                    continue
            break
            
        except ValueError:
            print("Try again! Please empty numbers only.")
            continue
    
    return bk_id

# Adds data to table
def add_book():
    # Gets values from users input
    bk_title, author, qty = user_details()
    
    # Gets the highest id number
    cursor.execute('''SELECT MAX(id) FROM books''')
    
    # Gets the records
    bk_id = cursor.fetchone()

    # Increase the id value by one to make it a unique number
    bk_id = int(''.join(map(str, bk_id))) + 1
    
    # Insert students into table books
    cursor.execute('''INSERT INTO books(id, book_title, book_author, book_qty) VALUES(?,?,?,?)''', (bk_id, bk_title, author, qty))
    print("\nNew book record has now been added.  See information below:")

    # Display new record added
    display_book(bk_id)

    db.commit()     # Saves Changes to the database
    

# Updates table records
def update_book():
    # Gets users input id
    bk_id = get_user_id()
    
    # Allows users the option of returning to the main when -1 is selected
    if bk_id != -1:
        #  Display book found
        display_book(bk_id)
        print(f"Start updating the book's information for ID: {bk_id}\n")

        # Gets values from users input
        bk_title, author, qty = user_details()

        # Updates book records 
        cursor.execute('''UPDATE books 
        SET book_title = ?, book_author = ?, book_qty = ?
        WHERE id = ? ''', (bk_title, author, qty, bk_id))

        db.commit()     # Saves Changes to the database

        print(f"Book record with ID {bk_id} has been updated\n")

    return bk_id


# Delete table records
def delete_book():
    # Gets users input id
    bk_id = get_user_id()

    # Allows users the option of returning to the main when -1 is selected
    if bk_id != -1:
        # Updates book records 
        cursor.execute('''DELETE FROM books WHERE id = ? ''', (bk_id,))
        db.commit()     # Saves Changes to the database

        print(f"Book record with ID {bk_id} has now been deleted")
        
    return bk_id


# Search table records
def search_book():
    # Gets users input id
    bk_id = get_user_id()
    
    # Allows users the option of returning to the main when -1 is selected
    if bk_id != -1:
        print(f"\nBook with ID {bk_id} has been found! See the book details below.")
        display_book(bk_id)
    
    return bk_id


# Displays book record records
def display_book(id):
    
    display_book = ""
    
    # Gets book details that is to be update
    cursor.execute('''SELECT * FROM books WHERE id = ? ''', (id,))
    get_book = cursor.fetchone()     # Fetch all the student data from the database
    
    display_book += f"\n-------------------- Book Details - ID: {id}-----------------------\n"
    display_book += f"\nTitle: {get_book[1]}\nAuthor: {get_book[2]}\nQuantity: {get_book[3]}\n"
    display_book += f"\n--------------------------------------------------------------------\n"

    print(display_book)     # Display book found


# User Menu
while True:

    program_menu = '''
Please select from the options below:
1 - Enter book
2 - Update book
3 - Delete book
4 - Search books
0 - Exit
: '''

    user_choice = input(program_menu)
    if user_choice == "1":
        add_book()

    elif user_choice == "2":
        update_item = update_book()

        # Returns users to the main menu when -1 is selected
        if update_item == -1:
            continue

    elif user_choice == "3":
        delete_item = delete_book()

        # Returns users to the main menu when -1 is selected
        if delete_item == -1:
            continue

    elif user_choice == "4":
        search_item = search_book()

        # Returns users to the main menu when -1 is selected
        if search_item == -1:
            continue
        
    elif user_choice == "0":
        print("Your have existed the program. Goodbye!")
        break
    else:
        print("\nWrong selection. Please try again!")


# Deletes books table
cursor.execute('''DROP TABLE books''')
print('Books table has now been deleted!')

db.close() # Close database
print('Connection to database closed')



