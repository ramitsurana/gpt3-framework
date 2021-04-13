  
from flask import render_template
from main import app

@app.route('/')
@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

@app.route('/translator')
def translator():
    return render_template('translator.html')