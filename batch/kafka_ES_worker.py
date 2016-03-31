from kafka import KafkaConsumer
import json
import time
 
# Wait for 5 seconds
time.sleep(5)
while True:
    consumer = KafkaConsumer('new-listings-topic', group_id='listing-indexer', bootstrap_servers=['kafka:9092'])
    for message in consumer:
        new_listing = json.loads((message.value).decode('utf-8'))
        # push to ES
