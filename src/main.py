#!/usr/bin/env python3
import json

import flask
import psycopg2
from flask import jsonify, Response
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from qovery_client.qovery import Qovery

# --- START INIT ---

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return "<h1>Welcome :)</h1><p>The current branch is <b>" + 'xxxxx' + "</b></p><p>Source code available " \
                                                                             "<a href='https://github.com/evoxmusic/flask-todo'>here</a></p>" \
                                                                             "<p>API resources available:</p>" \
                                                                             "<ul><li>GET /api/todo -> to list todo</li>" \
                                                                             "<li>GET /api/todo/:id -> to show todo by id</li>" \
                                                                             "<li>POST /api/todo -> to add todo</li>" \
                                                                             "<li>DELETE /api/todo/:id -> to delete todo by id</li></ul>"


if __name__ == '__main__':
    print('Server is ready!')
    app.run(host='0.0.0.0', port=5000)
