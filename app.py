import argparse
import asyncio
import json
from quart import (
    Quart,
    render_template,
    stream_with_context,
)

app = Quart(__name__,
    static_url_path='', 
    static_folder='static',
    template_folder='templates',
)


@app.route('/stream')
async def stream_json():
    async def generate_data():
        for i in range(10):
            data = {'id': i, 'value': 'Hello from Quart!'}
            yield json.dumps(data) + '\n'
            await asyncio.sleep(1)  # Simulate some delay

    return generate_data(), 200, {'Content-Type': 'application/x-ndjson'}

@app.route("/")
async def home():
    return await render_template("index.html")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("port",type=int)
    parser.add_argument('-d', '--debug',action='store_true')
    args = parser.parse_args()
    app.run(debug=args.debug,host="0.0.0.0",port=args.port)

