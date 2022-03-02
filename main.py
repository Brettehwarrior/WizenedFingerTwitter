from EldenRingMessage import message

if __name__ == '__main__':
    message_data = message.messages()
    factory = message.MessageFactory(message_data)

    print(factory.message())