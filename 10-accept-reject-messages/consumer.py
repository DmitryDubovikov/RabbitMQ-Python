import pika


def on_message_received(ch, method, properties, body):

    if method.delivery_tag % 5 == 0:
        ch.basic_ack(delivery_tag=method.delivery_tag, multiple=True)

    print(f"Received new message: {method.delivery_tag}")


credentials = pika.PlainCredentials("rmuser", "rmpassword")
connection_parameters = pika.ConnectionParameters("127.0.0.1", 5672, "/", credentials)

connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()


channel.exchange_declare(exchange="acceptrejectexchange", exchange_type="fanout")
channel.queue_declare(queue="letterbox")
channel.queue_bind("letterbox", "acceptrejectexchange")

channel.basic_consume(queue="letterbox", on_message_callback=on_message_received)

print("Starting Consuming")
channel.start_consuming()
