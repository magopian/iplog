import os
import sqlite3

from flask import Flask, g, render_template, request
from datetime import datetime


app = Flask(__name__)
HERE = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(HERE, 'db.sqlite3')


@app.route('/', methods=['GET', 'POST'])
def home():
    if 'empty' in request.args:
        empty_db()

    if 'store' in request.args:
        exec_db('INSERT INTO logs VALUES (?, ?, ?)',
                [datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                 request.remote_addr,
                 request.args.get('note', '')])

    logs = query_db('SELECT * from logs ORDER BY timestamp DESC')
    return render_template('iplog.html', now=datetime.now(), logs=logs)


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def exec_db(query, args=()):
    conn = get_db()
    cur = conn.execute(query, args)
    conn.commit()
    return cur


def query_db(query, args=(), one=False):
    cur = exec_db(query, args=args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


def empty_db():
    with app.app_context():
        exec_db('DELETE FROM logs')


if __name__ == '__main__':
    app.debug = True
    app.run()
