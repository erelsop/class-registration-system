from User import User
from Course import Course


class Student(User):

    # Student class that is a child of the User class. It has no additional
    # instance variables outside of inheritance
    # Provides the methods used in the student session outlined in the main module

    def __init__(self, id, pin):
        User.__init__(self, id, pin)

    def add_course(self, c_list):

        # This function adds a student ID to a course roster
        # It takes a list of Course objects as an argument
        # Asks the student to enter a course to add
        # It then iterates through the provided list to check if the course is valid
        # If the course is in the list it will call the add_student method from the Course class with
        # the student's ID.
        # It has no return value

        student_choice = input('Enter course to add: ')

        for course in c_list:
            if student_choice == course.get_course_code():
                Course.add_student(course, self.get_id())
                break
        else:
            print('This course is not available')

    def drop_course(self, c_list):

        # This function removes a student ID from a course roster
        # It takes a list of Course objects as an argument
        # Asks the student to enter a course to drop
        # It then iterates through the provided list to check if the course is valid
        # If the course is in the list it will call the drop_student method from the Course class with
        # the student's ID.
        # It has no return value

        student_choice = input('Enter course to drop: ')

        for course in c_list:
            if student_choice == course.get_course_code():
                Course.drop_student(course, self._id)
                break
        else:
            print('You are not registered in this course')

    def list_courses(self, c_list):

        # This function lists the courses the student is currently registered in
        # It takes a list of Course objects as an argument
        # Iterates through courses in the provided list and calls the student_in_course method
        # to check whether they are registered.
        # If they are it displays the course.
        # After displaying all registered courses it displays the total number of registered courses
        # It has no return value

        print("You are currently registered in: ")
        course_count = 0
        for course in c_list:
            if course.student_in_course(Student.get_id(self)):
                print(course.get_course_code())
                course_count += 1
        print(course_count, 'total courses.')
