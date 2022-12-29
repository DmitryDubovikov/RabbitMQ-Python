import pika, time, random

credentials = pika.PlainCredentials("rmuser", "rmpassword")
connection_parameters = pika.ConnectionParameters("127.0.0.1", 5672, "/", credentials)

connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()
channel.queue_declare(queue="letterbox")

messageId = 1

while True:
    message = f"Sending Message Id: {messageId}"
    channel.basic_publish(exchange="", routing_key="letterbox", body=message)
    print(f"sent message: {message}")
    time.sleep(random.randint(1, 4))
    messageId += 1
