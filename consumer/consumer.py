#!/usr/bin/env python
import pika
import traceback, sys, time


def callback(ch, method, properties, body):
    print('Received:', body, flush=True)

time.sleep(50)

params = pika.ConnectionParameters('rabbitmq', 5672)
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='random_queue')
channel.basic_consume(callback, queue='random_queue', no_ack=True)

while True:
    try:
        channel.start_consuming()
    except pika.exceptions.ConnectionClosed:
        channel.stop_consuming()
    except Exception as ex:
        channel.stop_consuming()
        print(ex)

