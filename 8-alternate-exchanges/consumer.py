import pika


def alt_queue_on_message_received(ch, method, properties, body):
    print(f"Alt exchange - received new message: {body}")


def main_queue_on_message_received(ch, method, properties, body):
    print(f"Main exchange - received new message: {body}")


credentials = pika.PlainCredentials("rmuser", "rmpassword")
connection_parameters = pika.ConnectionParameters("127.0.0.1", 5672, "/", credentials)

connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()


channel.exchange_declare(exchange="altexchange", exchange_type="fanout")

channel.exchange_declare(
    exchange="mainexchange",
    exchange_type="direct",
    arguments={"alternate-exchange": "altexchange"},
)

channel.queue_declare(queue="altexchangequeue")
channel.queue_bind("altexchangequeue", "altexchange")

channel.basic_consume(
    queue="altexchangequeue", on_message_callback=alt_queue_on_message_received
)

channel.queue_declare(queue="mainexchangequeue")
channel.queue_bind("mainexchangequeue", "mainexchange", "mainrouting")

channel.basic_consume(
    queue="mainexchangequeue", on_message_callback=main_queue_on_message_received
)

print("Starting Consuming")
channel.start_consuming()
