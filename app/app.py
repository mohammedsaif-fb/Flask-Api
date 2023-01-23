from flask_cors import CORS
from flask_cors import CORS
from flask import Flask, jsonify
from results import get_queries


app = Flask(__name__)
CORS(app)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False


@app.errorhandler(404)
def error_404(e):
    return '<h1>No source like your request.</h1>', 404


@app.route('/stackdata')
def sayname():

    return jsonify(get_queries())

    # Here you can pass any parameters you want.
    # It will not affect the application work.

    # Here you can pass any parameters you want.
    # It will not affect the application work.
