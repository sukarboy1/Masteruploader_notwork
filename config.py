import os

class Config(object):
    BOT_TOKEN = "7625355619:AAGg4gP0c4pO2ut5ZDFD6esqk_5edIeOulo"
    API_ID = 27032249
    API_HASH = "448a570f9b48fd49efe918600b282b81"
    AUTH_USER = os.environ.get('AUTH_USERS', '7001787251').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://api.masterapi.tech"
    CREDIT = "dq"
