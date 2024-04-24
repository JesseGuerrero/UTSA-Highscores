from flask import Flask, render_template
import threading
import time
from scrapeHS import getHSInfo
app = Flask(__name__)

allPlayers = []
students = []
teachers = []

@app.route('/')
def showAllHS():
    return render_template('highscores.html', highscores=allPlayers)

@app.route('/student')
def showStudentHS():
    return render_template('highscores.html', highscores=students

@app.route('/teacher')
def showTeacherHS():
    return render_template('highscores.html', highscores=teachers)

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
    app.run(debug=True)
