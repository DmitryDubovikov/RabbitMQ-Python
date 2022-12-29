import pika
from pika.exchange_type import ExchangeType


credentials = pika.PlainCredentials("rmuser", "rmpassword")
connection_parameters = pika.ConnectionParameters("127.0.0.1", 5672, "/", credentials)

connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()
channel.exchange_declare(exchange="mytopic", exchange_type=ExchangeType.topic)

message = "A european user paid for something"
channel.basic_publish(
    exchange="mytopic", routing_key="user.europe.payments", body=message
)
print(f"sent message: {message}")

message = "A european business ordered goods"
channel.basic_publish(
    exchange="mytopic", routing_key="business.europe.orders", body=message
)
print(f"sent message: {message}")


connection.close()
