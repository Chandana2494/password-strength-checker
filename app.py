from flask import Flask, render_template, request
import re

app = Flask(__name__)

def check_password_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score == 3 or score == 4:
        return "Medium"
    else:
        return "Strong"

@app.route("/", methods=["GET", "POST"])
def index():
    strength = None
    password_text = ""
    if request.method == "POST":
        password = request.form["password"]
        password_text = password  # Show what user typed
        strength = check_password_strength(password)
    return render_template("index.html", strength=strength, password_text=password_text)

if __name__ == "__main__":
    app.run(debug=True)
