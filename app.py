import traceback
import os
import sys
import ast
import pathlib
import argparse
import datetime
import aiohttp
import asyncio

from quart import Quart, render_template, websocket, jsonify


app = Quart(__name__,
    static_url_path='', 
    static_folder='static',
    template_folder='templates',
)

@app.route('/ping', methods=['GET'])
async def ping():
    return jsonify("pong")

@app.route("/")
async def hello():
    return await render_template("index.html")


@app.route("/api")
async def json():
    return {"hello": "world"}

@app.websocket("/ws")
async def ws():
    while True:
        await websocket.send("hello")
        await websocket.send_json({"hello": "world"})


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("port",type=int)
    parser.add_argument('-d', '--debug',action='store_true')
    args = parser.parse_args()
    app.run(debug=args.debug,host="0.0.0.0",port=args.port)

