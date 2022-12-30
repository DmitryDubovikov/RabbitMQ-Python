import pika

credentials = pika.PlainCredentials("rmuser", "rmpassword")
connection_parameters = pika.ConnectionParameters("127.0.0.1", 5672, "/", credentials)

connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

# declare 2 exchanges
channel.exchange_declare(exchange="firstexchange", exchange_type="direct")
channel.exchange_declare(exchange="secondexchange", exchange_type="fanout")

channel.exchange_bind("secondexchange", "firstexchange")

message = "This message has gone through multiple exchanges"
channel.basic_publish(exchange="firstexchange", routing_key="", body=message)
print(f"sent message: {message}")

connection.close()
