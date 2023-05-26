#!/bin/bash

# Start ZooKeeper
cd /Users/lichen/Downloads/kafka_2.12-3.4.0
# properties can redirect to the server.properties in this directory
bin/zookeeper-server-start.sh config/zookeeper.properties
