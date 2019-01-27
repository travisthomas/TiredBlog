#!/usr/bin/env python3

import os, unittest, requests, json, argparse
from base64 import b64encode

url = 'http://localhost:5000'
post_url = url + '/post'
posts_url = url + '/posts'
header_json = {'content-type':'application/json'}

class FlaskTestCase(unittest.TestCase):

    def test_page_not_found(self):
        rsp = requests.get(url)
        self.assertTrue(rsp.status_code == 404)

    def test_post_returns_200(self):
        data = {
            "title" : "test_post_returns_200", 
            "body" : "you posted!"
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
        index = b64encode(os.urandom(6)).decode('utf-8')
        data = {
            "title" : index, 
            "body" : "This has been posted and should be in the list of posts!"
        }
        rsp = requests.post(post_url, json=data, headers=header_json)
        self.assertTrue(rsp.status_code == 200)
        
        rsp = requests.get(posts_url)
        found = False
        for post in rsp.json():
            if index == post['title']: found = True
        self.assertTrue(found)

        

if __name__ == '__main__':
    unittest.main()
