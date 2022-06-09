'''Capstone template project for FCS Task 19 Compulsory task 1.
This template provides a skeleton code to start compulsory task 1 only.
Once you have successfully implemented compulsory task 1 it will be easier to
add a code for compulsory task 2 to complete this capstone'''

#=====Importing libraries===========


from datetime import date       # Looked up online how to get current date for 'a' option
import datetime
import os.path


#====Login Section====


# Task and user files opened with mode set to read only for user file and read + write for task file

user_file = open("user.txt", "r")
task_file = open("tasks.txt", "r+")

list_usernames = []
list_passwords = []

lines = user_file.readlines()

'''For loop uses .strip() and .split() functions to remove newline characters and split each item into
an individual string, and then uses .append() and indexing to add each individual username and password
to the respective lists created earlier.'''
 
for line in lines:
    temp = line.strip()                                        
    temp = temp.split(", ")
    
    list_usernames.append(temp[0])
    list_passwords.append(temp[1])

# Input command requests the user to enter their username and password

username = input("Please enter your username: ")
password = input("Please enter your password: ")

# Login defined as the Boolean variable 'False'

login = False

'''The while loop causes the nested if statements to run while login is not true. The if statement checks
whether the username entered by the user is in the list of passwords created earlier. If it is not in the
list of passwords, the if statement executes and login remains false and the user is asked to try again. If
the username is in the list of usernames, the else statement executes and login is switched to true and the
user is granted access to the program. The same method is then used to check the passwords although using
the password entered and the list of passwords.'''

while login != True:
    
    if username not in list_usernames or password not in list_passwords:
        
        print("Incorrect. Try again")
        
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        
        login = False

    else:
        
        login = True

print('''
Access granted.

Welcome to the program!
''')

user_file.close()
task_file.close()


#=========Defining functions=============


'''Function defined to add a new user to the user file. Function is called when the user selects 'r'. If the user
is 'admin', the nested if statement asks the user to input their username and password and then their password
again to confirm. The open command is used to open the user file with the mode set to 'a', allowing the program
to append to the file. The next nested if statement compares the two passwords entered by the user and if they
are equal, the else statement executes and uses the write function to append an fstring to the user file containing
the username and password. If the two passwords are not equal, the while loop asks the user to try again until they
match.'''

'''The first nested if statement is (a) of Part 2. It tells the program to only perform the functions to register
a new user if the current username is 'admin', and otherwise returns a message explaining to the user that only
admin is allowed to register new users.'''

'''The second nested if statement checks whether the username entered is already in the list of usernames. If the
username already exists, the user is displayed an error message and asked to try again with a different username.'''
    
def reg_user():
    
    if username == "admin":
            
        new_username = input("Enter your new username: ")
        new_password = input("Enter your new password: ")
        password_confirm = input("Please confirm your password: ")
            
        user_file = open("user.txt", "a")

        if new_username in list_usernames:
            print("Username already exists")
            new_username = input("Try again. Enter your new username: ")
            new_password = input("Enter your new password: ")
            password_confirm = input("Please confirm your password: ")

            user_file.write(f"\n{new_username}, {new_password}")
                    

        else:       
            
            if new_password != password_confirm:
                
                while new_password != password_confirm:
                    password_confirm = input("Passwords do not match. Try again: ")

                
                    print('''
Success! User added.
''')
                
            else:
                user_file.write(f"\n{new_username}, {new_password}")
                
                print('''
Success! User added.
''') 
                
    else:
        print('''
Sorry, only admin is allowed to register new users!
''')
            
    user_file.close()
        
    pass
    return


'''Function defined to add a task to the task file. The function is called when the user selects 'a'. The user is
requested to enter various data points pertaining to the task and they are stored as seperate variables. Date.today()
used to get the current date and .strftime() used to change the date format. The open function is used to open the
task file with the mode set to 'a', allowing the program to append new tasks to the file. The write function is then
used to append an fstring containing all of the data points entered by the user.'''

def add_task():
    
    task_assign = input("Enter the username of the person to whom the task is assigned: ")   
    task_title = input("Enter the title of the task: ")       
    task_descrip = input("Enter the description of the task: ")       
    task_date = input("Enter the due date of the task (dd/mm/yyyy): ")
        
    current_date = date.today()
    current_date_words = current_date.strftime("%d %B %Y")      # Looked up .strftime() online to change date format
        
    complete = "No"

    task_file = open("tasks.txt", "a")
        
    task_file.write(f"{task_assign}, {task_title}, {task_descrip}, {task_date}, {current_date_words}, {complete}\n")

    print('''
Success! Task added.
''')

    task_file.close()

    pass
    return


