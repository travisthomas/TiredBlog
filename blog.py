#!/usr/bin/env python3

import sqlite3, os
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
    if not request.is_json:
        abort(400)
    try:
        entry = {
            'post_id' : b64encode(os.urandom(15)).decode('utf-8'),
            'title' : request.json['title'],
            'body' : request.json['body']
        }
    except KeyError:
        abort(400)

    database.write_post(entry)
    return jsonify({'post_id':entry['post_id']})

@app.route('/posts', methods=['GET'])
def posts():
    '''
    Lists the posts persisted in the db.
    '''
    raw_posts = database.get_all_posts()
    posts = []
    for post in raw_posts:
        posts.append({'post_id' : post[0], 'title' : post[1], 'body' : post[2]})
    return jsonify(posts)

class Database:

    def __init__(self, path):
        self.path = path

    def get_all_posts(self):
        connection = sqlite3.connect(self.path)
        cursor = connection.cursor()
        raw_posts = cursor.execute('select post_id, title, body from posts;').fetchall()
        
        connection.close()
        return raw_posts

    def write_post(self, entry):
        connection = sqlite3.connect(self.path)
        cursor = connection.cursor()
        cursor.execute('insert into posts VALUES (?, ?, ?);', 
            (entry['post_id'], entry['title'], entry['body']))
        connection.commit()
        connection.close()



if __name__ == '__main__':
    database = Database('blog.db')
    app.run(host="0.0.0.0")
