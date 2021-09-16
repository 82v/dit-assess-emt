# Skateboarding quiz
# Luke

"""
Quiz on skateboarding
"""
#imports
from appJar import gui #imports appjar and gui
import random
import sys

# variables
question_db = []
quiz_progress = 0
user_answers = []

# functions

def press(button):
    print(button)
    
    global quiz_progress
    
    if button == "Start Quiz":
        app.hideFrame("welcome")
        app.showFrame("questions")
        update_question()
        app.hideFrame("summary")

    elif question_db[quiz_progress].check_correct(button):
        app.setLabel("correct","Correct") #adds a label telling you that u got the queston right
        app.showLabel("correct")
        app.showButton("Next") #switches to next questions
        app.setLabelFg("correct","yellow")   #sets button colour too yellow     
        user_answers.append("Question %d: %s"%(quiz_progress+1, app.getButton(button)+" - Correct !"))

    
    elif button == "Exit": #exit button
        app.stop() #closes gui
        
    elif button == "Next":
        
        print("quiz_progress = %d len question_db= %d)"%(quiz_progress,len(question_db)))
        if quiz_progress +1 < len(question_db):
            quiz_progress +=1
            app.hideLabel("correct")
            app.hideButton("Next")
            update_question()
        else:
            app.hideButton("Next")
            app.hideButton("a")
            app.hideButton("b")
            app.hideButton("c")
            app.hideButton("d")
            app.addButton("the end",press)

                
    elif button == "the end":
        app.hideButton("the end") #hides the button
        app.hideFrame("questions")
        app.showFrame("summary")
        summary_string = ""
        for answer in user_answers:
            summary_string += answer+"\n"
        app.setLabel("summary_display",summary_string)
        print(user_answers)    
        
        pass   
    
    else:
        app.setLabel("correct","Incorrect") #adds a label telling you that u got the queston wrong"""
        app.showLabel("correct")
        #print("Question %d: %s"%(quiz_progress, app.getButton(button)))
        user_answers.append("Question %d: %s"%(quiz_progress+1, app.getButton(button)))


# class definitions
class Question:
    # initilise class
    def __init__(self, question, answers, correct_answer):
        self.question = question
        self.answers = answers
        self.correct_answer = correct_answer
    
    # returns array of all possible answers
    def get_answer_array(self):
        _answer_array = self.answers
        _answer_array.append(self.correct_answer)
        return _answer_array
    # returns the answer text
    def get_question_text(self):
        return self.question
    def check_correct(self, selected_answer):
        #print(app.getButtonText(selected_answer))
        print(self.correct_answer,selected_answer)
        if selected_answer == self.correct_answer:
            return True
        else:
            return False

 
def update_question():
    global quiz_progress
    app.setLabel("question_label",question_db[quiz_progress].get_question_text())
    app.setButton("a",question_db[quiz_progress].get_answer_array()[0])
    app.setButton("b",question_db[quiz_progress].get_answer_array()[1])
    app.setButton("c",question_db[quiz_progress].get_answer_array()[2])
    app.setButton("d",question_db[quiz_progress].get_answer_array()[3])

# questions for quiz
question_db.append(Question("Who was skater of the year 2019",["Ishod Wair","Tyshawn Jones","Miltons","Kyle Walker"],"d")) #list of first question
question_db.append(Question("What is a real skateboard brand?",["Baker","North Mountain","Burton","Public"],"a")) #list of second question
question_db.append(Question("Who invented the skateboard?",["No one knows","Kader","Tony Hawk","Rodney Mullen"],"a")) #list of third question
question_db.append(Question("Which Olympics first featured skateboarding?",["UK 2013","USA 2003 ","Tokyo 2020","1994 Mexico"],"c")) #list of fourth question


# create a GUI variable called app
app = gui("Skate Quiz", "800x400") #gui name and dimensions of window
app.setBg("Grey") #gui colour
app.setFont(18)

# add & configure widgets - widgets get a name, to help referencing them later
with app.frame("welcome"):
    app.addLabel("title", "Welcome to my quiz on skateboarding") #header
    app.setLabelBg("title", "black")
    app.setLabelFg("title", "silver")
    app.addButton("Start Quiz",press) #button to start quiz
    app.addButton("Exit",press) #button which closes quiz 
    
    
with app.frame("questions"):
    app.addLabel("question_label","")
    app.setLabel("question_label",question_db[quiz_progress].get_question_text())
    app.addButtons(["a","b","c","d"],press)   
    app.addLabel("correct","")
    app.hideLabel("correct")
    app.addButton("Next",press)
    app.hideButton("Next")

with app.frame("summary"):
    app.addLabel("Summary")
    app.setLabelFg("Summary","yellow") #makes summary label yellow
    app.addLabel("summary_display")
    #summary_labels = "user_answers"
    #for answer in summary_label:
       # user_results += answer +"\n"
       # app.setLabel("summary_label",)     

app.hideFrame("questions")
app.hideFrame("summary")




#while loop
#while quiz_progress ==0:
    #quiz = GUI()

# start the GUI
app.go()
