import argparse
import asyncio
import datetime
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

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("port",type=int)
    parser.add_argument('-d', '--debug',action='store_true')
    args = parser.parse_args()
    app.run(debug=args.debug,host="0.0.0.0",port=args.port)

