#=====importing libraries===========
'''This is the section where you will import libraries'''
from datetime import date, datetime


# Registers new user
def reg_user():
        
        # List to store user details
        user_list = []

        # Read login details to user.txt file
        user_file = open("project3/user.txt", "r", encoding="utf-8")

        
        for user in user_file:
            data = user.split(", ")
            user_list.append(data[0])
        

        user_file.close()  # Close file
           
        # Validates input data for create_username
        while True:
            create_username = input("Enter a new username: ").strip()    # Strip off whitespace

            if  create_username == "":
                print("Please try again! The username field is empty")
                continue
            
            # Checks is username exists
            for existing_user in user_list:
                while create_username == existing_user:
                    print("Username already exists.  Try another username.")
                    create_username = input("Enter a new username: ").strip()    # Strip off whitespace

            break
        
        # Validates input data for create_password
        while True:
            create_password = input("Enter a new password: ")

            if  create_password == "":
                print("Please try again! The password field is empty")
                continue

            
            confirm_password = input("Confirm your password: ")

            if create_password == confirm_password:

                # Write login details to user.txt file
                user_file_write = open("project3/user.txt", "a+", encoding="utf-8")

                user_file_write.write(f"\n{create_username}, {create_password}")

                user_file_write.close()       # Close user.txt text file
                
                break
            else: 
                print("Your password doesn't match.  Please try again")
                continue

# Adds new tasks
def add_task():

    '''
    - Field validation is added
    - If user makes an error for a specific field they are force straight away to 
    enter a validate input for that the same field, instead of repeating filling out the whole form again 
        '''
        
    register_username = input("Enter the username: ").strip()    # Strip off whitespace

    # Validation for username
    while register_username == "":
        register_username = input("Please don't leave field empty. Fill in the username: ").strip()
        continue
    
    
    task_title = input("Enter the task title: ").strip()

    # Validation for task_title
    while task_title == "":
        task_title = input("Please don't leave field empty. Fill in the task title: ").strip()
        continue
    
    
    task_description = input("Enter the task description:  ").strip()

    # Validation for task_description
    while task_description == "":
        task_description = input("Please don't leave field empty. Fill in the task description:  ").strip()
        continue

    task_due_date = due_date()
    today = date.today()
    today_date = today.strftime("%d %b %Y")
    task_completion = 'No'
        
    # Opens tasks.txt file that contains users tasks
    add_tasks_file = open("project3/tasks.txt", "a+", encoding="utf-8")

    # Appends created data to file tasks.txt
    add_tasks_file.write(f"\n{username}, {task_title}, {task_description}, {task_due_date}, {today_date}, {task_completion}")

    add_tasks_file.close()       # Close user.txt text file


# Gets due date
def due_date():

     # Validation for task_due_day
    while True:
        try: 
            task_due_day = int(input("Enter the task due day (DD):  "))

            if len(str(task_due_day)) > 2 or len(str(task_due_day)) < 1 or task_due_day > 31:
                print("Try again! Fill in the correct task due day (DD), between 1 - 31.")
                continue
            else:
                break

        except ValueError:
            print("Please fill in the task due day in numbers only, e.g 30")
            continue

    
    task_due_month = input("Enter the task due month in format (MMM), (Jan - Dec):  ").strip()
    
    # Validation for task_due_month
    while (not task_due_month.lower() in month_list) or task_due_month == "":
        task_due_month = input("Please enter the month in the correct format (MMM). Fill in the task due month (Jan - Dec):  ")
        continue

    # Validation for task_due_year
    while True:
        try: 
            task_due_year = int(input("Enter the task due year (YYYY):  "))

            if len(str(task_due_year)) != 4:
                print("Please enter the month in the correct format (YYYY). Fill in the task due year")
                continue
            
            break

        except ValueError:
            print("Please fill in the task due year in numbers only, e.g 2023")
            continue

    return f"{task_due_day} {task_due_month.title()} {task_due_year}"


# Displays all task found in task.txt file
def view_all():
    view_task = 'all'
    task_file_reader(view_task)

# Displays specific task for specific users found in task.txt file
def view_mine():
    view_task = 'mine'
    task_file_reader(view_task)
    

