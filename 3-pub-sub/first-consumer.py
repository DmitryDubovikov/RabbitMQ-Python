import pika


def on_message_received(ch, method, properties, body):
    print(f"FIRST consumer received new message: {body}")


credentials = pika.PlainCredentials("rmuser", "rmpassword")
connection_parameters = pika.ConnectionParameters("localhost", 5672, "/", credentials)

connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.exchange_declare(exchange="pubsub", exchange_type="fanout")

queue = channel.queue_declare(queue="", exclusive=True)
channel.queue_bind(exchange="pubsub", queue=queue.method.queue)

channel.basic_consume(
    queue=queue.method.queue, auto_ack=True, on_message_callback=on_message_received
)

print("Starting Consuming (1st)")
channel.start_consuming()
