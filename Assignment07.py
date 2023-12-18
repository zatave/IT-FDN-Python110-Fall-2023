# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: This assignment demonstrates using data classes
# with structured error handling
# Change Log: (Who, When, What)
#   ZVelagic,11/27/2023,Created Script
# ------------------------------------------------------------------------------------------ #
import json

# Defining Data Constants

MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''

FILE_NAME: str = "Enrollments.json"

# Defining Data Variables

students: list = []  # a table of student data
menu_choice: str  # Hold the choice made by the user.

#Create Person class
class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, fn):
        self.first_name = fn

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, ln):
        self.last_name = ln

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

#Create Student Class

class Student(Person):
    def __int__(self, fn, ln, cn):
        super().__init__(fn, ln)
        self.course_name = cn

    def get_course_name(self):
        return self.course_name

    def set_course_name(self, cn):
        self.course_name = cn

    def __str__(self):
        return f"{self.first_name} {self.last_name} is register for {self.course_name}"


# Processing --------------------------------------- #
class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
    ZVelagic,11.27.2023,Created Class
    """

    """ This function reads data from a json file and loads it into a list of dictionary rows

            ChangeLog: (Who, When, What)
            ZVelagic,11.27.2023,Created function

            :param file_name: string data with name of file to read from
            :param student_data: list of dictionary rows to be filled with file data

            :return: list
            """
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):

        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with reading the file.", error=e)

        finally:
            if file.closed == False:
                file.close()
        return student_data

    """ This function writes data to a json file with data from a list of dictionary rows

           ChangeLog: (Who, When, What)
           ZVelagic,11.23.2023,Created function

           :param file_name: string data with name of file to write to
           :param student_data: list of dictionary rows to be writen to the file

           :return: None
           """
    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):

        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
            IO.output_student_and_course_names(student_data=student_data)
        except Exception as e:
            message = "Error: There was a problem with writing to the file.\n"
            message += "Please check that the file is not open by another program."
            IO.output_error_messages(message=message,error=e)
        finally:
            if file.closed == False:
                file.close()


# Presentation --------------------------------------- #
class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    ZVelagic,11.27.2023,Created Class
    Added menu output and input functions
    Added a function to display the data
    Added a function to display custom error messages
    """

    """ This function displays the a custom error messages to the user

           ChangeLog: (Who, When, What)
           ZVelagic, 11.27.2023,Created function

           :param message: string with message data to display
           :param error: Exception object with technical message to display

           :return: None
           """
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):

        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):

        print()  # Adding extra space to make it look nicer.
        print(menu)
        print()  # Adding extra space to make it look nicer.

    """ This function displays the menu of choices to the user

           ChangeLog: (Who, When, What)
           ZVelagic, 11.27.2023,Created function

           :return: None
           """

    """ This function gets a menu choice from the user

            ChangeLog: (Who, When, What)
            ZVelagic, 11.27.2023,Created function

            :return: string with the users choice
            """
    @staticmethod
    def input_menu_choice():

        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1","2","3","4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing e to avoid the technical message

        return choice

    @staticmethod
    def output_student_and_course_names(student_data: list):
        """ This function displays the student and course names to the user

        ChangeLog: (Who, When, What)
        ZVelagic, 11.27.2023,Created function

        :param student_data: list of dictionary rows to be displayed

        :return: None
        """

        print("-" * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)

    """ This function gets the student's first name and last name, with a course name from the user

           ChangeLog: (Who, When, What)
           ZVelagic, 11.27.2023,Created function

           :param student_data: list of dictionary rows to be filled with input data

           :return: list
           """
    @staticmethod
    def input_student_data(student_data: list):

        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            student_data.append(student)
            print()
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages(message="One of the values was the correct type of data!", error=e)
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with your entered data.", error=e)
        return student_data


# Start of main body

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Present and Process the data
while (True):

    # Present the menu of choices
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice() # function/method


    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        students = IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_and_course_names(students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
