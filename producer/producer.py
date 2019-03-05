#!/usr/bin/env python

import pika
import time
import random


time.sleep(30)

while True:
    try:
        params = pika.ConnectionParameters('rabbitmq', 5672)
        connection = pika.BlockingConnection(params)
        channel = connection.channel()

        channel.queue_declare(queue = 'random_queue')
        while True:
            num = random.randint(-1000, 1000)
            
            channel.basic_publish(exchange='', routing_key='random_queue', body=str(num))
            print('Sent:', num)
            
            time.sleep(random.randint(1, 10))
            
    except pika.exceptions.ConnectionClosed:
        print('Connection is closed')
    except Exception as ex:
        print(ex)

connection.close()
