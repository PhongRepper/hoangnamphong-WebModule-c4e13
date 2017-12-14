from flask import Flask, render_template, request, flash
import mlab
from mongoengine import *
app = Flask(__name__)
app.config['SECRET_KEY'] = 'M_x/rE~qcHu4xj#x'
# 1.connect to data base
mlab.connect()

# 2.design collection
class Item(Document):
    title = StringField()
    image = StringField()
    description = StringField()
    price = IntField()
# # 3.Try insert an item
# new_item = Item(
#     title="DT cu ",
#     image="http://4.bp.blogspot.com/-s5hcGBgKtkc/UQPeBgxJq9I/AAAAAAAAAvw/r8RICpl9GiE/s1600/old+mobile+phone!.jpg",
#     description="DT nen dat",
#     price= 3000000
# )
# new_item.save()

items = Item.objects()
# for item in items:
#     print(item.title)
#     print(item.price)

@app.route('/')
def index():
    items= Item.objects() #get all item in data base
    return render_template('index.html', items= items)

@app.route('/add_item', methods=['GET', 'POST'])
def add_item():
    if request.method == "GET": #get form
        return render_template('add_item.html')
    elif request.method == "POST":
        # 1. Extract data in form
        form = request.form
        title = form['title']
        image = form['image']
        description = form['description']
        price = form['price']
        # 2. Add into data base
        new_item= Item(title= title, image=image,description=description,price=price)
        new_item.save()
        return "ok anh"

@app.route('/admin')
def admin():
    return render_template('admin.html', items=Item.objects())

@app.route('/edit_item/<item_id>', methods=['GET', 'POST'])
def edit_item(item_id):
    item = Item.objects().with_id(item_id)
    if request.method == 'GET':
        return render_template('edit_item.html', item=item)
    elif request.method == 'POST':
        form= request.form
        title= form['title']
        description= form['description']
        image= form['image']
        price= form['price']

        item.update(title=title, description=description,image=image,price=price)
        # must not use save
        flash("Đã sửa thành công ahihi")
        return render_template('edit_item.html', item= Item.objects().with_id(item_id))
    # return render_template('edit_item.html',item=item)


if __name__ == '__main__':
  app.run(debug=True)
