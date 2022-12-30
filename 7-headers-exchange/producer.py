import pika

credentials = pika.PlainCredentials("rmuser", "rmpassword")
connection_parameters = pika.ConnectionParameters("127.0.0.1", 5672, "/", credentials)

connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.exchange_declare("headersexchange", "headers")

message = "This message will be sent with headers"

channel.basic_publish(
    exchange="headersexchange",
    routing_key="",
    body=message,
    properties=pika.BasicProperties(headers={"name": "dmitry"}),
)

print(f"sent message: {message}")

connection.close()
