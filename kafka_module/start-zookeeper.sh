#!/bin/bash

# Start ZooKeeper
cd /Path/to/kafka_2.12-3.4.0/kafka_2.12-3.4.0
# properties can redirect to the server.properties in this directory
bin/zookeeper-server-start.sh config/zookeeper.properties
