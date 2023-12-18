
#---------------------------------------------------------------------------------#
# Title: Assignment05
# Desc: This assignment demonstrates using dictinaries, exceptions, and JSON file
# Change Log: (Who, When, What)
#   ZVelagic,11/12/23,Created Script
#---------------------------------------------------------------------------------#

import json

FILE_NAME: str = "data.json"
student_first_name: str = ""
student_last_name: str = ""
course_name: str = ""
student_data = dict()
students: list = []
csv_data: str = ""
file = None
menu_choice: str

MENU: str = ""

file = open(FILE_NAME, "r")
data = json.load(file)
for student in data:
    print(f"Student: {student["student_first_name"]}, {student["student_last_name"]}, {student["course_name"]}")

while True:
    print("--- Course Registration Program ----")
    print("Select from the following menu:")
    print("1.Register a Student for a Course")
    print("2.Show current data")
    print("3.Save data to a file")
    print("4.Exit the program")
    menu_choice = input("What would you like to do: ")

    menu_choice = int(menu_choice)
    if menu_choice == 1: #----------------- this is menu choice 1 ---------------
        #student_first_name = input("Enter the student's first name: ")

        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
        except ValueError as e:
            print(e)
            print("--Technical Error Message --")
            print(e._doc_)
            print(e._str_())
        except Exception as e:
            print("There was a non-specific error!\n")
            print("Built-In Python error info: ")
            print(e, e._doc_, type(e), sep="\n")

        #student_last_name = input("Enter the student's last name: ")

        try:
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
        except ValueError as e:
            print(e)
            print("--Technical Error Message --")
            print(e._doc_)
            print(e._str_())
        except Exception as e:
            print("There was a non-specific error!\n")
            print("Built-In Python error info: ")
            print(e, e._doc_, type(e), sep="\n")

        course_name = input("Please enter the name of the course: ")
        #print(type(student_data))
        student_data["student_first_name"] = student_first_name
        student_data["student_last_name"] = student_last_name
        student_data["course_name"] = course_name

        # student_data = [student_first_name, student_last_name, course_name]
        students.append(student_data.copy())
        print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        student_data.clear()
        continue

    elif menu_choice == 2: #----------------- this is menu choice 2 ---------------
        try:
            file = open("data.json", "r")
            data = json.load(file)
            for student in data:
               print(f"Student: {student["student_first_name"]}, {student["student_last_name"]}, {student["course_name"]}")
        except ZeroDivisionError as e:
            print("Please do not use Zero for the second number!\n")
            print("Built-In Python error info: ")
            print(e, e._doc_, type(e), sep="\n")
        except FileNotFoundError as e:
            print("Text file must exist before running this script!]\n")
            print(e, e._doc_, type(e), sep= "\n")
        except Exception as e:
            print("There was a non-specific error!\n")
            print("Built-In Python error info: ")
            print(e, e._doc_, type(e), sep="\n")

    elif menu_choice == 3: #----------------- this is menu choice 3 ---------------
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file)
            file.close()
            continue
        except TypeError as e:
            print("Please check that the data is a valid JSON format \n")
            print("--Technical Error Message __")
            print(e, e._doc_, type(e), sep="\n")
        except Exception as e:
            print("--Technical Error Message--")
            print("Built-In Python error info: ")
            print(e, e._doc_, type(e), sep= "\n")
        finally:
            if file.closed == False:
                file.close()

    elif menu_choice == 4: #----------------- this is menu choice 4 ---------------
        break
    else:
        print("Please only choose option 1, 2, or 3")
        print("Program Ended")


