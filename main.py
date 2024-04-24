from flask import Flask, render_template, request
import threading
import time
from scrapeHS import getHSInfo
app = Flask(__name__)

allPlayers = []
students = []
teachers = []

@app.route('/')
def showAllHS():
    global allPlayers
    hindex = request.args.get('h_index')
    hs = []
    if hindex:
        hs = sorted(allPlayers, key=lambda x: x['h_index'], reverse=True)
    else:
        hs = sorted(allPlayers, key=lambda x: x['citations'], reverse=True)
    return render_template('highscores.html', highscores=hs)

@app.route('/student')
def showStudentHS():
    global students
    hindex = request.args.get('h_index')
    hs = []
    if hindex:
        hs = sorted(students, key=lambda x: x['h_index'], reverse=True)
    else:
        hs = sorted(students, key=lambda x: x['citations'], reverse=True)
    return render_template('highscores.html', highscores=hs)

@app.route('/teacher')
def showTeacherHS():
    global teachers
    hindex = request.args.get('h_index')
    hs = []
    if hindex:
        hs = sorted(teachers, key=lambda x: x['h_index'], reverse=True)
    else:
        hs = sorted(teachers, key=lambda x: x['citations'], reverse=True)
    return render_template('highscores.html', highscores=hs)

def dailyUpdate():
    global allPlayers, students, teachers
    while True:
        print("Running daily task on...")
        allPlayers = getHSInfo("all")
        teachers = getHSInfo("teachers")
        students = getHSInfo("students")
        time.sleep(86400)  # Sleep for 24 hours

task_thread = threading.Thread(target=dailyUpdate)
if __name__ == '__main__':
    task_thread.start()
    app.run(host="0.0.0.0", debug=True)
