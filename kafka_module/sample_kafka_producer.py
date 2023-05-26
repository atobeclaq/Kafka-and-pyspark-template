from kafka import KafkaProducer
import time

def Producer(
    bootstrap_server:str = 'localhost:9092',
    topic:str = "topic1",
    messagesource:str = "pyspark/input.csv",
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
            message = f"Message generated at {time.time()}"
            producer.send(topic, value=message.encode('utf-8'))
            time.sleep(1)  # Wait for 1 second before sending the next message
    elif(type == "production"):
        with open(messagesource, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                # Process the row as needed
                # Convert the row to a message value (e.g., JSON string, comma-separated string)
                # Send the message to Kafka
                producer.send( topic, row)

    # Close the producer (this part may not be executed since it's an infinite loop)
    producer.close()
