import time
import paho.mqtt.client as mqtt
import random
import json
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

print("----------------------------------------")
NETPIE_HOST = "broker.netpie.io"

# Client ID ของ Device ที่สร้างขึ้นใน NETPIE
CLIENT_ID = "4d046c4d-37c7-4978-953a-c851d596fad5"

# Token ของ Device ที่สร้างขึ้นใน NETPIE
DEVICE_TOKEN = "M7ptbnbqoBZWgLzm72Jcb4gfJ2N6ahGd"
sensor_data = {'dataswitchsw':'','dataswitch':''}

def on_connect(client, userdata, flags, rc):
    print("Result from connect: {}:".format(mqtt.connack_string(rc)))
    client.subscribe("@msg/switch")

def on_message(client, userdata, msg):
    data_ = msg.payload
    data = data_.decode("utf-8")
    if (data == "ontoggle_one"):
        GPIO.output(17, GPIO.HIGH)
        GPIO.output(27, GPIO.HIGH)
        sensor_data["dataswitchsw"] = "ontoggle_one"
        sensor_data["dataswitch"] = "ontoggle"
        client.publish("@shadow/data/update",json.dumps({"data": sensor_data}), 1)
    if (data == "offtoggle"):
        GPIO.output(17, GPIO.LOW)
        GPIO.output(27, GPIO.LOW)
        sensor_data["dataswitchsw"] = "offtoggle"
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
                sensor_data["dataswitch"] = datasend
                client.publish("@shadow/data/update",json.dumps({"data": sensor_data}), 1)
        elif(sensor_data["dataswitchsw"] == "ontoggle_one"):
                print("LED ON")
                sensor_data["dataswitchsw"] = "ontoggle_one"
                sensor_data["dataswitch"] = "ontoggle"
                client.publish("@shadow/data/update",json.dumps({"data": sensor_data}), 1)
        elif(GPIO.input(22) == False):
                print("Waiting for you to press a button")
                GPIO.output(17, GPIO.LOW)
                GPIO.output(27, GPIO.LOW)
                datasend = "offtoggle"
                sensor_data["dataswitch"] = datasend
                client.publish("@shadow/data/update",json.dumps({"data": sensor_data}), 1)
                time.sleep(0.1)
        time.sleep(3)

except KeyboardInterrupt:
    pass

