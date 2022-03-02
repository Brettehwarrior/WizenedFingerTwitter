from EldenRingMessage import message
import bot

if __name__ == '__main__':
    message_data = message.messages()
    factory = message.MessageFactory(message_data)

    bot.send_tweet(factory.message())