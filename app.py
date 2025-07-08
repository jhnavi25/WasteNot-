from flask import Flask, render_template, request, redirect
import json
from datetime import datetime
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

# Home page with form
@app.route('/')
def index():
    return render_template('index.html')

# Add item to data.json
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

# View all items
@app.route('/items')
def view_items():
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    return render_template('list.html', items=data)

# Pie chart: Saved vs Wasted (Real Logic)
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

# Run app
if __name__ == '__main__':
    app.run(debug=True)
