import time
import paho.mqtt.client as mqtt
import random
import json

NETPIE_HOST = "broker.netpie.io"
# Client ID ของ Device ที่สร้างขึ้นใน NETPIE
CLIENT_ID = "6b17009a-a604-4659-a5fe-2bf2e142072d"

# Token ของ Device ที่สร้างขึ้นใน NETPIE
DEVICE_TOKEN = "pjPW3JvZj8LT96RHcnN1cPU8yE5KM2Eb"

def on_connect(client, userdata, flags, rc):
    print("Result from connect: {}:".format(mqtt.connack_string(rc)))
    client.subscribe("@shadow/data/updated")

def on_message(client, userdata, msg):
    data1 = str(msg.payload).split(",")
    data2 = (data1[2]).split(":")
    data3 = (data2[1]).split("}")
    Humi = data3[0]
    print("Humidity is    : ", Humi)
    data4 = (data1[1]).split(":")
    Temp = data4[2]
    print("Temperature is : ", Temp)

client = mqtt.Client(protocol=mqtt.MQTTv311,
                     client_id=CLIENT_ID, clean_session=True)
client.username_pw_set(DEVICE_TOKEN)
client.on_connect = on_connect
client.on_message = on_message
client.connect(NETPIE_HOST, 1883)
client.loop_start()

while True:
    client.loop_start()
