from flask import Flask, render_template
import mlab
from mongoengine import *
app = Flask(__name__)

# 1.connect to data base
mlab.connect()

# 2.design collection
class Item(Document):
    title = StringField()
    image = StringField()
    description = StringField()
    price = IntField()
# 3.Try insert an item
old_tv = Item(
    title="Cat set cu va dat ",
    image="https://tinhte.cdnforo.com/store/2015/07/3081243_IMG_0589.jpg",
    description="Cat set cu nen dat",
    price= 3000000
)
old_tv.save()

items = Item.objects()
for item in items:
    print(item.title)
    print(item.price)

# @app.route('/')
# def index():
#     return render_template('index.html', title="TV cũ", image="https://tinhte.cdnforo.com/store/2015/07/3081243_IMG_0589.jpg")
#
# @app.route('/list')
# def title_list():
#     return render_template('title_for.html', titles=['TV cũ', 'Cát sét cũ', 'Người yêu cũ'])
#
# @app.route('/object')
# def object():
#     x = {
#         'title': 'TV cũ giá cao',
#         'image': 'https://tinhte.cdnforo.com/store/2015/07/3081243_IMG_0589.jpg',
#         'description': 'TV vì cũ nên giá cao'
#     }
#     return render_template('object.html', item= x)
@app.route('/object-list')
def object_list():
    # data = [
    #     {
    #         'title': 'TV cũ',
    #         'image': 'http://via.placeholder.com/200x300',
    #         'description': 'TV cũ nên đắt'
    #     },
    #
    #     {
    #         'title': 'cát sét cũ',
    #         'image': 'http://via.placeholder.com/200x300',
    #         'description': 'cát sét cũ nên đắt'
    #     },
    #
    #     {
    #         'title': 'PS1 cũ',
    #         'image': 'http://via.placeholder.com/200x300',
    #         'description': 'PS1 cũ nên đắt'
    #     }
    # ]
    data = Item.objects()
    return render_template('object_list.html', items= data)
if __name__ == '__main__':
  app.run(debug=True)
