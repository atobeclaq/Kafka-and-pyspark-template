#!/bin/bash

# Start ZooKeeper
# To Do: pointing to your own kafka
cd /Path/to/kafka_2.12-3.4.0
# properties can redirect to the server.properties in this directory
bin/zookeeper-server-start.sh config/zookeeper.properties
