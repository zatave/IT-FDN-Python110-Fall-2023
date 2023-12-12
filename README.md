
# Creating Application
## Employee Ratings 

## Overview/Introduction

This program demonstrates a multi-module application, showing user (employee) rating data using menu selection. This application interacts with the user, to display data, enter user data, and save user data. This application is organized into three classes: `Person` and`Employee` (data class), `IO` (Input/Output presentation class), and `FileProcessor` (Processing class).

## Constants
### Defining constants 

- `FILE_NAME`: Name of the file ('EmployeeRatings.json') where employee data is stored.
- `MENU`: Menu options presented to the user.

## Variables
### Defining variables 

- `employees`: List stores employee data.
- `menu_choice`: User's menu choice.

## Main Body

1. **Data Initialization:**
   - Reads existing employee data from the file using `FileProcessor.read_employee_data_from_file`.

2. **Menu Loop:**
   - Presents the user with a menu using `IO.output_menu`.
   - Reads the user's menu choice using `IO.input_menu_choice`.
   - Executes actions based on the user's choice:
      - "1": Displays current employee data.
      - "2": Allows the user to enter new employee data and displays the updated data.
      - "3": Saves the current data to the file using `FileProcessor.write_employee_data_to_file`.
      - "4": Exits the program.

3. **Exception Handling:**
   - Catches and displays any exceptions that may occur during data processing or user interaction.

    
#### Data Initialization
      
      - Imports the `FileProcessor` and `Employee` classes.
      - Defines a constant `FILE_NAME` with the name of the file ('EmployeeRatings.json') where employee data is stored.
      - Initializes an empty list `employees` to store employee data.

#### IO Class Initialization

      - Initializes an instance of the `IO` class.

#### Employee Data Initialization

      - Reads existing employee data from the file using `FileProcessor.read_employee_data_from_file`.


# Person and Employee Classes

## Person Class

The Person class to represent user basic personal information.

### Properties

- `first_name` (str): The person's first name.
- `last_name` (str): The person's last name.

### Methods

- `__init__(self, first_name: str = "", last_name: str = "")`: Initializes the `Person` object with provided values.
- `__str__(self) -> str`: Returns a string representation of the user's full name.

### Property Methods

- `first_name`: Ensures the first name contains only alphabetical characters.
- `last_name`: Ensures the last name contains only alphabetical characters.

## Employee Class

The Employee class represents user (employee) data, inherits the `Person` class.

### Additional Properties

- `review_date` (date): The date of the employee's review.
- `review_rating` (int): The review rating of the employee's performance (1-5).

### Methods

- `__init__(self, first_name: str = "", last_name: str = "", review_date: str = "1900-01-01", review_rating: int = 3)`: Initializes the `Employee` object with default or provided values.
- `__str__(self) -> str`: Returns a string representation of the employee's information.

### Property Methods

- `review_date`: Ensures the review date is in the correct format (YYYY-MM-DD).
- `review_rating`: Ensures the review rating is within the valid range (1-5).




# IO Class (Presentation class)
## IO Class
A collection of presentation layer functions that manages user input and output.

### Methods

- `output_error_messages(message: str, error: Exception = None)`: Displays custom error messages to the user, along with any technical error details.
- `output_menu(menu: str)`: Displays a menu of choices to the user.
- `input_menu_choice() -> str`: Gets a menu choice from the user.
- `output_employee_data(employee_data: list)`: Displays employee data, including ratings, to the user.
- `input_employee_data(employee_data: list, employee_type: Employee) -> list`: Gets employee data (first name, last name, review date, and review rating) from the user and appends it to the `employee_data` list.


# FileProcessor Class (Processing Class)

The FileProcessor class is a collection of processing layer functions that work with a JSON files.

### Methods

#### `read_employee_data_from_file(file_name: str, employee_data: list, employee_type: Employee) -> list`

This function reads data from a JSON file and loads it into a list of `Employee` objects.

**Parameters:**
- `file_name` (str): Name of the file to read from.
- `employee_data` (list): List of `Employee` objects to be filled with file data.
- `employee_type` (Employee): A reference to the `Employee` class.

**Returns:** List of `Employee` objects.

#### `write_employee_data_to_file(file_name: str, employee_data: list)`

This function writes data to a JSON file with data from a list of `Employee` objects.

**Parameters:**
- `file_name` (str): Name of the file to write to.
- `employee_data` (list): List of `Employee` objects to be written to the file.

**Returns:** None.

# TestEmployee Unittest
## Import datetime 
This script imports the necessary modules of unittest, date from datetime, and employee class from data_classes.
This module tests data_classes for Employee class. 
import unittest
from datetime import date
from data_classes import Employee

## Test employee class definition
This class holds the test method and defines a test class that is named TestEmployee and it inherits from unittest.TestCase.

class TestEmployee(unittest.TestCase):

## Test Cases
test_init method creates an instance of the Employee class and specifies attributes and that they match the expected values.
This ensures that the class's initialization works as intended. The test_review_date_setter method tests the setter for the review_date attribute. 
The ValueError will test for invalid date. 

def test_init(self):
    employee = Employee("John", "Doe", "2021-01-01", 4)
    self.assertEqual(employee.first_name, "John")
    self.assertEqual(employee.last_name, "Doe")
    self.assertEqual(employee.review_date, "2021-01-01")
    self.assertEqual(employee.review_rating, 4)

