import paho.mqtt.client as mqtt
import time
import random
import json

# Callback khi kết nối thành công
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # Sau khi kết nối thành công, client sẽ gửi dữ liệu lên topic 'test/topic'
    client.subscribe("test/topic")  # Đăng ký nhận dữ liệu từ topic này

# Callback khi nhận message từ broker (nếu có)
def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()}")

# Khởi tạo MQTT client
client = mqtt.Client()

# Đăng ký các callback
client.on_connect = on_connect
client.on_message = on_message

# Kết nối tới MQTT broker (thí dụ: HiveMQ đang chạy trên localhost)
client.connect("localhost", 1883, 60)

# Bắt đầu quá trình gửi dữ liệu (Publish)
client.loop_start()

while True:
    # Tạo dữ liệu giả để gửi
    data = {
        "device_id": "device_1",
        "temperature": round(random.uniform(20.0, 30.0), 2),  # Nhiệt độ ngẫu nhiên
        "humidity": round(random.uniform(40.0, 60.0), 2),  # Độ ẩm ngẫu nhiên
        "timestamp": time.time()  # Thời gian gửi
    }
    print(f"Sending: {data}")
    
    # Gửi dữ liệu lên topic 'test/topic'
    client.publish("test/topic", json.dumps(data))  # Gửi dữ liệu dạng JSON
    
    time.sleep(5)  # Gửi dữ liệu mỗi 5 giây
