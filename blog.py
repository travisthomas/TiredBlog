#!/usr/bin/env python

import sqlite3, copy, os
from flask import Flask, jsonify, request, abort
from base64 import b64encode

app = Flask(__name__)

@app.route('/post', methods=['POST'])
def post():
    if not request.json:
        abort(400)
    try:
        entry = {
            'id' : b64encode(os.urandom(15)),
            'title' : request.json['title'],
            'body' : request.json['body']
        }
    except KeyError:
        abort(400)

    conn = sqlite3.connect(r'blog.db')
    c = conn.cursor()
    c.execute('insert into posts VALUES (?, ?, ?);', 
        (entry['id'], entry['title'], entry['body']))
    conn.commit()
    conn.close()
    return jsonify(entry)

@app.route('/posts')
def posts():
    conn = sqlite3.connect(r'blog.db')
    c = conn.cursor()
    posts = c.execute('select * from posts;').fetchall()
    conn.close()
    return jsonify(posts)
    

if __name__ == '__main__':
    app.run(debug=True)
    close_db()
