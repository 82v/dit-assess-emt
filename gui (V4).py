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
    if button == "Kyle Walker":
        print("Correct!")

    if button == "Ishod Wair" or button == "Tyshawn Jones" or button == "Miltons":
        print("no!")
    
    if button == "Exit":
        app.stop()
    if button == "Exit1":
        app.stop()        
            
        


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
question_db.append(Question("Who was skater of the year 2019",["Kyle Walker","Ishod Wair","Tyshawn Jones","Miltons"],"Exit1"))
question_db.append(Question("Enter question 2",["1","2","3","4"],"Exit2"))
question_db.append(Question("Enter question 3",["1","2","3","4"],"Exit3"))


# create a GUI variable called app
app = gui("Skate Quiz", "800x400")
app.setBg("magenta")
app.setFont(18)

# add & configure widgets - widgets get a name, to help referencing them later
with app.frame("welcome"):
    app.addLabel("title", "Welcome to my quiz on skateboarding")
    app.setLabelBg("title", "black")
    app.setLabelFg("title", "silver")
    app.addButton("Start Quiz",press)
    app.addButton("Exit",press)
    
    
with app.frame("questions"):
    app.addLabel("question_label","")
    app.setLabel("question_label",question_db[quiz_progress].get_question_text())
    app.addButtons(question_db[quiz_progress].get_answer_array(),press)
    
app.hideFrame("questions")

# start the GUI
app.go()