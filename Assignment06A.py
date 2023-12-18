
# ----------------------------------------------------------- #
# Title: Assignment06
# Description: Using functions, classes, and separation of concerns programming pattern
# ChangeLog: (Who, When, What)
# ZVelagic,11/20/2023,Created Script
#--------------------------------------------------------------#

# imports

import json
from dataclasses import dataclass
# from pathlib import Path
from typing import List, Dict
import io as _io

# Defining data constants

MENU: str = """
---- Course Registration Program ----
Select from the following menu:
  1. Register a Student for a Course
  2. Show current data
  3. Save data to a file
  4. Exit the program
-----------------------------------------
"""
FILE_NAME = "Enrollments.json"

#student_data: List[Dict]

# Defining variables

student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.

student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
csv_data: str = ''  # Holds combined string data separated by a comma.
json_data: str = ''  # Holds combined string data in a json format.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.


# Defining functions and classes

@dataclass
class Student:
    first_name: str
    last_name: str
    courses: str

# Class FileProcessor
class FileProcessor:
    """Handles reading and writing data to files."""

    @staticmethod
    def read_data_from_file(file_name: str) -> List[Dict]:
        """Reads data from a JSON file into a list of dictionaries."""
        data = []

        try:
            with open(file_name, 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            print(f"File not found: {file_name}")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from file: {file_name}")

        return data

    @staticmethod
    def write_data_to_file(file_name: str, data: List[Dict]):
        """Writes data from a list of dictionaries into a JSON file."""
        try:
            with open(file_name, 'w') as f:
                json.dump(data, f, indent=2)
            print(f"Data saved to file: {file_name}")
        except IOError:
            print(f"Error writing to file: {file_name}")

# Class IO -------------------------------------------------#
class IO:
    """Handles input and output."""

    @staticmethod
    def output_menu(menu: str):
        """Outputs the program menu."""
        print(menu)

    @staticmethod
    def input_menu_choice() -> str:
        """Gets a menu choice from the user."""
        return input("What would you like to do: ")

    @staticmethod
    def output_student_courses(student_data: List[Dict]):
        """Outputs the student course data."""
        if not student_data:
            print("No student course data found!")
            return

        print("\nStudent Course Registrations")
        print("-" * 30)
        for student in student_data:
            print(f"{student['first_name']} {student['last_name']} is registered for {student['courses']}")

    @staticmethod
    def input_student_data(student_data: List[Dict]):
        """Get student data from the user."""
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        course = input("Enter course: ")

        student_data.append({
            "first_name": first_name,
            "last_name": last_name,
            "courses": course
        })


@staticmethod
def output_error_messages(message: str, error: Exception = None):
    """Outputs an error message."""
    print(f"Error: {message}")
    if error:
        print(error)


def main():
    """Main program loop."""

    menu_choice = ""
    student_data = []

    try:
        # Load initial data from file
        student_data = FileProcessor.read_data_from_file(FILE_NAME)
    except Exception as e:
        IO.output_error_message("Error loading data from file.", e)


    while menu_choice != "4":

        IO.output_menu(MENU)
        menu_choice = IO.input_menu_choice()

# Input user data

        if menu_choice == "1":
            IO.input_student_data(student_data)
            print("Option One : ", student_data)

        elif menu_choice == "2":
            IO.output_student_courses(student_data)

        elif menu_choice == "3":
            try:
                print("Option three: ", student_data)
                FileProcessor.write_data_to_file(FILE_NAME, student_data)
            except Exception as e:
                IO.output_error_message("Error saving data to file.", e)

        elif menu_choice != "4":
            print("Invalid menu choice. Please try again.")

    print("Goodbye!")

if __name__ == "__main__":
    main()