#!/bin/bash

# Start Kafka
cd /Users/lichen/Downloads/kafka_2.12-3.4.0 
# properties can redirect to the server.properties in this directory
bin/kafka-server-start.sh config/server.properties