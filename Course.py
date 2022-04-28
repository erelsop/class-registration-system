
class Course:

    # Course class with 3 private instance variables for: course codes, max sizes, and rosters
    # Provides a variety of functions for altering and displaying course information

    def __init__(self, c_code, m_size):

        # Constructor that takes a course code and max course size as arguments
        # course_code is initialized with the c_code argument, max_size with the m_size argument
        # The roster is initialized as empty to be populated later

        self.__course_code = c_code
        self.__max_size = m_size
        self.__roster = []

    def add_student(self, id):

        # This function takes a student's ID and checks whether they are in the current course
        # If they are, it checks to see if the course is at max capacity
        # If the course is not full it adds the student's ID to the course roster
        # It has no return value

        if id not in self.__roster:
            if len(self.__roster) < self.__max_size:
                self.__roster.append(id)
                print('Course registered,', self.__course_code)
            else:
                print("Course is already full.")
        else:
            print('Already registered for course,', self.__course_code)

    def drop_student(self, id):

        # This function takes a student's ID and checks whether they are in the current course
        # If they are, it removes their ID from the course roster
        # It has no return value

        if id in self.__roster:
            self.__roster.remove(id)
            print("Successfully dropped from course:", self.__course_code)
        else:
            print("You are not registered in course:", self.__course_code)

    def display_roster(self):

        # This function iterates through the course roster and displays each student ID registered for the course
        # It has no return value

        self.__roster.sort()
        print("Number of students registered in course", self.__course_code, "is:", len(self.__roster))
        for student in self.__roster:
            print(student, "registered")

    def change_max_size(self):

        # This function displays the current enrollment count and the max size of the current course
        # It then asks the user to input a new max course size
        # If the course size is greater than or equal to the current enrollment count
        # It will change the max size of the course to the new value
        # It has no return value

        print("Current enrollment count for course:", self.__course_code, ':', len(self.__roster))
        print("Max size for course", self.__course_code + ':', self.__max_size)

        while True:
            try:
                new_max_size = int(input('Please enter the new max size: '))
                if new_max_size >= len(self.__roster):
                    self.__max_size = new_max_size
                    break
                else:
                    print('Max size cannot be lower than current class size.')
            except ValueError:
                print('Invalid input type for max class size.')

    def get_course_code(self):

        # This function returns the current course code

        return self.__course_code

    def student_in_course(self, id):

        # This function checks if a student's ID is in the current roster
        # If it is, it returns true
        # Otherwise it returns false

        if id in self.__roster:
            return True
        else:
            return False