# Displays statistic all task found in task.txt file
def task_stats():
    
    while True:
        try:

            # Reads task_overview file
            tasks_overview_file = open("project3/task_overview.txt", "r", encoding="utf-8")
            
            display_stat = f"\n\n-------------------- TASK STATISTICS ------------------------\n\n"

            
            for data in tasks_overview_file:
                display_stat += f"{data}\n"

            
            tasks_overview_file.close() #close file


            display_stat += f"\n-------------------- END OF TASK STATISTICS --------------------\n"

            
            # Displays Statistics from the task_overview.txt file
            print(display_stat)
    
            

            # Reads user_overview file
            user_overview_file = open("project3/user_overview.txt", "r", encoding="utf-8")

            display_stat_user = f"\n\n-------------------- USERS STATISTICS ------------------------\n\n"
           
            for data_task in user_overview_file:
                display_stat_user += f"{data_task}\n"


            user_overview_file.close() #close file

            display_stat_user += f"\n-------------------- END OF USER STATISTICS --------------------\n\n"

            # Displays Statistics from the user_overview.txt file
            print(display_stat_user)

            break

        except FileNotFoundError:
            generate_report()
            continue


# Gets all the information from the task.txt file
def task_file_reader(view_type):
    
    # Empty list to store information for tasks in tasks.txt
    task_list = []

    # Initialise variables below
    display_task = ""
    display_specific_task = ""
    
    # Opens tasks.txt file that contains users tasks
    tasks_file = open("project3/tasks.txt", "r", encoding="utf-8")
    read_task_file = tasks_file.readlines()

    # Loop through the tasks data in tasks.txt to get all the task(s) and also specific tasks for specific username
    # Each task has a unique ID displayed above it
    for count, data in enumerate(read_task_file, 1):
        task_list = data.split(", ")
        
        # Use to display all the tasks in tasks.txt file
        if view_type == "all" and task_list:
            display_task += f"\n\n-------------------- TASK ID: {count}--------------------\n\n"
            display_task += f"Assigned to:\t\t {task_list[0]}\n"
            display_task += f"Title:\t\t\t {task_list[1]}\n"
            display_task += f"Description:\t\t {task_list[2]}\n"
            display_task += f"Assigned Date:\t\t {task_list[3]}\n"
            display_task += f"Due Date:\t\t {task_list[4]}\n"
            display_task += f"Task Completed:\t\t {task_list[5]}\n"
            display_task += f"\n--------------------END OF TASK --------------------\n\n"



        # Use to display specific tasks for specific users in tasks.txt file
        if username == task_list[0] and view_type == "mine" and task_list:
            display_specific_task += f"\n\n-------------------- TASK ID: {count}--------------------\n\n"
            display_specific_task += f"Assigned to:\t\t {task_list[0]}\n"
            display_specific_task += f"Title:\t\t\t {task_list[1]}\n"
            display_specific_task += f"Description:\t\t {task_list[2]}\n"
            display_specific_task += f"Assigned Date:\t\t {task_list[3]}\n"
            display_specific_task += f"Due Date:\t\t {task_list[4]}\n"
            display_specific_task += f"Task Completed:\t\t {task_list[5]}\n"
            display_specific_task += f"\n--------------------END OF TASK --------------------\n\n"
    

    # Displays tasks information if tasks.txt file is not empty
    if len(task_list) > 0:

        # Use to display all the tasks in tasks.txt file
        if view_type == "all":
            print(display_task)
        
        # Use to display specific tasks for specific users in tasks.txt file
        if view_type == "mine":  
            print(f"\n\nYour task(s). User: {username}")
            print(display_specific_task)
    

    # Displays message and exit from program if tasks.txt is empty when option vm is selected
    elif view_type == "all" and not task_list:
        print(f"\n\n-------------------- TASK LIST --------------------\n\n")
        print("No tasks are found")
        print(f"\n\n--------------------END OF TASK LIST --------------------\n\n")
        
        exit()

    # Displays message and exit from program if tasks.txt is empty when option vm is selected
    elif view_type == "mine" and not task_list:
        print(f"\n\n-------------------- TASK LIST --------------------\n\n")
        print(f"No task found for user {username}")
        print(f"\n\n--------------------END OF TASK LIST --------------------\n\n")

        exit()

    tasks_file.close()          # Close tasks.txt file



