#!/usr/bin/env python

import os, unittest, requests, json
from base64 import b64encode

url = 'http://localhost:5000'
post_url = url + '/post'
posts_url = url + '/posts'

class FlaskTestCase(unittest.TestCase):

    def test_page_not_found(self):
        rsp = requests.get(url)
        self.assertTrue(rsp.status_code == 404)

    def test_post_returns_200(self):
        data = {"title":"test_post_returns_200", "body":"you posted!"}
        rsp = requests.post(post_url, data=json.dumps(data), headers={
            'content-type':'application/json'})
        self.assertTrue(rsp.status_code == 200)

    def test_posts_returns_200(self):
        rsp = requests.get(posts_url)
        self.assertTrue(rsp.status_code == 200)

    def test_post_shows_what_was_posted(self):
        index = b64encode(os.urandom(4))
        data = {"title":index, 
            "body":"This has been posted and should be in the list of posts!"}
        rsp = requests.post(post_url, data=json.dumps(data), headers={
            'content-type':'application/json'})
        self.assertTrue(rsp.status_code == 200)
        rsp = requests.get(posts_url)
        found = False
        for post in rsp.json():
            if index in post: found = True
        self.assertTrue(found)

        

if __name__ == '__main__':
    unittest.main()
