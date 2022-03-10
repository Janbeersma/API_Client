import json
from collections import  namedtuple

class JsonToObject:
    # def customUserDecoder(self, data):
    #     return namedtuple(str, data.keys())(*data.values())

    def DeserializeUserFromJson(self, data):
        user = json.loads(data, object_hook =
                lambda d : namedtuple('X', d.keys())(*d.values()))
        json.dumps(user)
        return user