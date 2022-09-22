import paho.mqtt.client as mqtt

NETPIE_HOST = "broker.netpie.io"
# Client ID ของ Device ที่สร้างขึ้นใน NETPIE
CLIENT_ID = "6b17009a-a604-4659-a5fe-2bf2e142072d"

# Token ของ Device ที่สร้างขึ้นใน NETPIE
DEVICE_TOKEN = "pjPW3JvZj8LT96RHcnN1cPU8yE5KM2Eb"

def on_connect(client, userdata, flags, rc):
    print("Result from connect: {}:".format(mqtt.connack_string(rc)))
    client.subscribe("@msg/farm")

def on_message(client, userdata, msg):
    data_ = (msg.payload)
    datarecv = (data_).decode("utf-8").split(",")
    temp = datarecv[0]
    humi = datarecv[1]
    print("Data Recive : ", datarecv)
    print("Temperature", temp)
    print("Humidity", humi)

client = mqtt.Client(protocol=mqtt.MQTTv311,
                     client_id=CLIENT_ID, clean_session=True)
client.username_pw_set(DEVICE_TOKEN)
client.on_connect = on_connect
client.on_message = on_message
client.connect(NETPIE_HOST, 1883)
client.loop_start()
while True:
    client.loop_start()

