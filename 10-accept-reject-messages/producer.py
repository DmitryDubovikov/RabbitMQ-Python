import pika

credentials = pika.PlainCredentials("rmuser", "rmpassword")
connection_parameters = pika.ConnectionParameters("127.0.0.1", 5672, "/", credentials)

connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.exchange_declare(exchange="acceptrejectexchange", exchange_type="fanout")
message = "Lets send this"

while True:
    channel.basic_publish(
        exchange="acceptrejectexchange", routing_key="samplekey", body=message
    )
    print(f"sent message: {message}")
    input("Press any key to continue")
