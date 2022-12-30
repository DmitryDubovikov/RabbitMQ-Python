import pika


def on_request_message_received(ch, method, properties, body):
    print(f"Received Request: {properties.correlation_id}")
    ch.basic_publish(
        "",
        routing_key=properties.reply_to,
        body=f"Hey its your reply to {properties.correlation_id}",
    )
    print(f"Sending Reply to: {properties.correlation_id}")


credentials = pika.PlainCredentials("rmuser", "rmpassword")
connection_parameters = pika.ConnectionParameters("127.0.0.1", 5672, "/", credentials)

connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.queue_declare(queue="request-queue")

channel.basic_consume(
    queue="request-queue",
    auto_ack=True,
    on_message_callback=on_request_message_received,
)

print("Starting Server")

channel.start_consuming()
