import time
import json
import random
from kafka import KafkaProducer

# Khởi tạo Kafka Producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Gửi dữ liệu định kỳ
while True:
    data = {
        "device_id": "iot_device_01",
        "temperature": round(random.uniform(25.0, 35.0), 2),
        "humidity": round(random.uniform(40.0, 60.0), 2),
        "timestamp": time.time()
    }

    print(f"Gửi: {data}")
    producer.send("iot-data", value=data)
    time.sleep(5)  # gửi mỗi 5 giây