'''Function defined to display the information about all of the tasks that have been stored in the task file.
The task file is first opened with the mode set to 'r', allowing the program only to read from the file.
Readlines() is used to extract the data from the file, and the for loop splits the data into a list of seperate
items at each comma and space (", "). Finally, the information for each task is printed out in an easy-to-read
format using a multi-line fstring.'''

def view_all():
    
    task_file = open("tasks.txt", "r")
    lines = task_file.readlines()

        
    for line in lines:
        temp = line.split(", ")
            
            
        print(f'''
Task:            {temp[1]}
Assigned to:     {temp[0]}
Date assigned:   {temp[4]}
Due date:        {temp[3]}
Task complete?   {temp[5]}
Task description:
  {temp[2]}

  ''')

    task_file.close()
        
    pass
    return


'''Function defined to display the information related to all tasks assigned to the username that is currently
logged in. The task file is opened with the mode set to 'r', allowing the program only to read from the file.
The for loop loops through each line in the task file and splits the elements by the commas. Then the if statement
uses indexing to find the username in the task file that each task is assigned to and compares it with the username
that was entered in the login section. If the usernames match, the task details are printed out in an easy-to-read
format using a multi-line fstring.'''

'''In the second part of the 'vm' function, an empty list is created and then each task from the task file is added
as an item to the list. Input command is then used to get task choice from user and they are given the option to either
edit the task or mark is as complete. The for loop loops through the list of tasks and finds the one with the task name
that matches the one entered by the user, and then it stores the index of that task in a variable called 'taskNum', which
will be used to pop out the selected task later. If the user enters '-1', the information from the list of tasks is written
back to the file without any changes, and the user is returned to the previous menu.'''

'''If the user enters 'c' for mark as complete, the task is popped from the list using 'taskNum', the last index of the
selected task is changed to "Yes", and the task is appended back to the list. The list of tasks is then written back to the
task file with the newly changed information.'''

'''If the user enters 'e' to edit the task, first the program checks if the task has been completed. If the task is complete,
the information is written back to the file without any changes and the user is displayed a message that 'the task cannot be
edited as it is complete'. If the task has not been completed, it is popped in the same manner as above, the user is asked to
provide input to change the username and due date, and then the task is appended back to the list and the list of tasks is
written to the file with the newly changed information.'''

def view_mine():
    
    task_file = open("tasks.txt", "r")

    lines = task_file.readlines()
    
    for line in lines:
        temp = line.split(",")
            
        if username == temp[0]:
            print(f'''
Task:            {temp[1]}
Assigned to:      {temp[0]}
Date assigned:   {temp[4]}
Due date:        {temp[3]}
Task complete?   {temp[5]}
Task description:
  {temp[2]}
''')

    task_file.close()

    task_file = open("tasks.txt", "r")
    lines = task_file.readlines()
    task_file.close() 

    listTasks = []

    task_file = open("tasks.txt", "w")

    for line in lines:
        temp = line.split(", ")

        listTasks.append(temp)       

    taskChoice = input("Select a task or enter '-1' to return to the main menu: ")
    
    
    for i in listTasks:
        
        if taskChoice == i[1]:
            taskNum = listTasks.index(i)

            newChoice = input('''
What would you like to do to the task?
c - mark the task as complete
e - edit the task

''')

        elif taskChoice == "-1":
            
            for line in listTasks:
                task_file.write(f"{line[0]}, {line[1]}, {line[2]}, {line[3]}, {line[4]}, {line[5]}")
            
            return                       

    if newChoice == 'c':
   
        a = listTasks.pop(taskNum)
        a[-1] = "Yes\n"
        listTasks.append(a)
        
        print('''
Success!
''')

        for line in listTasks:
            task_file.write(f"{line[0]}, {line[1]}, {line[2]}, {line[3]}, {line[4]}, {line[5].strip()}\n")      

        with open("tasks.txt", "r") as file:                                    # To remove blank spaces in file
            for line in file:                                                  
                file.close()
                if not line.isspace():
                    with open("tasks.txt", "w") as file:
                        file.write(line)

        file.close()    

    elif newChoice == 'e':      
            
        for line in lines:
            temp = line.split(", ")

            if temp[1] == taskChoice:
                
                if temp[-1].strip() == "No":
            
                    a = listTasks.pop(taskNum)
                    a[0] = input("Enter the new username you would like to assign the task to: ")
                    a[3] = input("Enter the new due date for the task: ")
                    listTasks.append(a)
              
                    print('''
Success!
''')

                else:

                    for line in listTasks:
                        task_file.write(f"{line[0]}, {line[1]}, {line[2]}, {line[3]}, {line[4]}, {line[5].strip()}\n")
            
                    print('''
This task cannot be edited as it has already been completed.
''')
                    return

        for line in listTasks:
            task_file.write(f"{line[0]}, {line[1]}, {line[2]}, {line[3]}, {line[4]}, {line[5].strip()}\n")
    
        with open("tasks.txt", "r") as file:                                        # To remove blank spaces in file
            for line in file:
                file.close()
                if not line.isspace():
                    with open("tasks.txt", "w") as file:
                        file.write(line)

        file.close()
        
    task_file.close()
        
    pass
    return


