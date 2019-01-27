#!/usr/bin/env python3

import sqlite3, copy, os
from flask import Flask, jsonify, request, abort
from base64 import b64encode

app = Flask(__name__)

@app.route('/post', methods=['POST'])
def post():
    '''
    Parameters: title, body
    
    Generates a random base 64 string for a post_id.
    Persists the post_id, title, and body of a post to sqlite db.
    '''
    if not request.is_json():
        abort(400)
    try:
        entry = {
            'post_id' : b64encode(os.urandom(15)).decode('utf-8'),
            'title' : request.json['title'],
            'body' : request.json['body']
        }
    except KeyError:
        abort(400)

    conn = sqlite3.connect(r'blog.db')
    c = conn.cursor()
    c.execute('insert into posts VALUES (?, ?, ?);', 
        (entry['post_id'], entry['title'], entry['body']))
    conn.commit()
    conn.close()
    return jsonify({'post_id':entry['post_id']})

@app.route('/posts', methods=['GET'])
def posts():
    '''
    Lists the posts persisted in the db.
    '''
    conn = sqlite3.connect(r'blog.db')
    c = conn.cursor()
    raw_posts = c.execute('select * from posts;').fetchall()
    conn.close()
    posts = [{
        'post_id' : post[0], 
        'title' : post[1], 
        'body' : post[2]
    } for post in raw_posts]
    return jsonify(posts)
    

if __name__ == '__main__':
    app.run(debug=True)
