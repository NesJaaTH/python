import time
import paho.mqtt.client as mqtt
import random
import json
import logging
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

print("----------------------------------------")
NETPIE_HOST = "mqtt.netpie.io"

# Client ID ของ Device ที่สร้างขึ้นใน NETPIE
CLIENT_ID = "4d046c4d-37c7-4978-953a-c851d596fad5"

# Token ของ Device ที่สร้างขึ้นใน NETPIE
DEVICE_TOKEN = "M7ptbnbqoBZWgLzm72Jcb4gfJ2N6ahGd"
sensor_data = {'dataswitch':''}
sensor_data = {'dataswitchsw':''}

def on_connect(client, userdata, flags, rc):
    print("Result from connect: {}:".format(mqtt.connack_string(rc)))
    client.subscribe("@msg/switch")

def on_message(client, userdata, msg):
    data_ = msg.payload
    data = data_.decode("utf-8")
    if (data == "ontoggle") :
        GPIO.output(17, GPIO.HIGH)
        GPIO.output(27, GPIO.HIGH)
        sensor_data["dataswitch"] = "ontoggle"
        client.publish("@shadow/data/update",json.dumps({"data": sensor_data}), 1)
    if (data == "offtoggle") :
        GPIO.output(17, GPIO.LOW)
        GPIO.output(27, GPIO.LOW)
        sensor_data["dataswitch"] = "offtoggle"
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
        if(GPIO.input(22) == True):
                print("Button Pressed")
                print(GPIO.input(22))
                GPIO.output(17, GPIO.HIGH)
                GPIO.output(27, GPIO.HIGH)
                datasend = "ontoggle"
                sensor_data["dataswitchsw"] = datasend
                client.publish("@shadow/data/update",json.dumps({"data": sensor_data}), 1)
        else:
                print("Waiting for you to press a button")
                GPIO.output(17, GPIO.LOW)
                GPIO.output(27, GPIO.LOW)
                datasend = "offtoggle"
                sensor_data["dataswitchsw"] = datasend
                client.publish("@shadow/data/update",json.dumps({"data": sensor_data}), 1)
                time.sleep(0.1)
        time.sleep(3)

except KeyboardInterrupt:
    pass
