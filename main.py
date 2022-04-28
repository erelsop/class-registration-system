from Course import Course
from Student import Student
from Admin import Admin

# Main module for the class registration system


def login(u_list):

    # This function provides a login prompt to the users
    # It takes a user list as an argument
    # Asks the user to enter their ID, and then their PIN
    # It iterates through the provided user list to verify entries
    # If the provided information matches an iteration,
    # it returns the index of that user within the list
    # Otherwise it return -1

    id = input('Enter ID: ')
    pin = input('Enter PIN: ')

    for user in u_list:
        if user.get_id() == id:
            if user.get_pin() == pin:
                print('ID and PIN verified')
                return u_list.index(user)
    else:
        print('Invalid ID or PIN')
        return -1


def student_session(c_list, s_list):

    # This function lays out the functionality of a student session
    # It takes a list of Course objects and a list of students as arguments
    # Calls the login function with the student list before allowing course alterations
    # Asks whether the student wants to add, drop, view their courses, or exit
    # Calls the relevant method according to the student's choice
    # It will loop until student manually exits
    # It has no return value

    student = login(s_list)

    if student != -1:

        while True:

            while True:
                try:
                    student_choice = int(input('Enter 1 to add course, 2 to drop course, 3 to see registered courses, 0 to exit: '))
                    if student_choice in range(4):
                        break
                except ValueError:
                    print('Invalid input')

            if student_choice == 1:
                Student.add_course(s_list[student], c_list)

            if student_choice == 2:
                Student.drop_course(s_list[student], c_list)

            if student_choice == 3:
                Student.list_courses(s_list[student], c_list)

            if student_choice == 0:
                break


def admin_session(c_list, a_list):

    # This function lays out the functionality of an admin session
    # It takes a list of Course objects and a list of admins as arguments
    # Calls the login function with the admin list before allowing course alterations
    # Asks whether the admin wants to view a course roster, change max size for a course, or exit
    # Calls the relevant method according to the admin's choice
    # It will loop until admin manually exits
    # It has no return value

    admin = login(a_list)

    if admin != -1:

        while True:

            while True:
                try:
                    admin_choice = int(input('Enter 1 to show class roster, 2 to change max class size, 0 to exit: '))
                    if admin_choice in range(3):
                        break
                except ValueError:
                    print('Invalid input')

            if admin_choice == 1:
                Admin.show_roster(a_list[admin], c_list)

            if admin_choice == 2:
                Admin.change_max_size(a_list[admin], c_list)

            if admin_choice == 0:
                break


def init_lists(c_list, s_list, a_list):

    # ------------------------------------------------------------
    # This function adds elements to course_list, student_list and
    # admin_list.  It makes testing and grading easier.  It has
    # three paramters: c_list is the list of Course objects;
    # s_list is the list of Student objects; a_list is the list of
    # Admin objects.  This function has no return value.
    # -------------------------------------------------------------

    course1 = Course("CSC121", 2)
    course1.add_student("1004")
    course1.add_student("1003")
    c_list.append(course1)
    course2 = Course("CSC122", 2)
    course2.add_student("1001")
    c_list.append(course2)
    course3 = Course("CSC221", 1)
    course3.add_student("1002")
    c_list.append(course3)

    student1 = Student("1001", "111")
    s_list.append(student1)
    student2 = Student("1002", "222")
    s_list.append(student2)
    student3 = Student("1003", "333")
    s_list.append(student3)
    student4 = Student("1004", "444")
    s_list.append(student4)

    admin1 = Admin("7001", "777")
    a_list.append(admin1)
    admin2 = Admin("8001", "888")
    a_list.append(admin2)


def main():

    # The main function has 3 lists for: courses, student IDs, and admin IDs
    # The lists are populated with the init_lists function
    # Asks where the user wants to begin a student session, admin session, or exit the program
    # It has no return value

    course_list = []
    student_list = []
    admin_list = []

    init_lists(course_list, student_list, admin_list)

    while True:

        try:
            user_choice = int(input('Enter 1 if you are a student, 2 if you are administrator, 0 to quit: '))
        except ValueError:
            print('Invalid input')

        if user_choice == 1:
            student_session(course_list, student_list)

        if user_choice == 2:
            admin_session(course_list, admin_list)

        if user_choice == 0:
            break


main()
