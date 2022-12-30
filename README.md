# RabbitMQ-Python

Run RabbitMQ:

    docker-compose build
    docker-compose up

RabbitMQ management (browser-based UI):

    http://localhost:15672/

Python:

    pipenv shell
    pipenv install

## 1. Basics

Run:

    consumer.py
    producer.py

Check that messages are produced and consumed. Check Message rates, Connections, Channels and Queues in RabbitMQ management.

## 2. Competing consumers

Run:

    consumer.py
    producer.py

 Check that messages are produced and consumed. Check Queued messages, Message rates, Connections, Channels and Queues in RabbitMQ management.

 Then run 2 consumers and 1 producer. Check differences in RabbitMQ management.

## 3. Publish / Subscribe (pub-sub)

Run:

    first-consumer.py
    second-consumer.py
    producer.py

Check that both consumers received new message from exchange="pubsub". Check for exchange="pubsub" in Exchanges in RabbitMQ management.

## 4. Routing using the Direct exchange

Run:

    analytics-consumer.py
    payments-consumer.py
    producer.py

Check that consumers received new messages according to their routing_key. Check for exchange="routing" in Exchanges in RabbitMQ management.

## 4. Routing using the Topic exchange

Run:

    analytics-consumer.py
    payments-consumer.py
    user-consumer.py
    producer.py

Check that consumers received new messages according to their routing_key. Check for exchange="mytopic" in Exchanges in RabbitMQ management.

## 5. Request-Reply

Run:

    client.py
    server.py

Check that request and reply are sent and recieved. Check Queues in RabbitMQ management.