from flask import Flask, jsonify, request
import redis
import os

app = Flask(__name__)
redis_host = os.environ.get("REDIS_HOST", "localhost")
r = redis.Redis(host=redis_host, port=6379, decode_responses=True)

@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/counter')
def counter():
    count = r.incr("counter")
    return f"This page has been visited {count} times."

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)