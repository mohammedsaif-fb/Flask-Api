from flask_cors import CORS
from flask import Flask, jsonify, request

app = Flask(__name__)

CORS(app)


@app.route('/', methods=['GET'])
def fish():
    app.logger.info('health check requested')
    return jsonify({
        "client": "hastec",
        "healthcheck": "active",
        "latency": "20ms"
    })


@app.route('/stacks', methods=['GET'])
def stack():

    data = [
        {
            "stack_id": 100010000000000,
            "latitude": 53.30175,
            "longitude": -1.13653,
            "location": "Worksop England United Kingdom",
            "status": "red"
        },
        {
            "stack_id": 100310000000000,
            "latitude": 51.671036,
            "longitude": -0.30088,
            "location": "Radlett England United Kingdom",
            "status": "green"
        },
        {
            "stack_id": 100310000000000,
            "latitude": 51.85384,
            "longitude": -0.374142,
            "location": "Luton England United Kingdom",
            "status": "red"
        },
        {
            "stack_id": 100310000000000,
            "latitude": 51.592701,
            "longitude": -0.237055,
            "location": "Hendon London England United Kingdom",
            "status": "green"
        },
        {
            "stack_id": 100310000000000,
            "latitude": 51.613602,
            "longitude": -0.249545,
            "location": "Mill Hill London England�",
            "status": "red"
        },
        {
            "stack_id": 100310000000000,
            "latitude": 52.133572,
            "longitude": -0.475675,
            "location": "Bedford",
            "status": "green"
        },
        {
            "stack_id": 100310000000000,
            "latitude": 53.402557,
            "longitude": -2.93572,
            "location": "Picton Rd, Liverpool ",
            "status": "red"
        },
        {
            "stack_id": 140310000000000,
            "latitude": 53.216908,
            "longitude": -1.426562,
            "location": "Chesterfield S40 2WL",
            "status": "green"
        },
        {
            "stack_id": 7,
            "latitude": 53.216888,
            "longitude": -1.426285,
            "location": "Chesterfield",
            "status": "red"
        },
        {
            "stack_id": 8,
            "latitude": 51.67107,
            "longitude": -0.30095,
            "location": "London",
            "status": "green"
        },
        {
            "stack_id": 8,
            "latitude": 55.67107,
            "longitude": -0.30095,
            "location": "London",
            "status": "red"
        }
    ]

    return jsonify(data)


@ app.route('/stack/<id>/', methods=['GET'])
def stackmonitor(id):

    data = [{"stack_id": 7,
            "location": "Chesterfield",
             "latitude": 53.216888,
             "longitude": -1.426285},

            {"stack_id": 8,
            "location": "London",
             "latitude": 51.67107,
             "longitude": -0.30095},
            ]
    return jsonify(data)


@ app.route('/stackmonitor', methods=['GET'])
def stackplot():
    data = [{"red_limit": 100,
            "amber_limit": 200,
             "timestamps": [23, 32, 231, 3, 12, 3, 3, 21],
             "stack_height":[23, 32, 231, 3, 12, 3, 3, 21]}]
    return jsonify(data)


@ app.route('/stackadd/', methods=['POST'])
def stackaddition():
    email = request.json['email']

    return jsonify({"message": email+"2"})


@ app.route('/archive/stack/<id>/', methods=['GET', 'POST'])
def archived(id):

    data = [{"timestamp": 1661280790,
            "stack_height": 1000,
             "ambient_temperature": 23.5,
             "stack_height_forecast": 1000,
             "stack_temperature_forecast": 28
             }
            ]
    return jsonify(data)


@ app.errorhandler(404)
def resource_not_found(e):
    return jsonify({
        "message": "The resource doesn't exist, Please check Again"
    })


if __name__ == '__main__':
    app.run()

    # Here you can pass any parameters you want.
    # It will not affect the application work.
