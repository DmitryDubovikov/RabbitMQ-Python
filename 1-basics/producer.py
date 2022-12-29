import pika, time, datetime


credentials = pika.PlainCredentials("rmuser", "rmpassword")
connection_parameters = pika.ConnectionParameters("127.0.0.1", 5672, "/", credentials)

connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()
channel.queue_declare(queue="letterbox")

for i in range(5):
    message = f"Hello, this is my message, time is {datetime.datetime.now()}"
    channel.basic_publish(exchange="", routing_key="letterbox", body=message)
    print(f"sent message {i}: {message}")
    time.sleep(0.2)

message = "last message"
channel.basic_publish(exchange="", routing_key="letterbox", body=message)
print(f"sent message: {message}")

connection.close()
