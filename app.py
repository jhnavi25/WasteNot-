from flask import Flask, render_template, request, redirect
import json
from datetime import datetime
import matplotlib.pyplot as plt
import os

app = Flask(__name__)
logged_in = False  # track login status

# ✅ MAIN ENTRY POINT: Redirect to register page
@app.route('/')
def main_entry():
    return render_template('home.html')  # ✅ This loads the new homepage


# ✅ REGISTER PAGE
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Save to users.json
        user = {'username': username, 'password': password}

        try:
            with open('users.json', 'r') as f:
                users = json.load(f)
        except FileNotFoundError:
            users = []

        # Check if username already exists
        for u in users:
            if u['username'] == username:
                return render_template('register.html', error="Username already exists")

        users.append(user)

        with open('users.json', 'w') as f:
            json.dump(users, f, indent=4)

        return redirect('/login')

    return render_template('register.html')

# ✅ LOGIN PAGE
@app.route('/login', methods=['GET', 'POST'])
def login():
    global logged_in

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        try:
            with open('users.json', 'r') as f:
                users = json.load(f)
        except FileNotFoundError:
            users = []

        for user in users:
            if user['username'] == username and user['password'] == password:
                logged_in = True
                return redirect('/dashboard')  # we’ll treat /dashboard as app home after login


        return render_template('login.html', error="Invalid username or password.")

    return render_template('login.html')



# ✅ ASK HOW MANY ITEMS
@app.route('/entry-count', methods=['GET', 'POST'])
def entry_count():
    if request.method == 'POST':
        count = request.form['count']
        return redirect(f'/add-multiple/{count}')
    return render_template('entry-count.html')

@app.route('/add-multiple/<int:count>', methods=['GET', 'POST'])
def add_multiple(count):
    if request.method == 'POST':
        items = []

        for i in range(count):
            name = request.form.get(f'name_{i}')
            expiry = request.form.get(f'expiry_{i}')
            items.append({'name': name, 'expiry': expiry})

        try:
            with open('data.json', 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []

        data.extend(items)

        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)

        return redirect('/items')  # Or redirect to one-page summary if you want

    return render_template('add-multiple.html', count=count)


# ✅ ADD ONE ITEM (OLD INDIVIDUAL ROUTE)
@app.route('/add', methods=['POST'])
def add_item():
    name = request.form['name']
    expiry = request.form['expiry']

    item = {'name': name, 'expiry': expiry}

    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    data.append(item)

    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)

    return redirect('/')

# ✅ VIEW ALL ITEMS
@app.route('/items')
def view_items():
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    return render_template('list.html', items=data)

# ✅ DASHBOARD route must be here BEFORE app.run
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST':
        return redirect('/entry-count')  # or handle logic here
    return render_template('entry-count.html')


# ✅ RUN FLASK APP (should always be last)
if __name__ == '__main__':
    app.run(debug=True)
