import time
import paho.mqtt.client as mqtt
import random
import json
import logging


print("----------------------------------------")
NETPIE_HOST = "mqtt.netpie.io"

# Client ID ของ Device ที่สร้างขึ้นใน NETPIE
CLIENT_ID = "4d046c4d-37c7-4978-953a-c851d596fad5"  # Client ID ของ Device ที่สร้างขึ้นใน NETPIE
DEVICE_TOKEN = "M7ptbnbqoBZWgLzm72Jcb4gfJ2N6ahGd"# Token ของ Device ที่สร้างขึ้นใน NETPIE

def on_connect(client, userdata, flags, rc):
    print("Result from connect: {}:".format(mqtt.connack_string(rc)))
    client.subscribe("@msg/led")

def on_message(client, userdata, msg):
    data = msg.payload.decode("utf-8")
    print(data)
    if(data == "ontoggle"):
        while True:
            print("LED ON")
            time.sleep(0.5)
            coutled += 1 
            print(coutled)

    elif(data == "offtoggle"):
        print("LED OFF")

client = mqtt.Client(protocol=mqtt.MQTTv311,
                     client_id=CLIENT_ID, clean_session=True)
client.username_pw_set(DEVICE_TOKEN)
client.on_connect = on_connect
client.on_message = on_message
client.connect(NETPIE_HOST, 1883)
client.loop_start()

try:
    while True:
        time.sleep(5)

except KeyboardInterrupt:
    pass

