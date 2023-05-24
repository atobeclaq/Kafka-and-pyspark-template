#!/bin/bash
SPARK_HOME="/path/to/spark"
$SPARK_HOME/sbin/start-master.sh
$SPARK_HOME/sbin/start-worker.sh spark://localhost:7077
