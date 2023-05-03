import mysql.connector
# Set the path to the CA certificate file

MYSQL_HOST = "db-mysql-lon1-10668-do-user-8714569-0.b.db.ondigitalocean.com"
MYSQL_USER = "doadmin"
MYSQL_PASSWORD = "AVNS_yYlaUe6YWhbGhvki97L"
MYSQL_DATABASE = "tensorex_demo"
ca_cert_path = 'ca-certificate.crt'
# Connect to the MySQL server


def get_stack_height():
    connection2 = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database='tensorex_demo',
        port=25060,
        ssl_ca=ca_cert_path,)

# Do something with the connection
# ...
    cursor2 = connection2.cursor()

    query = ("SELECT FROM_UNIXTIME(timestamp) AS timestamp, stack_height, ambient_temp"
             "FROM stack_height"
             "WHERE timestamp >= UNIX_TIMESTAMP(NOW() - INTERVAL 5 MINUTE)")

    cursor2.execute(query)

    row = cursor2.fetchone()

    timestamps = []
    stack_heights = []
    temperatures = []

    while row is not None:
        timestamps.append(row[0]*1000)
        stack_heights.append(row[1])
        temperatures.append(row[2])
        row = cursor2.fetchone()

    result_json = {
        "timestamps": timestamps,
        "dataseries": [{
            "name": "Stack Heights",
            "data": stack_heights,
        },
            {
            "name": "Ambient Temperature",
            "data": temperatures,
        },

        ]
    }
# Close the cursor and connection
    cursor2.close()
    connection2.close()

    return result_json


def get_battery_data():
    connection2 = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database='tensorex_demo',
        port=25060,
        ssl_ca=ca_cert_path,

    )

# Do something with the connection
# ...
    cursor2 = connection2.cursor()

    query = (
        "SELECT timestamp as timestamp, battery_voltage as battery_Voltage from tensorex_battery ORDER BY timestamp DESC")
    cursor2.execute(query)

    row = cursor2.fetchone()

    timestamps = []

    battery_voltages = []

    while row is not None:
        timestamps.append(row[0]*1000)
        battery_voltages.append(row[1])
        row = cursor2.fetchone()

    result_json = {
        "timestamps": timestamps,
        "dataseries": [
            {
                "name": "Battery Voltage",
                "data": battery_voltages,
            },


        ]
    }
# Close the cursor and connection
    cursor2.close()
    connection2.close()

    return result_json
