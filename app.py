from flask import Flask, request
import re

app = Flask(__name__)

@app.route('/')
def index():
    try:
        ip = request.headers['X-Forwarded-For'].split(', ')[0]
    except KeyError:
        ip = request.remote_addr
    valid = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
    if valid.match(ip):
        return ip
    else:
        abort(400)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)