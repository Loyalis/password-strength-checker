# 🛡️ Password Strength Checker

A web app built with Flask that analyzes password strength, explains vulnerabilities, and encourages secure habits—all developed as part of my self-taught journey into cybersecurity.

---

## 👨‍💻 About Me

I'm **Casu Laurențiu Gabriel**, a Technical Support Engineer and Cybersecurity Enthusiast based in Romania.  
This project reflects my desire to go beyond theory, break things, explore code, and truly understand how secure systems are built. Everything here—from routing and entropy to password hashing—was learned, tested, and implemented with purpose.

---

## 🔍 Features

- ✅ Checks password structure (length, uppercase, lowercase, digits, symbols)
- ✅ Flags personal patterns like names (e.g. “gabriel”)
- ✅ Compares against leaked passwords in `rockyou.txt` (if provided)
- ✅ Calculates entropy score
- ✅ Displays strength: Weak, Medium, Strong
- ✅ Hashes strong passwords with Werkzeug and stores them securely in SQLite
- ✅ Built with Python, Flask, Bootstrap 5, and some caffeine

---

## 🚀 Quickstart

```bash
git clone https://github.com/Loyalis/password-strength-checker.git
cd password-strength-checker
python -m venv venv
venv\Scripts\activate       # On Windows
pip install -r requirements.txt

> Before running, set your secret key:

bash
set SECRET_KEY=your-secret-key
Then start the app:

bash
python app.py
Visit: http://localhost:5000

📂 Project Layout
password-strength-checker/
├── app.py                 # Flask app logic and routing
├── requirements.txt       # Dependencies
├── .gitignore             # Sensitive or unnecessary files
├── README.md              # This file
├── templates/             # index.html and about.html
└── static/                # Optional for future CSS or JS
> passwords.db is auto-generated, and .env / rockyou.txt should be excluded from Git.

🧠 What I Learned
This project helped me explore:

Password validation & entropy math

Regular expressions

Secure storage using hashing

Flask routes, forms, and rendering

Real-world cybersecurity habits

How to structure and polish a public GitHub project

🌱 Still Improving
[ ] Add visual strength meter and dynamic tips

[ ] Add unit tests for route validation

[ ] Improve UI styling and accessibility

[ ] Rate-limiting and cooldowns for abuse prevention

[ ] Docker support

[ ] Host it live (Render or Railway)

👨‍🎓 Also working on:

Building a personal cybersecurity portfolio site to showcase:


My journey, skills, projects, and labs

Creating an interactive learning platform:

Choose a tool (e.g. Metasploit), get quizzes, tips, and real-world questions

Learn cybersecurity by doing, not memorizing

🛡️ Disclaimer
This tool is for educational purposes only. Please do not enter real passwords—only test examples.

📜 License
MIT License — Free to use, share, and learn from.

🙌 Thanks
To every guide, repo, blog, and forum post that taught me something new—I’m building because I’m learning. And learning by building. This is just the start.

