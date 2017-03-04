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
        """Initialize student attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):
    """Creates questions and answers"""

    def __init__(self, question, correct_answer):
        """Initialize question attributes."""

        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        """ ."""

        print self.question
        self.user_answer = raw_input("> ")

        return self.correct_answer.lower() == self.user_answer.lower()


class Exam(object):
    """Creates the exam with a list of questions"""

    def __init__(self, name):
        """Initialize exam attributes."""

        self.name = name
        self.questions = []

    def add_question(self, question, correct_answer):
        """Adds question and answer instances to the list of questions"""

        self.question = Question(question, correct_answer)
        self.questions.append(self.question)

    def administer(self):
        """administer the exam and return a score displayed as a percent"""

        self.score = 0

        for question in self.questions:
            if question.ask_and_evaluate() is True:
                self.score += 1.0

        self.score_percent = self.score / len(self.questions) * 100
        return self.score_percent





