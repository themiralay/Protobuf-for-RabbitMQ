import sys
import pika
import protos.awesome_pb2 as awesome

def protoMaker():
    awesomeMessage = awesome.AwesomeMessage()
    awesomeMessage.awesomeField="TEST PROTOBUF MESSAGE CRYPTOTYLER"
    return awesomeMessage

credentials = pika.PlainCredentials('[RABBIT_USERNAME]', '[RABBIT_PASSWORD]')
parameters = pika.ConnectionParameters('[RABBIT_PASSWORD]',
                                   5672,
                                   '/',
                                   credentials)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

message = protoMaker().SerializeToString()

#message = ' '.join(sys.argv[1:]) or "CRYPTOTYLER"
# channel.basic_publish(exchange='crawler',
#                       routing_key='url_crawl',
#                       body=message)
channel.basic_publish(
    exchange='',
    routing_key='url_data_crawler',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
    ))
print(" [x] Sent %r" % message)
connection.close()