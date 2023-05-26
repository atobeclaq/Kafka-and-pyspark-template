from kafka import KafkaProducer
import time
import csv
import logging

def Producer(
    bootstrap_server:str = 'localhost:9092',
    topic:str = "topic1",
    messagesource:str = "pyspark_module/input.csv",
    type:str = "test"
):
    # Kafka broker configuration
    bootstrap_servers = bootstrap_server
    # Create Kafka producer
    producer = KafkaProducer(
        bootstrap_servers=bootstrap_servers
    )

    # Generate and send messages continuously
    if (type == "test"):
        while True:
            print("test msg generating")
            message = f"Message generated at {time.time()}"
            producer.send(topic, value=message.encode('utf-8'))
            time.sleep(1)  # Wait for 1 second before sending the next message
    elif(type == "production"):
        print("Real msg generating")
        with open(messagesource, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                print(row, "is sending -----------------------------")
                # Process the row as needed
                # Convert the row to a message value (e.g., JSON string, comma-separated string)
                # Send the message to Kafka
                producer.send(topic, bytes(str(row), encoding='utf-8'))


    # Close the producer (this part may not be executed since it's an infinite loop)
    print("Producer shutting down")
    producer.close()
