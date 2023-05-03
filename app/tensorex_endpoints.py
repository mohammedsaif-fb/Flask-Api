import mysql.connector
# Set the path to the CA certificate file

MYSQL_HOST = "db-mysql-lon1-10668-do-user-8714569-0.b.db.ondigitalocean.com"
MYSQL_USER = "doadmin"
MYSQL_PASSWORD = "AVNS_yYlaUe6YWhbGhvki97L"
MYSQL_DATABASE = "tensorex_demo"
ca_cert_path = 'ca-certificate.crt'
# Connect to the MySQL server


def get_optimised():
    connection2 = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database="optimised_store",
        port=25060,
        ssl_ca=ca_cert_path,)

    cursor2 = connection2.cursor()

    query = ("SELECT tsh.timestamp as timestamp, stack_height as stack_height , ambient_temp as temp, battery_voltage as battery_voltage FROM tensorex_stack_heights tsh INNER JOIN tensorex_locations tl ON tsh.stack_id = tl.stack_id INNER JOIN tensorex_battery tb  ON tsh.stack_id = tb.stack_id WHERE tsh .stack_id = 987654321")
    cursor2.execute(query)

    row = cursor2.fetchone()

    timestamps = []
    stack_heights = []
    temperatures = []
    battery_voltages = []

    while row is not None:
        timestamps.append(row[0]*1000)
        stack_heights.append(row[1])
        temperatures.append(row[2])
        battery_voltages.append(row[3])
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
            {
                "name": "Battery Voltage",
                "data": battery_voltages,
        }

        ]
    }
# Close the cursor and connection
    cursor2.close()
    connection2.close()

    return result_json


def get_stack_height():
    connection2 = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database='optimised_store',
        port=25060,
        ssl_ca=ca_cert_path,)

# Do something with the connection
# ...
    cursor2 = connection2.cursor()

    query = ("SELECT timestamp as timestamp, stack_height as stack_height, ambient_temp as temps from stack_height sh  WHERE timestamp > 1683126463  order by timestamp desc")
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
        database='optimised_store',
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
