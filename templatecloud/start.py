import os
import threading
from time import time
from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'   

@app.route('/servers')
def list_servers():
    conn = create_openstack_connection()
    for server in conn.compute.servers():
        print(server)

def run_flask():
    app.run(host="0.0.0.0", port=5234)

# Initialize and authenticate the connection
def create_openstack_connection():
    conn = openstack.connect(
        auth_url='http://172.16.15.101:5000/v3',
        project_name='cc',
        username='admin',
        password='abc',
        region_name='Default',
        user_domain_name='Default',
        project_domain_name='Default'
    )
    return conn

if __name__ == "__main__":
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()