from kafka import KafkaProducer
import time
import csv
import logging

def Producer(
    bootstrap_server: str = 'localhost:9092',
    topic: str = "topic1",
    messagesource: str = "pyspark_module/input.csv",
    type: str = "test"
):
    bootstrap_servers = bootstrap_server
    producer = KafkaProducer(
        bootstrap_servers=bootstrap_servers
    )

    if type == "test":
        while True:
            print("test msg generating")
            message = f"Message generated at {time.time()}"
            producer.send(topic, value=message.encode('utf-8'))
            time.sleep(1)

    elif type == "production":
        print("Real msg generating")
        with open(messagesource, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                print(row, "is sending -----------------------------")
                producer.send(topic, bytes(str(row), encoding='utf-8'))

    print("Producer shutting down")
    producer.close()
