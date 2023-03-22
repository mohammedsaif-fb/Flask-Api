from flask_cors import CORS
from flask import Flask, jsonify, request
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from app.results import get_queries, get_stack_id
from app.stacks import save_stack_data
from app.emails_alerts import send_alerts
from app.configs import email_list

app = Flask(__name__)
CORS(app)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
app.config["JWT_ALGORITHM"] = "HS256"

jwt = JWTManager(app)

app.config["JWT_ALGORITHM"] = "HS256"
app.config["SECRET_KEY"] = "IUGYGFYR456547E47636RDNGTXSDR"


@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username != "test" or password != "test":
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)


@app.errorhandler(404)
def error_404(e):
    return '<h1>Bad Request</h1>', 404


@app.route("/stacks")
def stack_info():
    un_allocated_stacks = [
        862771040055488, 862771040055481, 862771040055482, 862771040055484]

    allocated_stacks = [862771040055488, 862771040055481]

    response_stack = {
        "un_allocated_stacks": un_allocated_stacks,
        "allocated_stacks": allocated_stacks,
    }
    return jsonify(response_stack)


@app.route('/stackdatalegacy/')
def stackdata():
    return jsonify(get_queries())

    # Here you can pass any parameters you want.
    # It will not affect the application work.

    # Here you can pass any parameters you want.
    # It will not affect the application work.


@app.route('/stackdata/<stack_id>')
def stackdata_id(stack_id):
    return jsonify(get_stack_id(stack_id))


@app.route('/kpi')
def home_kpi():
    kpi_json = {
        "id": 1,
        "sensor_dashboard": {
            "low_voltage": 0,
            "connectivity_problems": 0
        },
        "alerts_summary": {
            "red": 0,
            "amber": 0,
            "green": 1,
            "attention_requried": 0
        },
        "prediction_dashboard": {
            "temperature_prediction": "UP",
            "critical": 0,
            "amber": 0
        }
    }
    return jsonify(kpi_json)


@app.route('/stack_addition', methods=['POST'])
def handle_addtion():
    data = request.json
    request_id = save_stack_data(data)
    send_alerts(reciepents=email_list, message_content=data)
    response = {
        "req_id": request_id
    }
    return jsonify(response)
