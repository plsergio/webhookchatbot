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
- https://08511fba.ngrok.io/webhook


### Urls
- https://www.pragnakalp.com/dialogflow-tutorial-create-fulfillment-webhook-using-python-django/
- https://github.com/pragnakalp/dialogflow-response-library-implementation-python-django/blob/master/views.py
- https://github.com/pragnakalp/dialogflow-webhook-response-libary-in-python
- https://github.com/googleapis/dialogflow-python-client-v2
- https://www.mockable.io/a/#/space/demo8949242/rest/QqtjKcAAA?inwizzard=true
- https://cloud.google.com/docs/authentication/production
- https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/dialogflow/cloud-client
- https://cloud.google.com/dialogflow/docs/quick/api#detect-intent-text-python
- https://cloud.google.com/dialogflow/docs/tutorials/build-an-agent/create-fulfillment-using-webhook
