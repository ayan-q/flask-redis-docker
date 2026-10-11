return f"Welcome Ayan! DevOps Pipeline Active. Page viewed {count} times.\n"import time
import redis
from flask import Flask

app = Flask(__name__)
# Notice how we use 'redis' as the hostname. Docker Compose's internal DNS resolves this automatically!
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return f"Welcome Ayan! DevOps Pipeline Active. Page viewed {count} times.\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
