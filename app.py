# Hackathon project – WasteNot

from flask import Flask, render_template, request, redirect
import json
from datetime import datetime

app = Flask(__name__)

# Home Page (shows the form)
@app.route('/')
def index():
    return render_template('index.html')

# Add item from form
@app.route('/add', methods=['POST'])
def add_item():
    name = request.form['name']
    expiry = request.form['expiry']

    item = {
        'name': name,
        'expiry': expiry
    }
@app.route('/items')
def view_items():
    try:
        with open('data.json','r') as f:
            data=json.load(f)
    except FileNotFoundError:
        data=[]
    return render_template('list.html',items=data)
    # Load existing data
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    data.append(item)

    # Save updated data
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)

    return redirect('/')
if __name__ == '__main__':
    app.run(debug=True)
