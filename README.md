# Kafka and Spark Integration

This project demonstrates the integration of Apache Kafka and Apache Spark for processing streaming data.

## Prerequisites

- Python 3.x
- Kafka
- Apache Spark

## Installation

1. Install the required Python dependencies:
```pip install kafka-python pyspark```

2. Install and configure Kafka. Follow the official Kafka documentation for installation instructions.

3. Install Apache Spark. Follow the official Spark documentation for installation instructions.

## Project Structure

- `kafka/sample-kafka-producer.py`: Kafka producer script that sends messages to a Kafka topic.
- `kafka/sample-kafka-consumer.py`: Spark consumer script that reads and processes messages from a Kafka topic.

## Usage

1. Start the Kafka server and ZooKeeper by running.
```shell
./kafka/start-kafka-zookeeper.sh
```

2. In a new terminal, run the Kafka producer:
```shell
python kafka/producer.py
```
This script will start sending messages to a Kafka topic.

3. In another terminal, run the Spark consumer:
```shell
python spark/consumer.py
```

This script will read and process the messages using Spark Streaming.

Customize the processing logic inside the spark/consumer.py script according to your requirements.

## Helper

check the port of the zookeeper
```lsof -i :2181```

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License.