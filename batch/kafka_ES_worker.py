from kafka import KafkaConsumer
import json

while True:
    for message in consumer:
        new_listing = json.loads((message.value).decode('utf-8'))
        # push to ES
