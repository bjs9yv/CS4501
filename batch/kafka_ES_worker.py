from kafka import KafkaConsumer
import json
import time
from elasticsearch import Elasticsearch
 
# Wait for 15 seconds to make sure Kafka is up and running
time.sleep(15)
while True:
    consumer = KafkaConsumer('new-listings-topic', group_id='listing-indexer', bootstrap_servers=['kafka:9092'])
    es = Elasticsearch(['es'])
    for message in consumer:
        # take a message from the queue
        new_listing = json.loads((message.value).decode('utf-8'))
        # push to ES
        es.index(index='listing_index', doc_type='listing', id=json.loads(new_listing)['id'], body=new_listing)
        es.indices.refresh(index="listing_index")
