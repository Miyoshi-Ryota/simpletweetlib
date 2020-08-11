# simple tweet library
A quite simple and easy to use twitter library.

# How To Install
```
pip install simpletweetlib
```

# How To Use
## Sample Code
```python
from simpletweetlib.tweet import Tweet
consumer_key = "foobar"
consumer_secret = "foobar"
access_token = "foobar"
access_token_secret = "foobar"

t = Tweet(consumer_key, consumer_secret, access_token, access_token_secret)
t.tweet("Hello World!")
```

## What is consumer_key, consumer_secret, access_token_secret and access_token?
* Following the [twitter document](https://developer.twitter.com/en/account/get-started).
* Creating an app in the website.
* Getting 4 keys in `Keys and Token` pages of the website.
* Replacing "foobar" in sample code to the keys.
