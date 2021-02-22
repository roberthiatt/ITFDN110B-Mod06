# -------------------------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
#                           RRoot,1.1.2030,Created starter script
#                           RHiatt,2.16.2021,Added code to complete Assignment05
#                           RHiatt,2.21.2021,Incorporated RRoot's Assignment06 code & modified
# -------------------------------------------------------------------------------------------- #

#objFile = open("C:\Python\_PythonClass\Assignment06\ToDoList.txt", "a") #Removed. Unnecessary. RHiatt 2/21/21

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
file_name = "C:\Python\_PythonClass\Assignment06\ToDoList.txt" # The name of the data file
objFile = None  # An object that represents a file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = ""  # Captures the user option selection
strTask = ""  # Captures the user task data
strPriority = ""  # Captures the user priority data
strStatus = ""  # Captures the status of an processing functions


# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows
        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  # clear current data
        file = open(file_name, "r")
        for line in file:
            task, priority = line.split(",")
            row = {"Task": task.strip(), "Priority": priority.strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows, 'Success'

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        """ Create a new row of data in a dictionary and pass it to a list
        :param task: (string) name of task:
        :param priority:(string) priority number:
        :param list_of_rows: (list) you want filled with new data:
        :return: (list) of dictionary rows
        """
        #Adding doc strings is a best practice!
        #ctrl + q to activate the process
        row_add = {"Task": task, "Priority": priority}
        list_of_rows.append(row_add)
        return list_of_rows, 'Success'

    @staticmethod
    def remove_data_from_list(task, list_of_rows):
        """ Remove a dictionary row of data in a list
        :param task: (string) name of task:
        :param list_of_rows: (list) you want to remove the data:
        :return: (list) of dictionary rows
        """
        for row_remove in list_of_rows:
            if row_remove["Task"] == task:
                list_of_rows.remove(row_remove)
                print("You have removed the unwanted task.")
        return list_of_rows, 'Success'

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """ Write a list of dictionary row to the file
        :param file_name: (string) the text file you want to write data:
        :param list_of_rows: (list) the data you want to write in the filr:
        :return: (list) of dictionary rows
        """
        objFile = open(file_name, "w")
        for row_write in list_of_rows:
            objFile.write(row_write["Task"] + ", " + row_write["Priority"] + "\n")
        print("Your data is saved!")
        objFile.close()
        return list_of_rows, 'Success'


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod #directive used with classes; discussed more fully in a later module
    def print_menu_Tasks():
        """  Display a menu of choices to the user
        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Reload Data from File
        5) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user
        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_Tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows
        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print() # Add an extra line for looks
        print("******* The current To-Do Tasks are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("********************************************")
        #print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user
        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing
        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_task_and_priority():
        """ Get user input for task and priority to be added
        :param strTask: (string) the new task:
        :param strPriority: (string) the priority:
        :return: priority and task (string)
        """
        global strTask
        strTask= input("Enter Task: ")
        global strPriority
        strPriority = input("Enter Priority: ")
        return strTask, strPriority

    @staticmethod
    def input_task_to_remove():
        """ Get user input for task to be removed
        :param strTask: (string) the new task:
        :return: task (string)
        """
        global strTask
        strTask = input("Enter Task to remove: ").strip()
        return strTask


# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
Processor.read_data_from_file(file_name, lstTable)  # read file data

# Step 2 - Display a menu of choices to the user
while (True):
    # Step 3 Show current data
    IO.print_current_Tasks_in_list(lstTable)  # Show current data in the list/table
    IO.print_menu_Tasks()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if strChoice.strip() == '1':  # Add a new Task
        IO.input_new_task_and_priority()
        Processor.add_data_to_list(strTask,strPriority,lstTable)
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '2':  # Remove an existing Task
        IO.input_task_to_remove()
        Processor.remove_data_from_list(strTask, lstTable)
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '3':  # Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to your file? (y/n) - ")
        if strChoice.lower() == "y":
            Processor.write_data_to_file(file_name, lstTable)
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif strChoice == '4':  # Reload Data from File
        print("Warning: Unsaved Data Will Be Lost!")
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")
        if strChoice.lower() == 'y':
            Processor.read_data_from_file(file_name, lstTable)
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("File Reload Cancelled!")
        continue  # to show the menu

    elif strChoice == '5':  # Exit Program
        print("Thank you for your time. Have a nice day!")
        break  # and Exit