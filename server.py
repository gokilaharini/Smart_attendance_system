from flask import Flask, render_template, jsonify, redirect, url_for
import os
from werkzeug.serving import run_simple
import tkinter as tk
import subprocess
import sys

app = Flask(__name__, template_folder='.')

# Route for the main login page (formerly main.html)

@app.route('/')
def index():
    return render_template('main.html')  # Render main.html as the entry point

@app.route('/employeedashboard.html')
def employeedashboard():
    return render_template('employeedashboard.html')
# Route for employee dashboard
@app.route('/leaveform.html')
def leaveform():
    return render_template('leaveform.html')

@app.route('/hrdashboard.html')
def hrdashboard():
    return render_template('hrdashboard.html')

@app.route('/hrleave.html')
def hrleave():
    return render_template('hrleave.html')

@app.route('/calender.html')
def calender():
    return render_template('calender.html')

# Face recognition activation endpoint
@app.route('/activate-face-recognition', methods=['POST'])
def activate_face_recognition():
    try:
        subprocess.Popen([sys.executable, 'main.py'])
        return jsonify({"status": "success", "message": "Face recognition system activated"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    # Run the Flask app
    run_simple('localhost', 5000, app, use_reloader=False)