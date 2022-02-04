FROM ubuntu:focal

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

RUN apt-get update -y
RUN apt install software-properties-common -y

# Python 3.10
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt install -y python3.10 \
                python3-pip

# Java
RUN apt-get install -y openjdk-11-jdk


# Install pip requirements  
COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

ENV MONGO_INPUT_URI="mongodb://localhost:27017"
ENV MONGO_OUTPUT_URI="mongodb://localhost:27017"
ENV MONGO_DB="company_one"
ENV MONGO_COLLECTION="sales"
ENV MONGO_SPARK_PACKAGE="org.mongodb.spark:mongo-spark-connector_2.12:3.0.1"

ENV KAFKA_SPARK_PACKAGE="org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.1"
ENV KAFKA_BOOTSTRAP_SERVER="localhost:9092"
ENV KAFKA_TOPIC_NAME="sales"

CMD ["python3", "stream.py"]
