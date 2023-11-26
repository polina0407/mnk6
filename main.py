from PyQt5.QtWidgets import QApplication

app = QApplication([])

from m2 import*
from m3 import*
from random import choice, shuffle
from time import sleep
class Question:
    def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.isAsking = True
q1 = Question('45-120=', '-75', '75', '45', '6')
q2 = Question('1500:50=', '30', '45', '23', '-30')
q3 = Question('40+137=', '177', '233', '456', '-45')
q4 = Question('4*3=', '12', '23', '3', '4')
q5 = Question('233-33=', '200', '122', '647', '32432222222222222')
q6 = Question('4+2=', '6', '7', '8', '9')
q7 = Question('1+1=', '2', '4', '88', '65')
q8 = Question('34-4=', '30', '34', '556', '78')
q9 = Question('5643767*0=', '0', '84738', '747', '8678')
q10 = Question('5676:0=', 'на 0 ділити не можна', '5676', '56', '67')
radio_buttons = [rb_ans1, rb_ans2, rb_ans3, rb_ans4]
questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]

def new_question():
    global cur_q
    cur_q = choice(questions)
    lb_question. setText (cur_q.question)
    lb_right_answer.setText (cur_q.answer)
    shuffle(radio_buttons)
    radio_buttons[1].setText(cur_q.wrong_answer2)
    radio_buttons[2].setText(cur_q.wrong_answer3)
    radio_buttons[3].setText(cur_q.answer)
new_question()

def check():
    RadioGroup.setExclusive(False)
    for answer in radio_buttons:
        if answer.isChecked():
            if answer. text() == lb_right_answer.text():
                lb_result.setText('Правильно!')
                answer. setChecked (False)
                break
    else:
        lb_result.setText('Неправильно!')
    RadioGroup.setExclusive(True)

def click_ok():
    if btn_next.text() == 'Відповісти':
        check()
        gb_question.hide()
        gb_answer.show()

        btn_next.setText('Наступне запитання')
    else:
        new_question()
        gb_question.show()
        gb_answer.hide()

    btn_next.setText('видповісти')
btn_next.clicked.connect(click_ok)

def rest():
    window.hide()
    n = sp_rest.value() * 60
    sleep (n)
    window.show()
btn_rezt.clicked.connect (rest)
def menu_generation():
    menu_win. show()
    window.hide()

btn_menu. clicked. connect (menu_generation)

btn_menu. clicked. connect (menu_generation)

def back_menu():
    menu_win.hide()
    window. show()

btn_back. clicked. connect (back_menu)
def clear():
    le_question.clear()
    le_right_ans.clear()
    le_wrong_ans1.clear()
    le_wrong_ans2.clear()
    Le_wrong_ans3.clear()
btn_clear.clicked.connect(clear)

def add_question():
    new_q = Question(le_question.text(), le_right_ans.text(), le_wrong_ans1.text(), le_wrong_ans2.text(), Le_wrong_ans3.text())

    questions.append(new_q)
    clear()
btn_add_question.clicked.connect(add_question)

window.show()
app.exec_()

