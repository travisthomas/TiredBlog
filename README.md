# TiredBlog

This blog is quite tired. Fortunately, it has a RESTful API, so the more that you use it, the less tired it will become. Here's what you need to know.

## Prerequisites

You must have Python3 installed along with pipenv. Install the required packages by executing:

`pipenv install`

## Execution

`pipenv run ./blog.py` 

will start the blog server.  By default, the flask server binds to `localhost:5000`.

## The API

There are two endpoints: 

* `/post` to create a new blog entry on the server
* `/posts` to list the blog entries found on the server

To post a new blog entry, send an HTTP POST request with a JSON payload of `{'title': 'blog-title', 'body' : 'blog-body-text'}` to `http://localhost:5000/post`. To query the list of posts, send an HTTP GET request with no payload to `http://localhost:5000/posts`. Parse the JSON response; each item in the list is a post.

## Tests

There is a small set of tests that verify the API.

#### Prerequisites

The blog must be running and bound to the hostname `localhost`, or you can adapt the test URL by modifying the `url` variable in `test.py`.

#### Execution

 To execute the tests:

`pipenv run python test.py`

