#Run the code to create the files etc.
class Course:
    def __init__(self, course_code, title, maximum_capacity):
        self.course_code = course_code
        self.title = title
        self.maximum_capacity = maximum_capacity
        self.current_number_of_students = 0

    def enroll_student(self):
        if self.current_number_of_students < self.maximum_capacity:
            self.current_number_of_students += 1
            return True
        else:
            return False

    def get_current_number_of_students(self):
        return self.current_number_of_students

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses_enrolled = []

    def enroll_in_course(self, course):
        if course.enroll_student():
            self.courses_enrolled.append(course)
            return True
        else:
            return False

    def get_courses_enrolled(self):
        return self.courses_enrolled

def main():
    try:
        with open("courses.txt", "x") as f:
            f.write("course_code,title,maximum_capacity\n")
            f.write("CS629,Introduction to Computer Science,100\n")
            f.write("CS628,Data Structures,80\n")
            f.write("CS627,Algorithms,40\n")
    except FileExistsError:
        pass

    try:
        with open("students.txt", "x") as f:
            f.write("student_id,name\n")
            f.write("12345,Justin Hadinata\n")
            f.write("67890,Alexander\n")
            f.write("98765,Xaverius William\n")
    except FileExistsError:
        pass

    with open("courses.txt", "r") as f:
        next(f)
        courses = [Course(line.split(",")[0], line.split(",")[1], int(line.split(",")[2].strip())) for line in f]

    with open("students.txt", "r") as f:
        next(f)
        students = [Student(int(line.split(",")[0]), line.split(",")[1]) for line in f]

    print("Courses:")
    for course in courses:
        print(f"{course.course_code} - {course.title} - {course.maximum_capacity} - Students Enrolled: {course.current_number_of_students}")

    print("\nStudents:")
    for student in students:
        print(f"{student.student_id} - {student.name} - Courses Enrolled: {[course.course_code for course in student.courses_enrolled]}")

    while True:
        student_id = int(input("Enter your student ID: "))
        student = next((student for student in students if student.student_id == student_id), None)

        if not student:
            print("Student not found.")
            continue

        course_code = input("Hello "+student.name+", "+"Enter the course code you want to enroll in: ")
        course = next((course for course in courses if course.course_code == course_code), None)

        if not course:
            print("Course not found.")
            continue

        if student.enroll_in_course(course):
            print("You have successfully enrolled in the course.")
        else:
            print("You cannot enroll in this course because it is full.")

        with open("courses.txt", "a") as f:
            f.write(f"{course.course_code},{course.title},{course.maximum_capacity}\n")

        with open("students.txt", "a") as f:
            f.write(f"{student.student_id},{student.name},{','.join([course.course_code for course in student.courses_enrolled])}\n")

if __name__ == "__main__":
    main()
