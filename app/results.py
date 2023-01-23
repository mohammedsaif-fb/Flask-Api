import json
import mysql.connector
# Set the path to the CA certificate file

MYSQL_HOST = "db-mysql-lon1-10668-do-user-8714569-0.b.db.ondigitalocean.com"
MYSQL_USER = "doadmin"
MYSQL_PASSWORD = "AVNS_yYlaUe6YWhbGhvki97L"
MYSQL_DATABASE = "hastec_stacks"
ca_cert_path = '/usr/src/app/ca-certificate.crt'
# Connect to the MySQL server


def get_queries():
    connection2 = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE,
        port=25060,
        ssl_ca=ca_cert_path,

    )

# Do something with the connection
# ...
    cursor2 = connection2.cursor()

    query = ("SELECT tms as timestamp, ZAI1 as stack_height, AI1 as battery_Voltage, AI2 as Ambient_Temperature from stacks ORDER BY tms DESC")

    cursor2.execute(query)

    row = cursor2.fetchone()

    timestamps = []
    stack_heights = []
    temperatures = []
    battery_voltages = []

    while row is not None:
        timestamps.append(row[0]*1000)
        stack_heights.append(row[1])
        temperatures.append(row[3])
        battery_voltages.append(row[2])
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
        },


        ]
    }
# Close the cursor and connection
    cursor2.close()
    connection2.close()

    return result_json
