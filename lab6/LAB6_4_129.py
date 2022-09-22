import time
import paho.mqtt.client as mqtt
import random

NETPIE_HOST = "broker.netpie.io"

# Client ID ของ Device ที่สร้างขึ้นใน NETPIE
CLIENT_ID = "4d046c4d-37c7-4978-953a-c851d596fad5"

# Token ของ Device ที่สร้างขึ้นใน NETPIE
DEVICE_TOKEN = "M7ptbnbqoBZWgLzm72Jcb4gfJ2N6ahGd"

def on_connect(client, userdata, flags, rc):
    print("Result from connect: {}:".format(mqtt.connack_string(rc)))
    client.subscribe("@msg/farm")

def on_message(client, userdata, msg):
    data_ = msg.payload
    print(data_.decode("utf-8"))

client = mqtt.Client(protocol=mqtt.MQTTv311,
                     client_id=CLIENT_ID, clean_session=True)
client.username_pw_set(DEVICE_TOKEN)
client.on_connect = on_connect
client.on_message = on_message
client.connect(NETPIE_HOST, 1883)
client.loop_start()

try:
    while True:
        temperature = random.randrange(0, 50)
        humidity = random.randrange(20, 100)
        datasend = str(temperature) + "," + str(humidity)
        client.publish("@msg/farm", datasend, 1)
        time.sleep(5)

except KeyboardInterrupt:
    pass
