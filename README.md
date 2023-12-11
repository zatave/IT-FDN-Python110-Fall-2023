# Creating Applications

## Ovierview 

This assignment will demonstrate multi-module applications in Python. 

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



# Unit Test Script for presentation_classes.IO

## Description
This script holds unit tests for methods within the `IO` class from the `presentation_classes` module. the tests cover input and ouput funcions for error messages, menu output, and processing input of employee data. 

```python
import unittest
from unittest.mock import patch
from presentation_classes import IO
from data_classes import Employee

# Unit Test Script for IO Class

## Description:
This script contains unit tests for the `IO` class methods. The `IO` class is responsible for handling input and output operations related to employee data and error messages.

```python
import unittest
from unittest.mock import patch
from presentation_classes import IO
from data_classes import Employee



### 1. `test_output_error_messages`
   - **Description:** Tests the `output_error_messages` method.
   - **Setup:** Initializes an instance of the `IO` class and an empty list for employee data.
   - **Test Steps:**
     1. Calls `output_error_messages` with a sample error message.
     2. Asserts that the `print` function is called once with the correct parameters.

### 2. `test_output_error_messages_with_exception`
   - **Description:** Tests the `output_error_messages` method with an exception.
   - **Setup:** Initializes an instance of the `IO` class and an empty list for employee data.
   - **Test Steps:**
     1. Calls `output_error_messages` with a sample error message and an exception.
     2. Constructs the expected output and asserts that the `print` function is called once with the correct parameters.

### 3. `test_output_menu`
   - **Description:** Tests the `output_menu` method.
   - **Setup:** Initializes an instance of the `IO` class and an empty list for employee data.
   - **Test Steps:**
     1. Calls `output_menu` with a sample menu string.
     2. Asserts that the `print` function is called once with the correct parameters.

### 4. `test_input_menu_choice`
   - **Description:** Tests the `input_menu_choice` method.
   - **Setup:** Initializes an instance of the `IO` class and an empty list for employee data.
   - **Test Steps:**
     1. Uses the `input` function to simulate user input ("2").
     2. Calls `input_menu_choice` and asserts that the returned value matches the expected input.

### 5. `test_input_menu_choice_invalid_choice`
   - **Description:** Tests the `input_menu_choice` method with invalid user input.
   - **Setup:** Initializes an instance of the `IO` class and an empty list for employee data.
   - **Test Steps:**
     1. Uses the `input` function to simulate user input ("5").
     2. Calls `input_menu_choice` and asserts that the returned value matches the expected input.
     3. Asserts that the `print` function is called once with a specific error message.

### 6. `test_output_employee_data`
   - **Description:** Tests the `output_employee_data` method.
   - **Setup:** Initializes an instance of the `IO` class and an empty list for employee data.
   - **Test Steps:**
     1. Creates a sample list of `Employee` objects.
     2. Calls `output_employee_data` with the sample employee data.
     3. Constructs the expected output and asserts that the `print` function is called once with the correct parameters.

### 7. `test_input_employee_data`
   - **Description:** Tests the `input_employee_data` method with valid input.
   - **Setup:** Initializes an instance of the `IO` class and an empty list for employee data.
   - **Test Steps:**
     1. Uses the `input` function to simulate user input for a new employee.
     2. Calls `input_employee_data` and asserts the correctness of the returned employee data.

### 8. `test_input_employee_data_value_error`
   - **Description:** Tests the `input_employee_data` method with invalid input (e.g., invalid rating).
   - **Setup:** Initializes an instance of the `IO` class and an empty list for employee data.
   - **Test Steps:**
     1. Uses the `input` function to simulate user input with invalid data.
     2. Calls `input_employee_data` and asserts that the returned employee data is empty.
     3. Asserts that the `print` function is called once with a specific error message.

### 9. `test_input_employee_data_generic_exception`
   - **Description:** Tests the `input_employee_data` method with a generic exception.
   - **Setup:** Initializes an instance of the `IO` class and an empty list for employee data.
   - **Test Steps:**
     1. Uses the `input` function to simulate user input for a new employee.
     2. Calls `input_employee_data` and asserts that the returned employee data is empty.
     3. Asserts that the `print` function is called once with a specific error message.

## Running the Tests
The script includes the standard `unittest.main()` block to execute the test cases when the script is run.

```python
if __name__ == "__main__":
    unittest.main()


# FileProcessor Unit Test Script

This script contains unit tests for the `FileProcessor` class, which is responsible for reading and writing employee data to and from a JSON file. The script uses the `unittest` framework.

# File Processor Test Suite

This script defines a test suite for the `FileProcessor` class, which is responsible for reading and writing employee data to and from a JSON file.

```python
import unittest
import json
from unittest.mock import mock_open, patch
from data_classes import Employee
from processing_classes import FileProcessor

class TestFileProcessor(unittest.TestCase):
    def setUp(self):
        # Set up common variables for tests
        self.file_name = 'EmployeeRatings.json'
        self.employee_data = []




### `test_read_employee_data_from_file`
-  Tests the successful reading of employee data from a JSON file.
- **Steps:**
  1. Mock the `open` function and provide JSON data.
  2. Call `FileProcessor.read_employee_data_from_file`.
  3. Validate the returned employee data.

### `test_read_employee_data_from_file_file_not_found`
-  Tests the case where the specified file is not found.
- **Steps:**
  1. Try to read employee data from a nonexistent file.
  2. Expect a `FileNotFoundError` to be raised.

### `test_read_employee_data_from_file_generic_exception`
- Tests the case where a generic exception occurs during file reading.
- **Steps:**
  1. Mock the `open` function to raise an exception.
  2. Call `FileProcessor.read_employee_data_from_file`.
  3. Expect the raised exception to be caught.

### `test_write_employee_data_to_file`
- Tests the successful writing of employee data to a JSON file.
- **Steps:**
  1. Mock the `open` function.
  2. Call `FileProcessor.write_employee_data_to_file`.
  3. Validate that the file is opened with the correct parameters.
  4. Validate that the data is written to the file.

### `test_write_employee_data_to_file_type_error`
-  Tests the case where a `TypeError` occurs during file writing.
- **Steps:**
  1. Mock the `open` function and simulate a `TypeError` during writing.
  2. Call `FileProcessor.write_employee_data_to_file`.
  3. Expect a `TypeError` to be raised.

### `test_write_employee_data_to_file_permission_error`
- Tests the case where a `PermissionError` occurs during file writing.
- **Steps:**
  1. Mock the `open` function and simulate a `PermissionError` during writing.
  2. Call `FileProcessor.write_employee_data_to_file`.
  3. Expect a `PermissionError` to be raised.

### `test_write_employee_data_to_file_generic_exception`
- Tests the case where a generic exception occurs during file writing.
- **Steps:**
  1. Mock the `open` function and simulate a generic exception during writing.
  2. Call `FileProcessor.write_employee_data_to_file`.
  3. Expect the raised exception to be caught.

## Execution
- Executes the unit tests if the script is run as the main module.
- **Steps:**
  1. Run unit tests using `unittest.main()`.



