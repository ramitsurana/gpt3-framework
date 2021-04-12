from flask import Flask
from flask import Flask, render_template, request
import configparser
import openai

app = Flask(__name__)

env = 'DEV'
config = configparser.ConfigParser()
config.read('config.ini')

print(config)
print(config['DEV']['API_KEY'])
openai.api_key = print(config['DEV']['API_KEY'])

@app.route("/")
def home():
    return render_template("main.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    response = openai.Completion.create(
        engine=config[env]['ENGINE'],
        prompt=userText,
        temperature=int(config[env]['TEMPERATURE']),
        max_tokens=int(config[env]['MAX_TOKENS']),
        top_p=int(config[env]['TOP_P']),
        frequency_penalty=int(config[env]['FREQUENCY_PENALTY']),
        presence_penalty=int(config[env]['PRESENCE_PENALTY']),
        stop=["\n"]
    )
    return str(response)


if __name__ == "__main__":
    app.run()
