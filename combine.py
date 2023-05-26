from kafka_module import Consumer, Producer
import subprocess

# Specify the path to the bash script
bash_script_path = '/kafka_module/start-kafka-zookeeper.sh'

# Run the bash script
subprocess.run(['bash', bash_script_path])

Producer(
    bootstrap_server='localhost:9092',
    topic = "topic1",
    messagesource= "pyspark/input.csv",
    type = "production" # Can just pass 'test' if just want test if the system will run as expected
    )

for message in consumer(bootstrap_server= "localhost:9092", topics= "topic1",group_id = "my-group"):
    print(f"Received message: {message}")
