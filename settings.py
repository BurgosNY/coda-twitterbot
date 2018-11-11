import environ


root = environ.Path(__file__) - 2
env = environ.Env(DEBUG=(bool, False),)
environ.Env.read_env()  # reading .env file

CONSUMER_KEY = env('CONSUMER_KEY')
CONSUMER_SECRET = env('CONSUMER_SECRET')
ACCESS_TOKEN = env('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = env('ACCESS_TOKEN_SECRET')
