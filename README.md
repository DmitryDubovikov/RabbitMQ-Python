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