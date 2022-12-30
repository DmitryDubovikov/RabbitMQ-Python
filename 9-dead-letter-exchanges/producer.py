import pika

credentials = pika.PlainCredentials("rmuser", "rmpassword")
connection_parameters = pika.ConnectionParameters("127.0.0.1", 5672, "/", credentials)

connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.exchange_declare(exchange="mainexchange", exchange_type="direct")

message = "This message might expire"
channel.basic_publish(exchange="mainexchange", routing_key="test", body=message)

print(f"sent message: {message}")
connection.close()
