import os
import re
import sqlite3
from math import log2
from flask import Flask, render_template, request, redirect, flash
from werkzeug.security import generate_password_hash
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "super-secret")  # Make sure to set this in your system or host

# Load leaked passwords from rockyou.txt (user should download manually)
def load_common_passwords(path="rockyou.txt"):
    if not os.path.exists(path):
        return set()
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return set(line.strip() for line in f)

common_passwords = load_common_passwords()

# Initialize database (if it doesn’t exist)
def init_db():
    conn = sqlite3.connect("passwords.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            password TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

init_db()

def calculate_entropy(password):
    charset = 0
    if re.search(r"[a-z]", password): charset += 26
    if re.search(r"[A-Z]", password): charset += 26
    if re.search(r"\d", password): charset += 10
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password): charset += 32
    return round(len(password) * log2(charset), 2) if charset else 0

def check_strength(password):
    names = ["gabriel", "laurentiu", "john", "sarah"]
    p = password.lower()

    if password in common_passwords:
        return "Weak", "This password is found in leaked databases.", None

    if any(name in p for name in names):
        return "Weak", "Avoid using names in passwords.", None

    criteria = {
        "length": len(password) >= 8,
        "uppercase": bool(re.search(r"[A-Z]", password)),
        "lowercase": bool(re.search(r"[a-z]", password)),
        "digit": bool(re.search(r"\d", password)),
        "special": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    }

    score = sum(criteria.values())
    if score == 5:
        return "Strong", "Excellent password!", criteria
    elif 3 <= score < 5:
        return "Medium", "Password could be stronger.", criteria
    else:
        return "Weak", "Password is too simple.", criteria

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        password = request.form.get("password")
        if not password:
            flash("Please enter a password.", "warning")
            return redirect("/")

        strength, message, criteria = check_strength(password)
        entropy = calculate_entropy(password)

        if strength == "Strong":
            hashed = generate_password_hash(password)
            conn = sqlite3.connect("passwords.db")
            conn.execute("INSERT INTO passwords (password) VALUES (?)", (hashed,))
            conn.commit()
            conn.close()
            flash("Strong password saved (hashed).", "success")

        result = {
            "message": message,
            "strength": strength,
            "criteria": criteria,
            "entropy": entropy
        }

    return render_template("index.html", result=result, current_year=datetime.now().year)

@app.route("/about")
def about():
    return render_template("about.html", current_year=datetime.now().year)

if __name__ == "__main__":
    app.run(debug=True)
