#!/bin/bash

# Get the absolute path of the current directory
current_dir=$(cd "$(dirname "$0")" && pwd)

# Function to check if ZooKeeper has started
check_zookeeper_started() {
    nc -z localhost 2181 < /dev/null
    lsof -i :2181
    echo $(nc -z localhost 2181 < /dev/null)
    echo $(lsof -i :2181)

    while true; do
        lsof -i :2181 | grep LISTEN > /dev/null
        if [ $? -eq 0 ]; then
            echo "ZooKeeper is running on port 2181."
            break
        else
            echo "ZooKeeper is not running on port 2181. Retrying..."
            sleep 1
        fi
    done
}


# Start ZooKeeper in a new terminal
osascript -e "tell application \"Terminal\" to do script \"cd '$current_dir' && ./start-zookeeper.sh\""

# Wait for ZooKeeper to start
check_zookeeper_started

# Start Kafka in another terminal
osascript -e "tell application \"Terminal\" to do script \"cd '$current_dir' && ./start-kafka.sh\""

echo "ZooKeeper and Kafka started successfully in separate terminals."
