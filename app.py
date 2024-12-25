import argparse
import asyncio
import json
from quart import (
    Quart,
    websocket,
    render_template,
)

app = Quart(__name__,
    static_url_path='', 
    static_folder='static',
    template_folder='templates',
)

@app.websocket('/ws')
async def ws():
    try:
        while True:
            #data = await websocket.receive()
            for i in range(3):
                data = {'id': i, 'value': 'Hello from Quart!'}
                yield json.dumps(data) + '\n'
                await websocket.send(data)
                await asyncio.sleep(1)  # Simulate some delay
    except asyncio.CancelledError:
        print('Client disconnected')
        raise
    # no return, means connection is kept open.

@app.route("/")
async def home():
    return await render_template("js-test.html")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("port",type=int)
    parser.add_argument('-d', '--debug',action='store_true')
    args = parser.parse_args()
    app.run(debug=args.debug,host="0.0.0.0",port=args.port)

