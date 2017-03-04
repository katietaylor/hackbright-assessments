"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

2. What is a class?

3. What is an instance attribute?

4. What is a method?

5. What is an instance in object orientation?

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.


"""


class Student(object):
    """Creates a new student and assigns a name and address."""

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):
    """Creates questions and answers"""

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer


class Exam(object):
    """Creates the exam with a list of questions"""

    def __init__(self, name):
        self.name = name
        self.questions = []
