import pika

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

message = "Hello this is my message sent with routing_key=mainrouting"
channel.basic_publish(exchange="mainexchange", routing_key="mainrouting", body=message)
print(f"sent message: {message}")

message = "Hello this is my message sent with routing_key=altrouting"
channel.basic_publish(exchange="mainexchange", routing_key="altrouting", body=message)
print(f"sent message: {message}")

connection.close()
