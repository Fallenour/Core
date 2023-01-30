from amqpstorm import Connection


connection = Connection('127.0.0.1', 'guest', 'guest')
channel = connection.channel()
channel.basic.consume(callback=on_message, queue='simple_queue', no_ack=False)
channel.start_consuming(to_tuple=False)


def on_message(message):
    """This function is called on message received.

    :param message: Delivered message.
    :return:
    """
    print("Message:", message.body)

    # Acknowledge that we handled the message without any issues.
    message.ack()

    # Reject the message.
    # message.reject()

    # Reject the message, and put it back in the queue.
    # message.reject(requeue=True)


### Notes on Rabbit ###
# https://riptutorial.com/python/example/11593/how-to-consume-messages-from-rabbitmq
# https://www.rabbitmq.com/tutorials/tutorial-two-python.html