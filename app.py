from socket import inet_pton, AF_INET, AF_INET6
from flask import abort, Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    # Make best-effort guess at the client's IP
    try:
        ip = request.headers['X-Forwarded-For'].split(', ')[0]
    except KeyError:
        ip = request.remote_addr
    # Attempt to sanitize/validate against possible
    try:
        inet_pton(AF_INET, ip)
    except OSError:
        try:
            inet_pton(AF_INET6, ip)
        except OSError:
            abort(400)
    finally:
        return ip