# Gets all the information from the task.txt
def file_reader_task():

    # Empty list to store information for tasks in tasks.txt
    tasks_data_list = []

    # Initialise variables below
    display_task_report = ""
    count = 0       # Set the count value to 0 if tasks.txt is empty.  That is display_stat will display 0 when tasks.txt is empty
    num_completed = 0       # Counting number of completed tasks
    num_uncompleted = 0     # Counting number of uncompleted tasks
    num_overdue_uncompleted  = 0     # Counting number of uncompleted tasks
    overdue_pct = 0
    uncompleted_pct = 0
    
    # Opens tasks.txt file that contains users tasks
    tasks_file = open("project3/tasks.txt", "r", encoding="utf-8")
    
    read_task_file = tasks_file.readlines()

    # Loop through the tasks data in tasks.txt to get all the task(s) and also specific tasks for specific username
    # Each task has a unique ID displayed above it
    for count, data in enumerate(read_task_file, 1):
        tasks_data_list.append(data.split(", "))
        

        # Gets number of completed tasks
        if tasks_data_list[count - 1][5].lower().strip('\n') == 'yes':
            num_completed += 1

        # Gets number of uncompleted tasks
        if tasks_data_list[count - 1][5].lower().strip('\n') == 'no':
            num_uncompleted += 1

        # Gets number of uncompleted and overdue task
        if tasks_data_list[count - 1][5].lower().strip('\n') == 'no' and datetime.strptime(tasks_data_list[count - 1][4], "%d %b %Y") < datetime.today():
            num_overdue_uncompleted += 1
    
        
    tasks_file.close()          # Close tasks.txt file


    if count != 0:

        # Calculates percentage of incomplete task
        uncompleted_pct = (num_uncompleted / count) * 100
        
        # Calculates percentage of overdue task 
        overdue_pct = (num_overdue_uncompleted / count) * 100

        display_task_report += f"\nThe total number of task that have been generated and tracked is {count}.\n"
        display_task_report += f"The total number of completed task is {num_completed}.\n"
        display_task_report += f"The total number of uncompleted task is {num_uncompleted}.\n"
        display_task_report += f"The total number of uncompleted and overdue task is {num_overdue_uncompleted }.\n"
        display_task_report += f"The percentage of incomplete task is {round((uncompleted_pct), 2)}%.\n"
        display_task_report += f"The percentage of overdue task is {round((overdue_pct), 2)}%.\n"

    # Returns value to generate_report()
    return display_task_report
    



# Gets all the information from the user.txt file
def file_reader_user():
      
    # Initialise variables below
    display_user_report = ""
    count = 0       # Set the count value to 0 if tasks.txt is empty.  That is display_stat will display 0 when tasks.txt is empty

    task_dict = {}  # Dictionary to store data for tasks, to generate the users report generation
    tasks_data_list = []

               
    completed_task = "Completed"
    uncompleted_task = "Uncompleted"
    overdue_task = "Overdue"

    # Opens tasks.txt file that contains users tasks
    tasks_file = open("project3/tasks.txt", "r", encoding="utf-8")
    read_task_file = tasks_file.readlines()

    # Loop through the tasks data in tasks.txt to get all the task(s) and also specific tasks for specific username
    # Each task has a unique ID displayed above it
    for count, data in enumerate(read_task_file, 1):
        tasks_data_list.append(data.split(", "))
    
    
    tasks_file.close()          # Close tasks.txt file
    

    # Starting section of the User report
    display_user_report += f"The total number of users registered is {len(username_list)}.\n"
    display_user_report += f"The total number of task that have been generated and tracked is {count}.\n"


    # Identifies users for found in the tasks_data_list list, then creates dictionary keys and value for task_dict
    # to capture data for user_report
    for user in username_list:
        for tasks in tasks_data_list:
            
            # Create key and set value for specific user for dictionary task_dict
            if user == tasks[0]:

                # Create key and set value for username for dictionary task_dict
                if user in task_dict:
                    task_dict[user] = int(task_dict[user]) + 1
                else:
                    task_dict[user] =  1

                # Create key and set value for completed task for dictionary task_dict
                if tasks[-1].strip("\n").lower() == 'yes':
                    user_dict_key = user + completed_task

                    if user_dict_key in task_dict:
                        task_dict[user_dict_key] = int(task_dict[user_dict_key]) + 1
                    else:
                        task_dict[user_dict_key] =  1

                else:
                    # Create key and set value for uncompleted task for dictionary task_dict
                    user_dict_key = user + uncompleted_task

                    if user_dict_key in task_dict:
                        task_dict[user_dict_key] = int(task_dict[user_dict_key]) + 1
                    else:
                        task_dict[user_dict_key] =  1

                    # Create key and set value for overdue task for dictionary task_dict
                    if datetime.strptime(tasks[4], "%d %b %Y") < datetime.today():
                        user_dict_key = user + overdue_task
                        
                        if user_dict_key in task_dict:
                            task_dict[user_dict_key] = int(task_dict[user_dict_key]) + 1
                        else:
                            task_dict[user_dict_key] =  1


        # Gets value from dictionary task_dict to generate data for user report 
        for item in task_dict:
            if user == item:
                user_completed = user + completed_task
                user_uncompleted = user + uncompleted_task
                user_overdue = user + overdue_task

                # Total number task for a specific user
                num_of_tasks = task_dict[user]
                
                # Calculates task percentage for specific user out of total task in task.txt file
                assigned_task_pct = (task_dict[user] / count) * 100

                display_user_report += f"\n----- Report for user {user} -----\n"
                display_user_report += f"The total number of task assigned to user {user} is {task_dict[user]}.\n"
                display_user_report += f"The percentage of task assigned to user {user} is {round(assigned_task_pct, 2)}%.\n"

            
                if user_completed in task_dict:
                    # Calculates percentage for completed task for specific user out of assigned tasks to the user
                    completed_task_pct = (task_dict[user_completed] / num_of_tasks) * 100

                    display_user_report += f"The percentage of assigned task completed by user {user} is {round(completed_task_pct, 2)}%.\n"
                else:
                    display_user_report += f"The percentage of assigned task completed by user {user} is 0%.\n"
                

                if user_uncompleted in task_dict:
                    # Calculates percentage for uncompleted task for specific user out of assigned tasks to the user
                    uncompleted_task_pct = (task_dict[user_uncompleted] / num_of_tasks) * 100

                    display_user_report += f"The percentage of assigned task uncompleted by user {user} is {round(uncompleted_task_pct, 2)}%.\n"
                else:
                    display_user_report += f"The percentage of assigned task uncompleted by user {user} is 0%.\n"

                if user_overdue in task_dict:
                    # Calculates percentage for uncompleted overdue task for specific user out of assigned tasks to the user
                    overdue_task_pct = (task_dict[user_overdue] / num_of_tasks) * 100

                    display_user_report += f"The percentage of assigned task uncompleted and overdue by user {user} is {round(overdue_task_pct, 2)}%.\n"
                else:
                    display_user_report += f"The percentage of assigned task uncompleted and overdue by user {user} is 0%.\n"

    # Returns value to generate_report()
    return display_user_report


