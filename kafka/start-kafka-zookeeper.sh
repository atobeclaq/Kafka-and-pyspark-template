#!/bin/bash

# Get the absolute path of the current directory
current_dir=$(cd "$(dirname "$0")" && pwd)

# Function to check if ZooKeeper has started
check_zookeeper_started() {
    nc -z localhost 2181
    return $?
}

# Start ZooKeeper in a new terminal
osascript -e "tell application \"Terminal\" to do script \"cd '$current_dir' && ./start-zookeeper.sh\""

# Wait for ZooKeeper to start
while ! check_zookeeper_started; do
    sleep 1
done

# Start Kafka in another terminal
osascript -e "tell application \"Terminal\" to do script \"cd '$current_dir' && ./start-kafka.sh\""

echo "ZooKeeper and Kafka started successfully in separate terminals."
