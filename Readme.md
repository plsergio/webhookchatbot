Fonte: https://www.pragnakalp.com/dialogflow-fulfillment-webhook-tutorial/

### Instalação
- python3 -m venv env
- source env/bin/activate
- pip install -r requirements.txt

### Run
- python app.py

### Run the webhook using Ngrok (https://dashboard.ngrok.com/get-started)

Ngrok is a web tunnelling tool that provides a way to test APIs and webhooks from local server. There are two versions available. I am using the free version with registration on ngrok.io.

To run ngrok, use the following command: ngrok http <port_number>
e.g. ngrok http 5000 (for flask app)

- ./ngrok authtoken 1SGR8XJ7fzgZDruZkt4qlX0uggU_7RQGG398NAFKumR1HwWmt
- ./ngrok http 5000 
- http://08511fba.ngrok.io/webhook