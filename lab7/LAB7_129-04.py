import time
import paho.mqtt.client as mqtt
import random
import json
import logging

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

print("----------------------------------------")
NETPIE_HOST = "broker.netpie.io"

CLIENT_ID = "4d046c4d-37c7-4978-953a-c851d596fad5"
DEVICE_TOKEN = "M7ptbnbqoBZWgLzm72Jcb4gfJ2N6ahGd"
sensor_data = {'dataswitch':''}


def on_connect(client, userdata, flags, rc):
    print("Result from connect: {}:".format(mqtt.connack_string(rc)))
    client.subscribe("@msg/switch")
def on_message(client, userdata, msg):
    data = msg.payload.decode("utf-8")
    if(data == "BlinkLED1"):
        sensor_data["dataswitch"] = "BlinkLED1"
        client.publish("@shadow/data/update",json.dumps({"data": sensor_data}), 1)
    elif(data == "BlinkLED2"):
        sensor_data["dataswitch"] = "BlinkLED2"
        client.publish("@shadow/data/update",json.dumps({"data": sensor_data}), 1)
    elif(data == "BlinkLED3"):
        sensor_data["dataswitch"] = "BlinkLED3"
        client.publish("@shadow/data/update",json.dumps({"data": sensor_data}), 1)
    elif(data == "FlashingLED"):
        sensor_data["dataswitch"] = "FlashingLED"
        client.publish("@shadow/data/update",json.dumps({"data": sensor_data}), 1)
    elif(data == "Reset"):
        sensor_data["dataswitch"] = "Reset"
        client.publish("@shadow/data/update",json.dumps({"data": sensor_data}), 1)


client = mqtt.Client(protocol=mqtt.MQTTv311,
                     client_id=CLIENT_ID, clean_session=True)
client.username_pw_set(DEVICE_TOKEN)
client.on_connect = on_connect
client.on_message = on_message
client.connect(NETPIE_HOST, 1883)
client.loop_start()

try:
    while True:
            if sensor_data["dataswitch"] == "BlinkLED1":
                GPIO.output(17, GPIO.HIGH)
                time.sleep(1)
                GPIO.output(17, GPIO.LOW)
                time.sleep(1)
            elif sensor_data["dataswitch"] == "BlinkLED2":
                GPIO.output(27, GPIO.HIGH)
                time.sleep(1)
                GPIO.output(27, GPIO.LOW)
                time.sleep(1)
            elif sensor_data["dataswitch"] == "BlinkLED3":
                GPIO.output(17, GPIO.HIGH)
                GPIO.output(27, GPIO.HIGH)
                time.sleep(1)
                GPIO.output(17, GPIO.LOW)
                GPIO.output(27, GPIO.LOW)
                time.sleep(1)
            elif sensor_data["dataswitch"] == "FlashingLED":
                GPIO.output(17, GPIO.HIGH)
                time.sleep(1)
                GPIO.output(17, GPIO.LOW)
                time.sleep(1)
                GPIO.output(27, GPIO.HIGH)
                time.sleep(1)
                GPIO.output(27, GPIO.LOW)
                time.sleep(1)
            elif sensor_data["dataswitch"] == "Reset":
                GPIO.output(27, GPIO.LOW)
                GPIO.output(17, GPIO.LOW)
                sensor_data["dataswitch"] = "Stop Led"
                client.publish("@shadow/data/update",json.dumps({"data": sensor_data}), 1)

except KeyboardInterrupt:
    pass

