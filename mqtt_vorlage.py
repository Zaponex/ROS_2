import paho.mqtt.client as mqtt
import json

# ThingsBoard MQTT-Broker-Einstellungen (Anpassen)
broker_address = "51.144.148.72"
broker_port = 1883
access_token = "hm12Dp0Hob9Lzw8yX9e2"
mqtt_topic = "v1/devices/roboter/telemetry"

# GPS-Daten aus dem Modul
latitude = 52.5200  # Beispiel-Latitude-Wert
longitude = 12.4050  # Beispiel-Longitude-Wert

# Erstelle ein JSON-Payload mit den GPS-Daten
payload = {
    "latitude": latitude,
    "longitude": longitude,
}

# MQTT Callback-Funktion, die aufgerufen wird, wenn die Verbindung hergestellt ist
def on_connect(client, userdata, flags, rc):
    print("Verbunden mit ThingsBoard MQTT-Broker")
    client.publish(mqtt_topic, json.dumps(payload))

# MQTT Client erstellen
client = mqtt.Client()
client.on_connect = on_connect

# Mit dem MQTT-Broker verbinden
client.username_pw_set(access_token, password=None)
client.connect(broker_address, broker_port, 60)

# Schleife für die MQTT-Kommunikation aufrechterhalten
client.loop_forever()


