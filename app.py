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
    return redirect('/register')

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
                return redirect('/entry-count')

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

# ✅ PIE CHART – SAVED vs WASTED
@app.route('/chart')
def chart():
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    saved = 0
    wasted = 0

    for item in data:
        expiry_str = item.get('expiry')
        try:
            expiry_date = datetime.strptime(expiry_str, '%Y-%m-%d').date()
            if expiry_date < datetime.now().date():
                wasted += 1
            else:
                saved += 1
        except:
            saved += 1  # if invalid date, count as saved

    labels = ['Saved', 'Wasted']
    sizes = [saved, wasted]
    colors = ['#4CAF50', '#F44336']

    plt.figure(figsize=(5, 5))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
    plt.title('Saved vs Wasted Food (Real Time)')

    chart_path = os.path.join('static', 'chart.png')
    plt.savefig(chart_path)
    plt.close()

    return render_template('chart.html')

# ✅ RUN FLASK APP
if __name__ == '__main__':
    app.run(debug=True)
