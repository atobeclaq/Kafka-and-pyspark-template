# Kafka and Spark Integration

This project demonstrates the integration of Apache Kafka and Apache Spark for processing streaming data.

## Features

- Kafka producer: Generates test messages or reads data from a CSV file and sends it to a Kafka topic.
- Kafka consumer: Subscribes to a Kafka topic, receives messages, and processes them.
- PySpark data transformation: Applies data transformation logic using PySpark DataFrame API.
- Output to CSV: Saves the transformed data as a CSV file.

## Prerequisites

- Python 3.x
- Kafka
- Apache Spark

## Installation

1. Install the required Python dependencies:
```pip install kafka-python pyspark```

2. Install and configure Kafka. Follow the official Kafka documentation for installation instructions.

3. Install Apache Spark. Follow the official Spark documentation for installation instructions.

4. Clone the repository:

```bash
git clone https://github.com/atobeclaq/Kafka-and-pyspark-template.git

## Usage

1. Start the Kafka server and ZooKeeper by running.
```shell
./kafka/start-kafka-zookeeper.sh
```

2. In a new terminal, run the Kafka producer:
```shell
python main.py
```
This script will start sending messages to a Kafka topic, and the script will read and process the messages using Spark Streaming.

## Customization

1. To customize the transformation logic in the PySpark job, modify the transform_data function in sample_spark_job.py.

2. To change the input data format or source, update the input.csv file or modify the producer module.

3. To change where the streaming data is piped to, modify the PySpark sample file.


## Helper

check the port of the zookeeper
```lsof -i :2181```

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License.