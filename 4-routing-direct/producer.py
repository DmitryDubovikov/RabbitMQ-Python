import pika
from pika.exchange_type import ExchangeType


credentials = pika.PlainCredentials("rmuser", "rmpassword")
connection_parameters = pika.ConnectionParameters("127.0.0.1", 5672, "/", credentials)

connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()
channel.exchange_declare(exchange="routing", exchange_type=ExchangeType.direct)

message = "This message needs to be routed to both"
channel.basic_publish(exchange="routing", routing_key="both", body=message)
print(f"sent message: {message}")

message = "This message needs to be routed to analyticsonly"
channel.basic_publish(exchange="routing", routing_key="analyticsonly", body=message)
print(f"sent message: {message}")

message = "This message needs to be routed to paymentsonly"
channel.basic_publish(exchange="routing", routing_key="paymentsonly", body=message)
print(f"sent message: {message}")

connection.close()
