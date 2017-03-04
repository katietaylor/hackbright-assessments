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

# Parts 2 and 3


class Student(object):
    """Creates a new student and assigns a name and address."""

    def __init__(self, first_name, last_name, address):
        """Initialize student attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):
    """Creates questions and answers."""

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
    """Creates an exam with a list of questions."""

    def __init__(self, name):
        """Initialize exam attributes."""

        self.name = name
        self.questions = []

    def add_question(self, question, correct_answer):
        """Adds question and answer instances to the list of questions."""

        new_question = Question(question, correct_answer)
        self.questions.append(new_question)

    def administer(self):
        """administer the exam and return a score displayed as a percent."""

        self.score = 0

        for question in self.questions:
            if question.ask_and_evaluate() is True:
                self.score += 1.0

        try:
            self.score_percent = self.score / len(self.questions) * 100
        except ZeroDivisionError:
            self.score_percent = None
            print "{} can't be administered without questions.".format(self.name)

        return self.score_percent

###############################################################################
# Part 5


class Quiz(Exam):
    "Creates a quiz with a list of questions."

    def administer(self):
        super(Quiz, self).administer()
        return self.score_percent >= 50

###############################################################################
# Part 4


def take_test(exam, student):
    """Administer the exam to a student and prints the score."""

    exam.administer()
    print "Your score is {}%".format(exam.score_percent)


def example():
    """Creates and exam, adds questions, and creates a student that takes the
    exam.
    """

    exam = Exam("midterm")

    # exam.add_question("Who is the best captain?", "Jean-Luc Picard")
    # exam.add_question("First step when there is something wrong with the ship",
                      # "Run a level 2 diagnostic")

    exam.add_question("1 + 1", "2")
    exam.add_question("1 + 2", "3")
    exam.add_question("1 + 3", "4")
    exam.add_question("1 + 4", "5")

    student = Student("Will", "Riker", "1701-D Enterprise")

    take_test(exam, student)
