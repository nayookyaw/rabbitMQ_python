"""
    *
    |  Nay Oo Kyaw |
    |  nayookyaw.nok@gmail.com |
    *
"""

import pika

class Sender:
    def __init__(self):
        self.host = 'localhost'

    def publish(self):
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.host))
        channel = connection.channel()

        channel.queue_declare(queue='hello')
        channel.basic_publish(exchange='', routing_key='hello',
                                body='Hello Developers!')
        print ("[x] Send 'Hello World '")
        connection.close()

if __name__ == '__main__':
    try:
        print ("Start sending..")
        sender = Sender()
        sender.publish()
        print ("After published")
    except KeyboardInterrupt:
        print ("Key Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
