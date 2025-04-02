import os

class Config(object):
    BOT_TOKEN = "7641591924:AAHZaHqvP5uEjnphGf3RhCkimVIGscKu6MU"
    API_ID = 26468828
    API_HASH = "4693513c08d1ac6af15f95b116c29478"
    AUTH_USER = os.environ.get('AUTH_USERS', '7935947598').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "http://master-api-v3.vercel.app"
    CREDIT = ""
