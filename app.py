# import flask dependencies
from flask import Flask, request, make_response, jsonify

# initialize the flask app
app = Flask(__name__)

# default route
@app.route('/')
def index():
    return 'Api Webhook ChatBot Ouvidoria!'

# function for responses
def results():
    # build a request object
    req = request.get_json(force=True)

    # fetch action from json
    action = req.get('queryResult').get('action')
    unidade = req.get('queryResult').get('parameters').get('unidade')

    if action == 'enderecos':
	    return {'fulfillmentText': 'Busca pelo endereço. '  + str(unidade)}

    # return a fulfillment response
    return {'fulfillmentText': 'Resposta Genérica da API.' + str(action)}

# create a route for webhook
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    # return response
    return make_response(jsonify(results()))

# run the app
if __name__ == '__main__':
   app.run()