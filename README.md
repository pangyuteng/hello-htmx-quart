# htmx-quart


docker compose build

docker run -it -u $(id -u):$(id -g) \
    -p 5000:5000 -v /mnt:/mnt -w $PWD \
    htmx-quart bash

## TODO

demo/excercise to plot random numbers using htmx/quart/webesocket.
 
https://v1.htmx.org/extensions/web-sockets/

https://quart.palletsprojects.com/en/latest/how_to_guides/websockets.html

https://stackoverflow.com/questions/69954196/quart-chat-server-example

https://stackoverflow.com/questions/67090607/python-quart-websocket-send-data-between-two-clients

https://python-team.pages.debian.net/packages/quart/websockets.html

keywords: stream json with python quart to javascript

https://plotly.com/javascript/plotlyjs-function-reference/