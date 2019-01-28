#!/usr/bin/env python3

import os, unittest, requests, json, argparse
from base64 import b64encode

header_json = {'content-type':'application/json'}
hostname = 'localhost'
port = 5000

url = 'http://{}:{}'.format(hostname, port)
post_url = url + '/post'
posts_url = url + '/posts'

class FlaskTestCase(unittest.TestCase):

    def test_page_not_found(self):
        rsp = requests.get(url)
        self.assertTrue(rsp.status_code == 404)

    def test_post_returns_200(self):
        data = {
            "title" : b64encode(os.urandom(6)).decode('utf-8'), 
            "body" : "test_post_returns_200"
        }
        rsp = requests.post(post_url, json=data, headers=header_json)

        self.assertTrue(rsp.status_code == 200)

    def test_posts_returns_200(self):
        rsp = requests.get(posts_url)
        self.assertTrue(rsp.status_code == 200)

    def test_post_shows_what_was_posted(self):
        '''
        Create a randomized string to persist as a post's title. POST it, then
        get the list of posts and find that string among the titles of the posts.
        '''
        random_title = b64encode(os.urandom(6)).decode('utf-8')
        data = {
            "title" : random_title, 
            "body" : "test_post_shows_what_was_posted"
        }
        rsp = requests.post(post_url, json=data, headers=header_json)
        self.assertTrue(rsp.status_code == 200)
        
        rsp = requests.get(posts_url)
        found = False
        for post in rsp.json():
            if random_title == post['title']: 
                found = True
        self.assertTrue(found)

        

if __name__ == '__main__':
    unittest.main()
