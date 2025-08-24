# Day 1 Task Question:
# Create a Student Management System (Simple Version)
# Requirements:
# Create a class Student with attributes: name, marks.
# Add a method display() to show student details.
# Use a getter and setter for marks (to prevent negative marks).
# Create a child class GraduateStudent that adds research_topic.
# Override the display() method in the child class to also show the research topic.

# Parent class
class Student:
    def __init__(self, name, marks):
        self.name = name
        self._marks = 0  # Internal variable for marks
        self.marks = marks  # Calls the setter

    # Getter for marks
    @property
    def marks(self):
        return self._marks

    # Setter for marks (prevents negative marks)
    @marks.setter
    def marks(self, value):
        if value < 0:
            print("Marks cannot be negative. Setting to 0.")
            self._marks = 0
        else:
            self._marks = value

    # Method to display student details
    def display(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")


# Child class
class GraduateStudent(Student):
    def __init__(self, name, marks, research_topic):
        super().__init__(name, marks)
        self.research_topic = research_topic

    # Override display method
    def display(self):
        super().display()
        print(f"Research Topic: {self.research_topic}")


# Testing the classes
student1 = Student("Alice", 85)
student1.display()
print()

grad_student1 = GraduateStudent("Bob", 90, "Artificial Intelligence")
grad_student1.display()
print()

# Trying negative marks
student2 = Student("Charlie", -10)
student2.display()
