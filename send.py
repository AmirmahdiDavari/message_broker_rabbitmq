import pika
from config import queue

def send_message(message,queue=queue):
    try:

        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()

        channel.queue_declare(queue=queue)

        channel.basic_publish(exchange='', routing_key=queue, body=message)
        print(f" [x] Sent 'message' {message}")
        connection.close()
    except pika.exceptions.AMQPConnectionError as e:
        print("Failed to connect to RabbitMQ server:", e)
    except Exception as e:
        print("An error occurred:", e)
