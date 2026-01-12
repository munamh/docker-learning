from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def welcome():
    return "Welcome to this webpage! "

@app.route('/count')
def count():
    redis.incr('hits')
    count = str(redis.get('hits'), 'utf-8')
    return f"Welcome to this webpage!, This webpage has been viewed {count} times."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
    
from app import app