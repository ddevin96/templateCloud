from gevent import monkey
monkey.patch_all()  # Patches for cooperative concurrency

from flask import Flask
from gevent.pywsgi import WSGIServer
import threading
import time
import openstack

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'   

@app.route('/servers')
def list_servers():
    print("Listing servers")
    conn = create_openstack_connection()
    print("Connection created")
    for server in conn.compute.servers():
        print(server)

def start_flask_server():
    print("start flask server")
    http_server = WSGIServer(('0.0.0.0', 9696), app)
    http_server.serve_forever()
    print("Flask server sstop")

# Initialize and authenticate the connection
def create_openstack_connection():
    print("Creating OpenStack connection")
    conn = openstack.connect(
        auth_url='http://172.16.15.101/identity',
        project_name='service',
        username='admin',
        password='abc',
        region_name='RegionOne',
        user_domain_name='Default',
        project_domain_name='Default'
    )
    print(conn)
    return conn

if __name__ == "__main__":
    flask_thread = threading.Thread(target=start_flask_server)
    flask_thread.daemon = False  # Don't use daemon thread so it doesn't terminate abruptly
    flask_thread.start()
    print("Flask server started")