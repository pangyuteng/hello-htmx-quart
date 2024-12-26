import os
import argparse
import asyncio
import datetime
import numpy as np
from quart import (
    Quart,
    websocket,
    render_template,
    jsonify
)

from jinja2 import Environment, FileSystemLoader
THIS_DIR = os.path.dirname(os.path.abspath(__file__))

app = Quart(__name__,
    static_url_path='', 
    static_folder='static',
    template_folder='templates',
)

@app.route("/ping")
async def ping():
    return jsonify("pong")
# 123
@app.websocket('/ws-basic')
async def ws_basic():
    try:
        while True:
            tstamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S.%f")
            data_str = f"""
            <div id="notifications" hx-swap-oob="true">
            New message received {tstamp}
            </div>
            """
            await websocket.send(data_str)
            await asyncio.sleep(1)  # Simulate some delay
    except asyncio.CancelledError:
        print('Client disconnected')
        raise
    # no return, means connection is kept open.

@app.route("/basic")
async def basic():
    return await render_template("basic.html")

@app.route("/csv-data")
async def csv_data():
    random_data = np.random.rand(10).astype(float).tolist()
    return jsonify(random_data)

template_folder = os.path.join(THIS_DIR,"templates")
def render_html(html_file,**kwargs):
    j2_env = Environment(loader=FileSystemLoader(template_folder))
    return j2_env.get_template(html_file).render(**kwargs)

@app.websocket('/ws-data')
async def ws_data():
    try:
        while True:
            tstamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S.%f")
            mylist = []
            for n in range(100):
                myitem = (np.random.rand(100)*2).astype(float).tolist()
                mylist.append(myitem)
            data_str = render_html("refresh.html",mylist=mylist,tstamp=tstamp)
            await websocket.send(data_str)
            await asyncio.sleep(0.01)
    except asyncio.CancelledError:
        print('Client disconnected')
        raise
    # no return, means connection is kept open.

@app.route("/")
async def home():
    return await render_template("index.html")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("port",type=int)
    parser.add_argument('-d', '--debug',action='store_true')
    args = parser.parse_args()
    app.run(debug=args.debug,host="0.0.0.0",port=args.port)

"""

"""