## Deployment Steps

### Pre requisites

* Python3 and above
* OpenAI Account

### Local Deployment of Application

1. Git Clone the repo on your computer.
2. Run ```pip install -r requirements.txt```
3. Generate your own API Key by logging into and going to <https://beta.openai.com/account/api-keys>.
4. Update the API Keys in config.cfg file under API_KEY Keyword.
5. Run the main.py file using the following command - ```python main.py```
6. Check on <http://localhost:5000/chatbot> to see the output.

### Deploying Docs Locally

1. Git Clone the repo on your computer.
2. Run ```pip install -r requirements.txt```
3. Run the following command at root folder level - ```mkdocs serve```.
4. Check on <http://localhost:8000> to see the output.