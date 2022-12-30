import pika


def on_message_received(ch, method, properties, body):
    print(f"received new message: {body}")


credentials = pika.PlainCredentials("rmuser", "rmpassword")
connection_parameters = pika.ConnectionParameters("127.0.0.1", 5672, "/", credentials)

connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.exchange_declare(exchange="secondexchange", exchange_type="fanout")
channel.queue_declare(queue="letterbox")
channel.queue_bind("letterbox", "secondexchange")

channel.basic_consume(
    queue="letterbox", auto_ack=True, on_message_callback=on_message_received
)

print("Starting Consuming")

channel.start_consuming()
