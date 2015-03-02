from flask import Flask
from flask import render_template

import os

import requests


app = Flask(__name__)
app.debug = os.environ.get('DEBUG', '0') in ('true', 'True', '1')


TSURU_TOKEN = os.environ.get("TSURU_TOKEN")
TSURU_HOST = os.environ.get("TSURU_HOST")


@app.route("/")
def app_list():
    headers = {'authorization': TSURU_TOKEN}
    url = '{}/apps'.format(TSURU_HOST)
    app_list = requests.get(url, headers=headers).json()
    return render_template('app_list.html', app_list=app_list)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "8888")))
