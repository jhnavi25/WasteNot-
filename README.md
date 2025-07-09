# 🌱 WasteNot – A Smart Food Tracker

**WasteNot** is a beginner-friendly, sustainability-focused web application designed to help users track their food inventory and reduce food waste. It allows users to register, add food items with expiry dates, and monitor their saved vs. wasted food behavior.

---

## 📌 Features

- 👤 User Registration & Login
- 🍽️ Add multiple food items at once
- 🕒 Track expiry dates in real-time
- 📋 View all saved items in a structured table
- 🌐 Language dropdown for inclusive design
- 🎥 Homepage with fullscreen background video
- 🧾 Simple, beautiful UI with clean layout
- 🔐 Session-based login using Flask

---

## 🚀 Tech Stack

- **Frontend**: HTML, CSS (custom)
- **Backend**: Python (Flask)
- **Storage**: JSON (local)
- **Visualization**: *(Optional)* Matplotlib
- **Deployment**: Localhost (Flask server)

---

## 📷 Screenshots

> *(Optional: Add screenshots to `/static/` folder and update these paths)*

| Homepage | Add Items Page |
|----------|----------------|
| ![Home](static/screenshot-home.png) | ![Add](static/screenshot-add.png) |

---

## 🛠️ How to Run

```bash
# Clone the repository
git clone https://github.com/jhnavi25/WasteNot.git
cd WasteNot

# Install dependencies
pip install flask matplotlib

# Run the app
python app.py

# Open in browser
http://127.0.0.1:5000/
```

---

## 📁 Folder Structure

```
WasteNot/
│
├── static/
│   ├── style.css
│   ├── homevedio.mp4
│   └── (screenshots)
│
├── templates/
│   ├── home.html
│   ├── login.html
│   ├── register.html
│   ├── entry-count.html
│   ├── add-multiple.html
│   └── list.html
│
├── app.py
├── data.json
└── users.json
```

---

## 🎯 Inspiration

Food waste is a global problem. With **WasteNot**, even a small personal step toward tracking perishables can reduce waste and promote sustainability 🌍

---

## 🙋 Author

**Jhnavi Bhadkariya**  
💻 1st Year CSE Student  
📍 Madhav Institute of Technology & Science, Gwalior  
📫 [GitHub](https://github.com/jhnavi25)

---

## 📜 License

MIT License – feel free to use, learn from, or extend this project!
