from kafka import KafkaConsumer, KafkaProducer
import json
import time

consumer = KafkaConsumer(
    "iot-data",
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# Giả lập gửi lệnh tới thiết bị
def send_ac_command(state):
    print(f"[LỆNH] Điều hòa: {state}")
    # Ở thực tế, bạn có thể gửi qua MQTT hoặc HTTP đến thiết bị thật
    with open("ac_state.txt", "w") as f:
        f.write(state)

for msg in consumer:
    data = msg.value
    print("Nhận:", data)

    if data["temperature"] > 32:
        print("[!] CẢNH BÁO: Nhiệt độ cao:", data["temperature"])
        send_ac_command("OFF")
    else:
        send_ac_command("ON")
