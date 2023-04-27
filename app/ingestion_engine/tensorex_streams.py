import paho.mqtt.client as mqtt
import json
import mysql.connector
import uuid


MYSQL_HOST = "db-mysql-lon1-10668-do-user-8714569-0.b.db.ondigitalocean.com"
MYSQL_USER = "doadmin"
MYSQL_PASSWORD = "AVNS_yYlaUe6YWhbGhvki97L"
MYSQL_DATABASE = "optimised_store"
# Connect to the MySQL server
ca_cert_path = "/home/backend-services/Flask-Api/app/ca-certificate.crt"
BROKER_ADDRESS = "dev.fishbonesolutions.co.uk"


mqtt_client = mqtt.Client()
mqtt_client.connect(BROKER_ADDRESS, 1883)

# MQTT broker address


def on_message(client, userdata, msg):
    connection2 = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE,
        port=25060,
        ssl_ca=ca_cert_path,)

    cursor = connection2.cursor()
    topic = msg.topic
    m_decode = str(msg.payload.decode("utf-8"))
    datapoint_index = str(uuid.uuid1())[:8]
    if topic == 'tensorx_frag2':
        payload = json.loads((m_decode))
        timestamp = payload[0]['TS']
        stack_id = payload[0]['ID']
        if len(payload[0]['VR']) == 2:
            latitude = payload[0]['VR'][0]
            longitude = payload[0]['VR'][1]
            insert_query = "INSERT INTO tensorex_locations (timestamp, latitude,longitude,stack_id,datapoint_index) VALUES (%s, %s, %s,%s, %s)"
            values = [(payload[0]['TS'], latitude,
                       longitude, stack_id, datapoint_index)]
            cursor.executemany(insert_query, values)
            connection2.commit()

        if len(payload[0]['VR']) == 1 and payload[0]['VR'] != [0]:
            battery_voltage = payload[0]['VR']
            if battery_voltage[0] > 20000:
                battery_voltage = battery_voltage[0]/1000
            insert_query = "INSERT INTO tensorex_battery(timestamp,battery_voltage,stack_id,datapoint_index) VALUES (%s, %s, %s,%s)"
            values = [(payload[0]['TS'], battery_voltage,
                       stack_id, datapoint_index)]
            cursor.executemany(insert_query, values)
            connection2.commit()
    if topic == 'tensorx_frag1':
        payload = json.loads(m_decode)
        stack_id = payload[0]['ID']
        if len(payload[0]['VR']) == 8:
            stack_raw = payload[0]['VR'][1]*0.022
            temperature = payload[0]['VR'][6]/400
            timestamp = payload[0]['TS']
        insert_query = "INSERT INTO tensorex_stack_heights(timestamp,stack_height,ambient_temp,stack_id,datapoint_index) VALUES (%s, %s, %s, %s,%s)"
        values = [(payload[0]['TS'], stack_raw,
                   temperature,
                   stack_id, datapoint_index)]
        cursor.executemany(insert_query, values)
        connection2.commit()
    cursor.close()
    connection2.close()


mqtt_client.on_message = on_message
mqtt_client.subscribe('#')
mqtt_client.loop_forever()
