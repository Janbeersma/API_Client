import json
import string
from collections import namedtuple


class User:
    fullname = string
    username = string

    def __init__(self, fullname, username):
        self.fullname = fullname
        self.username = username

