from flask import Flask, render_template
import mlab
from mongoengine import *
app = Flask(__name__)

# 1.connect mlab
mlab.connect()
# 2. design collection
class Item(Document):
    title= StringField()
    image= StringField()
    description= StringField()

# 3. insert items
# gtaiv = Item(
#     title= "The Witcher 3: Wild Hunt",
#     image= "https://lh3.googleusercontent.com/rOvpaCfSSdyBHEubOe-nogVq8rKCtDBJ6Pwc_gjEfQC7G_rEySLlWN0utL-d5rTX7g=h310",
#     description="Masterpiece!"
# )
# gtaiv.save()

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/object-list')
def object_list():
    data= Item.objects()
    return render_template("object_list.html", items= data)

if __name__ == '__main__':
  app.run(debug=True)
