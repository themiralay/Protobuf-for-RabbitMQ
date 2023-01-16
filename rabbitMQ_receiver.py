import pika, sys, os
import protos.awesome_pb2 as awesome


def main():
    credentials = pika.PlainCredentials('[RABBIT_USERNAME]', '[RABBIT_PASSWORD]')
    parameters = pika.ConnectionParameters('[RABBIT_PASSWORD]',
                                    5672,
                                    '/',
                                    credentials)

    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    def callback(ch, method, properties, body):
        awesomeMessage = awesome.AwesomeMessage()
        parsed = awesomeMessage.ParseFromString(body)
        print(" [x] Received %r" % parsed)

    channel.basic_consume(queue='protobuf_queue', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

main()
