"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   Encapsulation: Related pieces are kept together in the same box. It keeps the
   data close to the functionality.

   Abstraction: Allows another developer to use the benefits of the code without
   needing to see how it is actually written. What the code is doing is more
   important than how it is doing it.

   Polymorphism: Allows components to be used interchangeably. So, instead of
   using conditional statements, you can pull in different components as needed.
   It also helps keep your code "DRY". You can reuse pieces of code without
   having to rewrite it.

2. What is a class?

   A class is a type of thing in code that can have attributes and define
   methods. It is a way to store data in a structured way.

3. What is an instance attribute?

   An instance attribute is an attribute (piece of data) that is specific to
   the instance of the class.

4. What is a method?

   A method is code that is like a function, but it is defined on a class. A
   method will always take a least one argument, "self."

5. What is an instance in object orientation?

   An instance is an occurrance of a class, also known as an object.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   A class attribute is the same for all instances of a class. It is a piece of
   data that is specific to the class. However, once the instance is created,
   you can change the attribute, which will make it an instance attribute.

   You should use a class attribute for data that will be the same for all
   instances of a class, at least when it is first initalized.

   For example, the class Burrito could have a class attribute, has_tortilla
   set to True. Another class BurritoBowl which inherits from Burrito would
   set the has_tortilla class attribute to False. An instance attribute could
   be type_of_meat or has_guacamole.

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
        """Ask question and compares user's answer to the correct answer."""

        print self.question
        self.user_answer = raw_input("> ")

        # Checks is answer is correct and returns True of False
        return self.correct_answer.lower() == self.user_answer.lower()


class Exam(object):
    """Creates an exam with a list of questions."""

    def __init__(self, name):
        """Initialize exam attributes."""

        self.name = name
        self.questions = []

    def add_question(self, question, correct_answer):
        """Instantiates a Question instance and adds it to the list of
        questions.
        """

        new_question = Question(question, correct_answer)
        self.questions.append(new_question)

    def administer(self):
        """Administer the exam and return a score displayed as a percent."""

        self.score = 0

        # Ask each question in the list
        for question in self.questions:
            # Add 1 to the score if answered correctly
            if question.ask_and_evaluate() is True:
                self.score += 1.0

        try:
            # Calculate the percent of answers that were correct
            self.score_percent = self.score / len(self.questions) * 100

        # Handles error when trying to administer exam before adding questions.
        except ZeroDivisionError:
            self.score_percent = None
            print "{} can't be administered without questions.".format(
                self.name)

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
    """Creates an exam, adds questions, and creates a student that takes the
    exam.
    """

    # Instantiates an Exam instance.
    exam = Exam("ST TNG")

    # Adds 3 exam questions.
    exam.add_question("Who is the best captain?", "Jean-Luc Picard")
    exam.add_question("What is Data's cat's name?", "Spot")
    exam.add_question("What species is Q?", "Q")

    # Instantiates a Student instance.
    student = Student("Will", "Riker", "1701-D Enterprise")

    take_test(exam, student)
