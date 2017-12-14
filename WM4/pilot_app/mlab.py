import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds119151.mlab.com:19151/oldstuff

host = "ds119151.mlab.com"
port = 19151
db_name = "oldstuff"
user_name = "phong1002"
password = "1002"
# Authentication failed: lỗi bảo mật


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