'''If the user selects 's' (only available if the username is 'admin'), the program performs functions to count the
number of tasks and users in each respective file and display these stats as output. First, the task file is opened
with the mode set to 'r', allowing the program only to read from the file. The .readlines() function is used to extract
the data from the task file. The for loop uses the range() and len() functions to effectively provide a count of the
number of lines in the file. With one task per line, the count of the instance variable is taken as the number of tasks,
and the print statement uses an fstring to display this information. Finally, the exact same method is used to count the
number of users, although using the user file.'''

'''I added two for loops at the end of the view_stats function that loop through the contents of both the task_overview
file and the user_overview file and then print out each line to display the info to the user.'''

def view_stats():

    '''I looked up online how to use the os.path module to check whether a file exists. The if statement checks
    whether both the task_overview file and user_overview file exist, and calls the generate reports function if
    they have not yet been generated.'''

    if os.path.exists('task_overview.txt') != True and os.path.exists('user_overview.txt') != True:
        generate_reports()                                                                  
    
    task_file = open("tasks.txt", "r")
    lines = task_file.readlines()

    line = 0

    for line in range(len(lines)):
        line += 1

    print(f"Total number of tasks: {line}")
        
    task_file.close()

    user_file = open("user.txt", "r")
    lines = user_file.readlines()

    line = 0
        
    for line in range(len(lines)):
        line += 1
        
    print(f"Total number of users: {line}")
        
    user_file.close()
    
    task_overview_file = open("task_overview.txt", "r")

    lines = task_overview_file.readlines()

    print('''
Task overview:
''')

    for line in lines:
        line = line.strip()
        print(line)

    task_overview_file.close()

    user_overview_file = open("user_overview.txt", "r")

    lines = user_overview_file.readlines()

    print('''
User overview:
''')

    for line in lines:
        line = line.strip()
        print(line)

    user_overview_file.close()


# The 'generate reports' function is only displayed if admin is logged in

