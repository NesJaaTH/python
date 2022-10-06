from ast import While
from re import T
import time
import paho.mqtt.client as mqtt
import random
import json

print("----------------------------------------")
NETPIE_HOST = "broker.netpie.io"

# Client ID ของ Device ที่สร้างขึ้นใน NETPIE
CLIENT_ID = "4d046c4d-37c7-4978-953a-c851d596fad5"

# Token ของ Device ที่สร้างขึ้นใน NETPIE
DEVICE_TOKEN = "M7ptbnbqoBZWgLzm72Jcb4gfJ2N6ahGd"
sensor_data = {'dataswitch':''}
sensor_data_loop = {'loopstatus':''}

def on_connect(client, userdata, flags, rc):
    print("Result from connect: {}:".format(mqtt.connack_string(rc)))
    client.subscribe("@msg/switch")

def on_message(client, userdata, msg):
    data_ = msg.payload
    data = data_.decode("utf-8")
    print(data)
    if (data == "ontoggle") :
        print("on")
        sensor_data["dataswitch"] = "ontoggle"
        client.publish("@shadow/data/update",json.dumps({"data": sensor_data}), 1)
    if (data == "offtoggle") :
        print("off")
        sensor_data["dataswitch"] = "offtoggle"
        client.publish("@shadow/data/update",json.dumps({"data": sensor_data}), 1)
    if (data == "BlinkLED2"):
        print("tes")
    elif data == "TEST0":
        sensor_data["dataswitch"] = "TEST0"
        client.publish("@shadow/data/update",json.dumps({"data": sensor_data}), 1)
    elif data == "Reset":
        sensor_data["dataswitch"] = "Reset"
        client.publish("@shadow/data/update",json.dumps({"data": sensor_data}), 1)
    elif data == "TEST1":
        sensor_data["dataswitch"] = "TEST1"
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
                #sensor_data["dataswitch"] = "testz"  
                #client.publish("@shadow/data/update",json.dumps({"data": sensor_data}), 1)
                print("test")
                time.sleep(5)
                if sensor_data["dataswitch"] == "Reset":
                    print("time1")
                    time.sleep(2)
                elif sensor_data["dataswitch"] == "TEST0":
                    print("time2")
                    time.sleep(2)
                elif sensor_data["dataswitch"] == "TEST1":
                    sensor_data["dataswitch"] = "testz"  
                    

except KeyboardInterrupt:
    pass