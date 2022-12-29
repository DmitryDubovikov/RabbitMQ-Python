import pika
from pika.exchange_type import ExchangeType


credentials = pika.PlainCredentials("rmuser", "rmpassword")
connection_parameters = pika.ConnectionParameters("127.0.0.1", 5672, "/", credentials)

connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.exchange_declare(exchange="pubsub", exchange_type=ExchangeType.fanout)

message = f"Hello, I want to broadcast this message"
channel.basic_publish(exchange="pubsub", routing_key="", body=message)
print(f"sent message: {message}")

connection.close()