def generate_reports():

    # New file created (task_overview) and tasks file opened.

    task_overview_file = open("task_overview.txt", "w")             
    task_file = open("tasks.txt", "r")

    lines = task_file.readlines()

    # Variables created with values set to 0. Will be used to count number of uncompleted tasks, overdue tasks, etc.

    t = 0
    c = 0
    u = 0
    o = 0
    uo = 0

    '''The for loop splits the elements in the task file by the commas and spaces (", ") and adds 1 to the variable 't'
    which represents the total number of tasks. The if and elif statement checks whether or not the task is complete and
    adds 1 to the respective variable for total complete or uncomplete tasks ("c" or "u"). The second if statement checks
    whether the due date of the task is earlier than the current date, and adds 1 to the variable 'o', which represents
    total overdue tasks, if the due date has passed. Then, calculations are performed to compute each variable, and the
    information is printed to the task_overview_file.'''
    
    for line in lines:
        temp = line.split(", ")
        t += 1     
    
        if temp[-1].strip() == "Yes":
            c += 1
            
        elif temp[-1].strip() == "No":
            u += 1

        dueDate = datetime.datetime.strptime(temp[3], "%d %B %Y")
        today = datetime.datetime.today()
    
        if dueDate < today:
            o += 1

        pi = u / t * 100
        po = o / t * 100

    tasksGenerated = t
    completedTasks = c
    uncompletedTasks = u
    uncompletedOverdue = uo
    percentUncompleted = round(pi, 2)
    percentOverdue = round(po, 2)

    print('''
Success! Reports generated.
''')
    
    task_overview_file.write(f'''Total tasks generated and tracked: {tasksGenerated}
Total number of completed tasks: {completedTasks}
Total number of uncompleted tasks: {uncompletedTasks}
Total number of uncompleted and overdue tasks: {uncompletedOverdue}
Percentage of tasks uncompleted: {percentUncompleted}%
Percentage of tasks overdue: {percentOverdue}%''')

    task_overview_file.close()
    task_file.close()

    # New file created (user_overview) with mode set to write and task and user files opened with mode set to read only

    user_overview_file = open("user_overview.txt", "w")
    user_file = open("user.txt", "r")
    task_file = open("tasks.txt", "r")

    linesUser = user_file.readlines()
    linesTasks = task_file.readlines()

    '''The same method as above is used to perform calculations from the user and task files to compute the total
    percentages of tasks assigned to the user are overdue, incomplete, etc. Similar to above, once the totals and
    percentages have been computed, the information is written to the user_overview_file.'''

    u = 0
    t = 0

    for line in linesUser:
        u += 1

    for line in linesUser:
        temp = line.split(", ")
 
    # Variables created with values set to 0. Will be used to count number of uncompleted tasks, overdue tasks etc.

    tu = 0
    ut = 0
    ct = 0
    uo = 0

    for line in linesTasks:
        t += 1
        temp = line.split(", ")      
        
        if username == temp[0]:
            tu += 1
            
            if temp[-1].strip() == "Yes":
                ct += 1
                
            elif temp[-1].strip() == "No":
                ut += 1

        dueDate = datetime.datetime.strptime(temp[3], "%d %B %Y")
        today = datetime.datetime.today()
        
        if dueDate < today and temp[-1].strip() == "No":
            uo += 1

    # The try/except block accounts for the error that occurs when there are no tasks assigned to admin
    # I learned how to use try/except blocks from the HyperionDev Task 26 notes

    try:        
    
        ptu = tu / t * 100
        pct = ct / tu * 100
        put = ut / tu * 100
        puo = uo / tu * 100

    except ZeroDivisionError:

        pct = 0
        put = 0
        puo = 0

    totalUsers = u
    percentUserTasks = ptu
    percentUserComplete = pct
    percentUserUncomplete = put
    percentUncompleteOverdue = puo

    user_overview_file.write(f'''Total number of registered users: {totalUsers}
Total tasks generated and tracked: {tasksGenerated}
Percentage of total tasks assigned to user: {percentUserTasks}%
Percentage of tasks assigned to user that are complete: {percentUserComplete}%
Percentage of tasks assigned to user that must still be completed: {percentUserUncomplete}%
Percentage of tasks assigned to user that must still be completed and are overdue: {percentUncompleteOverdue}%''')
                     
    user_overview_file.close()
    user_file.close()
    task_file.close()

#=======================

'''The while loop presents the menu to the user and the .lower() function is used to make sure that the user's
input is converted to lower case'''

'''If the username entered in the login section is equal to 'admin', the user is displayed a menu with an added
option ('s') allowing them to view statistics. If the username entered is not equal to admin, the else statement
executes and the user is displayed the original menu without the 'display statistics' option.'''

while True:

    if username == 'admin':
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Add a task
va - View all tasks
vm - View my tasks
gr - Generate reports
s - Display statistics
e - Exit
: ''').lower()
        
    else:  
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Add a task
va - View all tasks
vm - view my tasks
e - Exit
: ''').lower()


    '''If and elif statements tell the program to perform a certain set of functions based on the option selected
    by the user from the above menu, and else statement executes if the user makes an invalid entry and prints an
    appropriate message.'''

   
# If and elif statements call the function corresponding to the user's input

    if menu == 'r':
        reg_user()      

    elif menu == 'a':
        add_task()          

    elif menu == 'va':
        view_all()

    elif menu == 'vm':
        view_mine()


    elif menu == 'gr':
        generate_reports()   


    elif menu == 's':
        view_stats()
    
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please try again")
