import os
import Tkinter
import tkMessageBox
from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient

app = Flask(__name__)



client = MongoClient(
    os.environ['TODO_DB_1_PORT_27017_TCP_ADDR'],
    27017)
db = client.tododb


@app.route('/')
def todo():

    _items = db.tododb.find()
    items = [item for item in _items]

    return render_template('todo.html', items=items)



@app.route('/new', methods=['POST'])
def new():
    valor1= request.form['producto']
    valor2= request.form['precio']
    valor3= request.form['descripcion']
    valor4= request.form['categoria']
    item_doc = {
        'producto': request.form['producto'],
        'precio': request.form['precio'],
        'descripcion':request.form['descripcion'],
        'categoria': request.form['categoria']
    }

    if not valor1:
        print("no hay data de producto")
        return redirect('/')

    elif not valor2:
        print("no hay data de precio")
        return redirect('/')
        
    else:
        print("se registro correctamente")
        db.tododb.insert_one(item_doc)
        return redirect(url_for('todo'))
       
 

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
