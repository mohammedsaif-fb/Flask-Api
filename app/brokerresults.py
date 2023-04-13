import json
import mysql.connector
# Set the path to the CA certificate file

MYSQL_HOST = "db-mysql-lon1-10668-do-user-8714569-0.b.db.ondigitalocean.com"
MYSQL_USER = "doadmin"
MYSQL_PASSWORD = "AVNS_yYlaUe6YWhbGhvki97L"
MYSQL_DATABASE = "broker_dump"
MYSQL_DATABASE_LEGACY = "hastec_stacks"

ca_cert_path = 'ca-certificate.crt'
# Connect to the MySQL server


def get_broker_logs():
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

    query = ("SELECT timestamp as timestamp, topic as topic, message as message, id as id from broker_messages")

    cursor2.execute(query)

    row = cursor2.fetchone()

    timestamps = []
    topic = []
    message = []
    id = []

    while row is not None:
        timestamps.append(row[0])
        topic.append(row[1])
        message.append(row[2])
        id.append(row[3])
        row = cursor2.fetchone()

    result_json = {"timestamps": timestamps,
                   "topic": topic, "id": id, "message": message}

    cursor2.close()
    connection2.close()
    return result_json
