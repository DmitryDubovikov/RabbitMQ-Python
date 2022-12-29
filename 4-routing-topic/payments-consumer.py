import pika
from pika.exchange_type import ExchangeType


def on_message_received(ch, method, properties, body):
    print(f"Payments Service - received new message: {body}")


credentials = pika.PlainCredentials("rmuser", "rmpassword")
connection_parameters = pika.ConnectionParameters("localhost", 5672, "/", credentials)

connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.exchange_declare(exchange="mytopic", exchange_type=ExchangeType.topic)
queue = channel.queue_declare(queue="", exclusive=True)
channel.queue_bind(
    exchange="mytopic", queue=queue.method.queue, routing_key="#.payments"
)

channel.basic_consume(
    queue=queue.method.queue, auto_ack=True, on_message_callback=on_message_received
)

print("Payments Service - Starting Consuming")
channel.start_consuming()
