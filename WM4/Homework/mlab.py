import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds133746.mlab.com:33746/topgame

host = "ds133746.mlab.com"
port = 33746
db_name = "topgame"
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