# Write file for task edited
def edit_write_file(task_list):

    with open('tasks.txt', 'w') as file_update:
        for task_data in task_list:
            tasks = ""
            tasks += ", ".join(task_data)
            
            file_update.writelines( tasks )


# Function that edit tasks
def edit_task():
    
    # Reads tasks file 
    tasks_file = open("project3/tasks.txt", "r", encoding="utf-8")
    read_task_file = tasks_file.readlines()
     
    
    while True:
        try:
            edit_menu_option = int(input(f"\nSelect one of the options below: \nTo edit task enter the ID number \nTo go to the main menu enter -1 \n: "))

            break

        except ValueError:
            print("\nTry again! Please enter an ID number or enter -1 to go back to main menu\n")
            continue


    # List to store all tasks from tasks.txt for editing and updating
    tasks_list = []
    edit_menu_str = str(edit_menu_option)

    # Error message
    task_not_found_msg = f"\nTask not found with ID {edit_menu_option} for the username '{username}'\n"


    # Allows users to return to main menu
    if  edit_menu_str == "-1":
        return -1
        
    else:
        # Loop through the tasks data in tasks.txt to get all the task(s)
        for data in read_task_file:
            tasks_list.append(data.split(", "))

        if edit_menu_option <= len(tasks_list):

            # Allows user to edit task assigned to them
            if username == tasks_list[edit_menu_option - 1][0]:
                
                # variable to store value for task completion - No or Yes
                is_task_completion = tasks_list[edit_menu_option - 1][-1].lower().strip().strip("\n")

                # Only allows users to edit task when task completion is equals to No
                if is_task_completion == 'no':

                    # Gives users option to mark task as complete or edit some fields
                    update_task = input(f"\nTo mark the task ID {edit_menu_option} as complete enter 'Yes' or to edit the task enter 'Edit' or"
                                            " select any other keys to go to the option menu: ").lower()
                    
                    # Gives users option to mark task as complete
                    if update_task == 'yes':
                        tasks_list[edit_menu_option - 1][-1]  = 'Yes\n'
                        print(f"\nTask ID {edit_menu_option} has been marked as completed\n")

                        # Updates task.txt file, the selected user task is marked as completed
                        edit_write_file(tasks_list)


                    # Gives users option to update username and completion date
                    elif update_task == 'edit':

                        # Allows user to select what they want to edit out for both items
                        task_edit = input("To edit Username select 'u', for Due Date select 'd' or for both select 'b' or select any other keys to go to the option menu: ").lower()
                        
                        # For editing username
                        if task_edit == 'u' or task_edit == 'b':
                            update_username = input("Enter the new surname name: ")

                            # updates username 
                            tasks_list[edit_menu_option-1][0] = update_username
                            
                            print(f"\nThe username has now been updated\n")

                        # For editing due date
                        if task_edit == 'd' or task_edit == 'b':

                            # updates due date
                            tasks_list[edit_menu_option - 1][-3] = due_date()

                            print(f"\nThe due date has now been updated\n")

                            
                        # Updates due date and username in task.txt file
                        edit_write_file(tasks_list)

                 # Displays message for users telling them, they can't edit the task 
                elif is_task_completion == 'yes':
                    print(f"\nTask ID {edit_menu_option} for the username '{username}' is completed and cannot be edited \n")
            else:
                print(task_not_found_msg)
        else:
            print(task_not_found_msg)
    
    tasks_file.close()    # Close files
            
                    
