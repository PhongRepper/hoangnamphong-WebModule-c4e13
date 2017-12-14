from flask import Flask, render_template, request, flash
import mlab
from mongoengine import *
from flask import Flask, render_template
app = Flask(__name__)
app.config['SECRET_KEY'] = 'M_x/rE~qcHu4xj#x'

mlab.connect()

class Item(Document):
    title = StringField()
    image = StringField()
    description = StringField()
    price = IntField()
# new_game= Item(
#     title= "Counter-Strike: Global Offensive",
#     image= "http://on-winning.com/wp-content/uploads/2015/11/steamworkshop_webupload_previewfile_271277161_preview.jpg",
#     description= "Plant bomb-Defuse. Defend-Rescue",
#     price="160000"
# )
# new_game.save()

items = Item.objects()

@app.route('/')
def index():
    items= Item.objects() #get all item in data base
    return render_template('index.html', items= items)

@app.route('/add_item', methods=['GET', 'POST'])
def add_item():
    if request.method== 'GET':
        return render_template('add_item.html')
    elif request.method== 'POST':
        form = request.form
        title = form['title']
        image = form['image']
        description = form['description']
        price = form['price']

        new_game= Item(title=title, image=image, description=description, price=price)
        new_game.save()
        return render_template('sc.html')
        # return 'ok anh'

@app.route('/admin')
def admin():
    return render_template('admin.html',items = Item.objects())

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
        flash("Changing completed!")
        return render_template('edit_item.html', item= Item.objects().with_id(item_id))

@app.route('/delete_item/<item_id>', methods = ['GET', 'POST'])
def delete_item(item_id):
    item = Item.objects().with_id(item_id)
    if request.method == 'GET':
        return render_template('delete_item.html', item=item)
    elif request.method == 'POST':
        item.delete()
        return render_template('post_delete.html')




if __name__ == '__main__':
  app.run(debug=True)
