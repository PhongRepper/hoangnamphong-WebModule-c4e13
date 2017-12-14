import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds135486.mlab.com:35486/gamestore

host = "ds135486.mlab.com"
port = 35486
db_name = "gamestore"
user_name = "phong"
password = "phong"

def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
