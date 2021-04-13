from flask import Flask
from flask import Flask, render_template, request
import configparser
import openai

app = Flask(__name__)

config_file_path= "C:\\Users\\ramit\\Projects\\Personal\\gpt3-framework\\config.cfg"

config = configparser.ConfigParser()
config.read(config_file_path)

openai.api_key = config.get('GLOBAL', 'API_KEY')

@app.route("/chatbot/")
def home():
    return render_template("chatbot.html")

@app.route("/chatbot/get")
def get_bot_response():
    application_type = 'CHATBOT'
    userText = request.args.get('msg')
    response = openai.Completion.create(
        engine=config[application_type]['ENGINE'],
        prompt=str(userText),
        temperature=float(config[application_type]['TEMPERATURE']),
        max_tokens=int(config[application_type]['MAX_TOKENS']),
        top_p=float(config[application_type]['TOP_P']),
        frequency_penalty=float(config[application_type]['FREQUENCY_PENALTY']),
        presence_penalty=float(config[application_type]['PRESENCE_PENALTY']),
        stop=["\n"]
    )
    return str(response['choices'][0]['text'])


if __name__ == "__main__":
    app.run()