def test_review_date_setter(self):
    employee = Employee()
    employee.review_date = "2021-01-01"
    self.assertEqual(employee.review_date, "2021-01-01")

    with self.assertRaises(ValueError):
        employee.review_date = "2021-13-01"

This method tests the setter for the review_rating attribute. Tests a rating and checks if it was set correctly. 

def test_review_rating_setter(self):
    employee = Employee()
    employee.review_rating = 4
    self.assertEqual(employee.review_rating, 4)

    with self.assertRaises(ValueError):
        employee.review_rating = 6

This method tests the calling str() and that it provides the expected string. 

def test_str(self):
    employee = Employee("John", "Doe", "2021-01-01", 4)
    self.assertEqual(str(employee), "John,Doe,2021-01-01,4")

This method runs tests when the program is applied in the main module. 
if __name__ == "__main__":
    unittest.main()


# Unit Test for presentation_classes.IO

This program script contains unit tests for the methods in the `IO` presentation class from the `presentation_classes` module. The `IO` class handles the input and output in the application. 
This script holds unit tests for methods within the IO class from the presentation_classes module. the tests cover input and ouput funcions for error messages, menu output, and processing input of employee data.

import unittest
from unittest.mock import patch
from presentation_classes import IO
from data_classes import Employee

# Unit Test for IO Class

## Description:
This script contains unit tests for the `IO` class methods. The `IO` class is responsible for handling input and output operations related to employee data and error messages.

```python
import unittest
from unittest.mock import patch
from presentation_classes import IO
from data_classes import Employee
```

### 1. `test_output_error_messages`
   - Tests the `output_error_messages` method.
   - **Setup:** Initializes an instance of the `IO` class and an empty list for employee data.
   - **Test:**
     1. Calls `output_error_messages` with a sample error message.
     2. Asserts that the `print` function is called once with the correct parameters.

### 2. `test_output_error_messages_with_exception`
   - Tests the `output_error_messages` method with an exception.
   - **Setup:** Initializes an instance of the `IO` class and an empty list for employee data.
   - **Test:**
     1. Calls `output_error_messages` with a sample error message and an exception.
     2. Constructs the expected output and asserts that the `print` function is called once with the correct parameters.

### 3. `test_output_menu`
   - Tests the `output_menu` method.
   - **Setup:** Initializes an instance of the `IO` class and an empty list for employee data.
   - **Test:**
     1. Calls `output_menu` with a sample menu string.
     2. Asserts that the `print` function is called once with the correct parameters.

### 4. `test_input_menu_choice`
   - Tests the `input_menu_choice` method.
   - **Setup:** Initializes an instance of the `IO` class and an empty list for employee data.
   - **Test:**
     1. Uses the `input` function to simulate user input ("2").
     2. Calls `input_menu_choice` and asserts that the returned value matches the expected input.

### 5. `test_input_menu_choice_invalid_choice`
   - Tests the `input_menu_choice` method with invalid user input.
   - **Setup:** Initializes an instance of the `IO` class and an empty list for employee data.
   - **Test:**
     1. Uses the `input` function to simulate user input ("5").
     2. Calls `input_menu_choice` and asserts that the returned value matches the expected input.
     3. Asserts that the `print` function is called once with a specific error message.

### 6. `test_output_employee_data`
   -  Tests the `output_employee_data` method.
   - **Setup:** Initializes an instance of the `IO` class and an empty list for employee data.
   - **Test:**
     1. Creates a sample list of `Employee` objects.
     2. Calls `output_employee_data` with the sample employee data.
     3. Constructs the expected output and asserts that the `print` function is called once with the correct parameters.

### 7. `test_input_employee_data`
   - Tests the `input_employee_data` method with valid input.
   - **Setup:** Initializes an instance of the `IO` class and an empty list for employee data.
   - **Test:**
     1. Uses the `input` function to simulate user input for a new employee.
     2. Calls `input_employee_data` and asserts the correctness of the returned employee data.

### 8. `test_input_employee_data_value_error`
   - Tests the `input_employee_data` method with invalid input (e.g., invalid rating).
   - **Setup:** Initializes an instance of the `IO` class and an empty list for employee data.
   - **Test:**
     1. Uses the `input` function to simulate user input with invalid data.
     2. Calls `input_employee_data` and asserts that the returned employee data is empty.
     3. Asserts that the `print` function is called once with a specific error message.

### 9. `test_input_employee_data_generic_exception`
   - Tests the `input_employee_data` method with a generic exception.
   - **Setup:** Initializes an instance of the `IO` class and an empty list for employee data.
   - **Tests:**
     1. Uses the `input` function to simulate user input for a new employee.
     2. Calls `input_employee_data` and asserts that the returned employee data is empty.
     3. Asserts that the `print` function is called once with a specific error message.

### Running the Tests
The script includes the standard `unittest.main()` block to execute the test cases when the script is run.

```python
if __name__ == "__main__":
    unittest.main()
```

# FileProcessor Unit Test 

This script holds a unit tests for the `FileProcessor` class. This class reads and writes the employee user data to and from a JSON file. 

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
```

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


# Summary
This program is a multi-module application to show user data using menu selection system. This application takes user input, displays data, and saves the user data to a JSON file. 

