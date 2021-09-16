# Skateboarding quiz
# Luke

"""
Quiz on skateboarding
"""
#imports
from appJar import gui
import random

# variables
question_db = []
quiz_progress = 0

# functions

def press(button):
    if button == "Start Quiz":
        app.hideFrame("welcome")
        app.showFrame("questions")
    if button == "4":
        print("Correct!")

    if button == "3" or button == "2" or button == "1":
        print("no!")

# class definitions
class Question:
    # initilise class
    def __init__(self, question, answers, correct_answer):
        self.question = question
        self.answers = answers
        self.correct_answer = correct_answer
        
        
    # returns True if correct answer is selected
    def check_correct(self, selected_answer):
        _correct = True
        return _correct
    # returns array of all possible answers
    def get_answer_array(self):
        _answer_array = self.answers
        _answer_array.append(self.correct_answer)
        return _answer_array
    # returns the answer text
    def get_question_text(self):
        return self.question

# create three question instances    
question_db.append(Question("Enter question",["1","2","3"],"4"))
question_db.append(Question("Enter question 2",["1","2","3"],"4"))
question_db.append(Question("Enter question 3",["1","2","3"],"4"))


# create a GUI variable called app
app = gui("Skate Quiz", "500x300")
app.setBg("magenta")
app.setFont(18)

# add & configure widgets - widgets get a name, to help referencing them later
with app.frame("welcome"):
    app.addLabel("title", "Welcome to my quiz on skateboarding")
    app.setLabelBg("title", "black")
    app.setLabelFg("title", "silver")
    app.addButton("Start Quiz",press)
    
with app.frame("questions"):
    app.addLabel("question_label","")
    app.setLabel("question_label",question_db[quiz_progress].get_question_text())
    app.addButtons(question_db[quiz_progress].get_answer_array(),press)
    
app.hideFrame("questions")

# start the GUI
app.go()