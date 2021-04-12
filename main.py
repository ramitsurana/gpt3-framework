from flask import Flask
from flask import Flask, render_template, request
import configparser
import openai

app = Flask(__name__)

env = 'DEV'
config_file_path= "C:\\Users\\ramit\\Projects\\Personal\\gpt3-framework\\config.cfg"

config = configparser.ConfigParser()
config.read(config_file_path)

openai.api_key = config.get(env, 'API_KEY')

@app.route("/chatbot/")
def home():
    return render_template("main.html")

@app.route("/chatbot/get")
def get_bot_response():
    userText = request.args.get('msg')
    response = openai.Completion.create(
        engine=config[env]['ENGINE'],
        prompt=str(userText),
        temperature=float(config[env]['TEMPERATURE']),
        max_tokens=int(config[env]['MAX_TOKENS']),
        top_p=float(config[env]['TOP_P']),
        frequency_penalty=float(config[env]['FREQUENCY_PENALTY']),
        presence_penalty=float(config[env]['PRESENCE_PENALTY']),
        stop=["\n"]
    )
    return str(response['choices'][0]['text'])


if __name__ == "__main__":
    app.run()
