# Employee Ratings Management

This script manages employee ratings using a simple menu-driven interface.

    FILE_NAME: str = 'EmployeeRatings.json'
    
    MENU: str = '''
    ---- Employee Ratings ------------------------------
      Select from the following menu:
        1. Show current employee rating data.
        2. Enter new employee rating data.
        3. Save data to a file.
        4. Exit the program.
    --------------------------------------------------
    '''

FILE_NAME: This variable stores the name of the file ('EmployeeRatings.json') where employee data will be read from and saved to.

MENU: A multiline string representing the menu options for the user interface. This will be displayed to the user so they can choose an action.

employees: An empty list that will be used to store employee data. This list will be populated as the program runs.

menu_choice: A variable initialized to an empty string, which will be used to store the user's menu choice.

Main Body Section
# Beginning of the main body of this script
        employees = FileProcessor.read_employee_data_from_file(file_name=FILE_NAME,
                                                       employee_data=employees,
                                                       employee_type=Employee)  # Note this is the class name (ignore the warning)

# Repeat the following tasks
while True:
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":  # Display current data
        try:
            IO.output_employee_data(employee_data=employees)
        except Exception as e:
            IO.output_error_messages(e)
        continue

    elif menu_choice == "2":  # Get new data (and display the change)
        try:
            employees = IO.input_employee_data(employee_data=employees, employee_type=Employee)  # Note this is the class name (ignore the warning)
            IO.output_employee_data(employee_data=employees)
        except Exception as e:
            IO.output_error_messages(e)
        continue

    elif menu_choice == "3":  # Save data to a file
        try:
            FileProcessor.write_employee_data_to_file(file_name=FILE_NAME, employee_data=employees)
            print(f"Data was saved to the {FILE_NAME} file.")
        except Exception as e:
            IO.output_error_messages(e)
        continue

    elif menu_choice == "4":  # End the program
        break  # out of the while loop

The script begins by reading existing employee data from a file using FileProcessor.read_employee_data_from_file. The data is stored in the employees list.

The script then enters a while True loop, creating a simple menu-driven interface that repeatedly prompts the user for input.

Menu Display and User Input Handling:

IO.output_menu(menu=MENU): This function displays the menu to the user.
menu_choice = IO.input_menu_choice(): Takes user input to select a menu option.
Menu Option Handling:

Option "1": Displays the current employee data using IO.output_employee_data. It includes exception handling to catch and display any errors that may occur during the output.
Option "2": Allows the user to input new employee data using IO.input_employee_data and then displays the updated data. Again, includes exception handling.
Option "3": Saves the current employee data to the file using FileProcessor.write_employee_data_to_file and informs the user about the successful operation. Exception handling is included.
Option "4": Breaks out of the while loop, ending the program.
This script essentially provides a user-friendly interface for managing employee ratings, with options to view, input, and save data. Error handling is implemented to ensure that any issues encountered during file operations or data display are gracefully handled.
