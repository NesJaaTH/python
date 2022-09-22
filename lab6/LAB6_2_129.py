import sys
import time
import paho.mqtt.client as mqtt
import json
import random

NETPIE_HOST = "broker.netpie.io"
CLIENT_ID = "4d046c4d-37c7-4978-953a-c851d596fad5"  # Client ID ของ Device ที่สร้างขึ้นใน NETPIE
DEVICE_TOKEN = "M7ptbnbqoBZWgLzm72Jcb4gfJ2N6ahGd"# Token ของ Device ที่สร้างขึ้นใน NETPIE
sensor_data = {'temperature': 0, 'humidity': 0}

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


try:
    while True:
        temperature = random.randint(0, 50)
        humidity = random.randint(0, 100)
        sunshine = random.randint(0, 100)
        if humidity is not None and temperature is not None and sunshine is not None:
            humidity = round(humidity)
            temperature = round(temperature)
            sunshine = round(sunshine)
            print(
                "Temp={0: 0.1f}*C Humidity={1: 0.1f} % sunshine={0: 0.1f}*C".format(temperature, humidity, sunshine))
            sensor_data["temperature"] = temperature
            sensor_data["humidity"] = humidity
            sensor_data["sunshine"] = sunshine
            print(json.dumps({"data": sensor_data}))
            client.publish("@shadow/data/update",
                           json.dumps({"data": sensor_data}), 1)
            time.sleep(10)
        else:
            print("Failed to get reading. Try again!")
except KeyboardInterrupt:
    pass
    client.loop_start()

    client.disconnect()
