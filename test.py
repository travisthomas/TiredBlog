#!/Users/travisthomas/virtualenvs/flask/bin/python

import os, unittest, requests

url = 'http://localhost:5000'

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_responds(self):
        data = '{"title":"this is a title", "body":"Tis the season."}'
        rsp = requests.get(url, data)
        print(rsp)
        self.assertTrue(rsp)

if __name__ == '__main__':
    unittest.main()
