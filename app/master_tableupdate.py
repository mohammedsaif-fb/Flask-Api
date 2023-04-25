import json
import mysql.connector
# Set the path to the CA certificate file

MYSQL_HOST = "db-mysql-lon1-10668-do-user-8714569-0.b.db.ondigitalocean.com"
MYSQL_USER = "doadmin"
MYSQL_PASSWORD = "AVNS_yYlaUe6YWhbGhvki97L"
MYSQL_DATABASE = "broker_dump"
MYSQL_DATABASE_LEGACY = "hastec_powerbi"

ca_cert_path = 'ca-certificate.crt'
# Connect to the MySQL server


def get_broker_logs(id, latitude, longitude):
    connection2 = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE_LEGACY,
        port=25060,
        ssl_ca=ca_cert_path,

    )

# Do something with the connection
# ...
    mycursor = connection2.cursor()

    # Define the SQL query to update the columns
    sql = "UPDATE masterstack_register SET latitude = %s, longitude = %s WHERE id = %s"

    val = (latitude, longitude, id)

    # Execute the SQL query
    mycursor.execute(sql, val)

    # Commit the changes to the database
    connection2.commit()


for i in range(2):
    get_broker_logs(4, 53.216909, -1.626153)
    get_broker_logs(3, 53.216909, -1.826153)
    get_broker_logs(2, 53.216909,  -1.426153)
    get_broker_logs(1, 53.216909, -2.1631298480437997)
