import paho.mqtt.client as mqtt
from kafka import KafkaProducer

# Kafka producer để gửi message vào Kafka
producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

# Callback khi kết nối MQTT thành công
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("test/topic")  # Subscribe vào topic

# Callback khi nhận message từ MQTT
def on_message(client, userdata, msg):
    print(f"Message received: {msg.payload.decode()}")
    # Gửi message vào Kafka
    producer.send('mqtt-topic', value=msg.payload)

# Khởi tạo MQTT client
client = mqtt.Client()

# Đăng ký các callback
client.on_connect = on_connect
client.on_message = on_message

# Kết nối đến HiveMQ (hoặc broker MQTT khác)
client.connect("localhost", 1883, 60)

# Bắt đầu loop để client nhận và xử lý message
client.loop_forever()
