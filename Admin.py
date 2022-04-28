from User import User
from Course import Course


class Admin(User):

    # Admin class that is a child of the User class. It has no additional
    # instance variables outside of inheritance
    # Provides the methods used in the admin section outlined in the main module

    def __init__(self, id, pin):
        User.__init__(self, id, pin)

    def show_roster(self, c_list):

        # This function displays the roster for a given course
        # It takes a list of Course objects as an argument
        # Asks the admin to enter a course to display
        # Then iterates through the course list to check if the course is valid
        # If the course is valid, calls the display_roster with the entered course
        # It has no return value

        course_choice = input('Please enter course: ')

        for course in c_list:
            if course_choice == course.get_course_code():
                Course.display_roster(course)
                break
        else:
            print('Course,', course_choice + ", not available.")

    def change_max_size(self, c_list):

        # This function allows the admin to adjust the maximum course size
        # It takes a list of Course objects as an argument
        # Asks the admin to enter a course
        # Then iterates through the course list to check if the course is valid
        # If the course is valid, calls the change_max_size method with the entered course
        # It has no return value

        course_choice = input('Please enter course to change: ')

        for course in c_list:
            if course_choice == course.get_course_code():
                Course.change_max_size(course)
                break
        else:
            print('Course,', course_choice + ', not available.')