# Function use to generate task and users report
def generate_report():

    generate_tasks_report()
    generate_user_report()


# Use to generate task report
def generate_tasks_report():

    file_name = "project3/task_overview.txt"
    tasks_overview_report = "tasks_report"
    report_file_writer(file_name, tasks_overview_report)


# Use to generate users report
def generate_user_report():

    file_name = "project3/user_overview.txt"
    user_overview_report = "users_report"
    report_file_writer(file_name, user_overview_report)


# Generates file and write data to it
def report_file_writer(file, report_type):

    # Generates file
    tasks_overview_file = open(file, "w", encoding="utf-8")

    # Stores of report generated from data reader from files tasks.txt and user.txt
    if report_type == "users_report":
        overview_report = file_reader_user()
    elif report_type == "tasks_report":
        overview_report = file_reader_task()

        if overview_report:
            print("\nBoth the tasks and users report has been generated.\n")

        else:
            print("\nTask file is empty. To add task(s) to the file select option 'a' from the main menu\n")
    
    tasks_overview_file.writelines(overview_report)

    tasks_overview_file.close() #close file


    
#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.task_file_reader
'''

# Opens user.txt file containing login details
login_file = open("project3/user.txt", "r", encoding="utf-8")

# Empty list to store the users login details
username_list = []
password_list = []

# Appends username and password into the list username_list and password_list respectively
for login_detail in login_file:
    user_name, user_password = login_detail.strip("\n").split(", ")
    
    username_list.append(user_name.lower())     # Makes username non case sensitive when validating the username
    password_list.append(user_password)


login_file.close()      # Close user.txt file

login_err_msg = "You have enter an invalid credential. Please enter the correct  username and password"

# Validates users username and password
while True:
    username = input("Enter username: ").lower().strip()    # Use lowercase to make username not case sensitive. and strip off whitespace
    password = input("Enter password: ")

    if username in username_list:
        password_pos = username_list.index(username)
        
        if password == password_list[password_pos]:
            break
        else:
            print(login_err_msg)
            continue
    
    else:
        print(login_err_msg)
        continue


# List contains month of the year in the required format (MMM). This list is used for the month validation
month_list = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

# Adds extra menu for username 'admin'
extra_menu = ""
if username == 'admin':
    extra_menu = "\ngr - Generate reports \nds - Display statistics"

while True:
    #presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    menu = input(f'''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task {extra_menu}
e - Exit
: ''').lower()
    


    if menu == 'r':
        '''In this block you will write code to add a new user to the user.txt file
        - You can follow the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same.
            - If they are the same, add them to the user.txt file,
            - Otherwise you present a relevant message.'''
        
        
    # Gives only username 'admin' access rights to register a user
        if username == 'admin':
            reg_user()
        else:
            print("\nOnly the username 'admin' has permission to register a user. Please select another option.\n")
       
        break

    elif menu == 'a':
        '''In this block you will put code that will allow a user to add a new task to task.txt file
        - You can follow these steps:
            - Prompt a user for the following: 
                - A username of the person whom the task is assigned to,
                - A title of a task,
                - A description of the task and 
                - the due date of the task.
            - Then get the current date.
            - Add the data to the file task.txt and
            - You must remember to include the 'No' to indicate if the task is complete.'''
        
        add_task()

        break

    elif menu == 'va':
        '''In this block you will put code so that the program will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 
            - It is much easier to read a file using a for loop.'''
        
        # Prints out all the tasks
        view_all()

        break

    elif menu == 'vm':
        '''In this block you will put code the that will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the username you have
            read from the file.
            - If they are the same print it in the format of Output 2 in the task PDF'''
        
        # Prints out the tasks for specific users
        view_mine()
        edit_task()

        # continue

    # Ensures this menu vs is only accessible to username 'admin'
    elif menu == 'ds' and username == 'admin':
        task_stats()

        break

    # Ensures this menu gr is only accessible to username 'admin'
    elif menu == 'gr' and username == 'admin':

        generate_report()

        break

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
