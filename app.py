import argparse
import asyncio
import datetime
import numpy as np
from quart import (
    Quart,
    websocket,
    render_template,
    render_template_string,
    jsonify
)

app = Quart(__name__,
    static_url_path='', 
    static_folder='static',
    template_folder='templates',
)

@app.route("/ping")
async def ping():
    return jsonify("pong")

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

@app.websocket('/ws-data')
async def ws_data():
    try:
        while True:
            tstamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S.%f")
            data_list = np.random.rand(10).astype(float).tolist()
            block = await render_template("refresh.html",data_list=data_list)
            await websocket.send(block.encode("utf-8"))
            await asyncio.sleep(1)
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

