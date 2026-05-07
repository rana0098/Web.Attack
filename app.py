import random
import hashlib
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask import Flask, request, redirect, url_for, render_template, session
from flask_wtf import CSRFProtect
from flask_wtf.csrf import CSRFError



app = Flask(__name__)
app.secret_key = 'your_secret_key'
csrf = CSRFProtect(app)


app.config.update(
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Strict',  
)
@app.errorhandler(CSRFError)
def handle_csrf_error(e):
    return f"<h3>CSRF Error:</h3><p>{e.description}</p>", 400

# Rate limiting setup
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["5 per minute"]
)

# In-memory user store 
users = {
    "alice@example.com": hashlib.sha256("password123".encode()).hexdigest(),
    "bob@example.com": hashlib.sha256("qwerty".encode()).hexdigest()
}

# ---------------- Login Route ----------------

@app.route('/', methods=['GET', 'POST'])
@limiter.limit("5 per minute")
def login():
    message = ''

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user_captcha = request.form['captcha_answer'].strip()

        # CAPTCHA validation
        if user_captcha != session.get('captcha_answer'):
            message = 'Invalid CAPTCHA.'
        else:
            hashed_pw = hashlib.sha256(password.encode()).hexdigest()
            if email in users and users[email] == hashed_pw:
                session['user'] = email
                return redirect(url_for('dashboard'))
            else:
                message = 'Invalid email or password.'

    # CAPTCHA generation
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    captcha_answer = str(num1 + num2)
    captcha_question = f"What is {num1} + {num2}?"
    session['captcha_answer'] = captcha_answer

    return render_template('login.html', message=message, captcha_question=captcha_question)


# ---------------- Dashboard ----------------
@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', email=session['user'])

# ---------------- Logout ----------------
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

# ---------------- Change Email (CSRF Target) ----------------
@app.route('/change_email', methods=['GET', 'POST'])
def change_email():
    if 'user' not in session:
        return redirect(url_for('login'))

    message = ''
    if request.method == 'POST':
        new_email = request.form['new_email']
        old_email = session['user']

        # Simulate email change in memory
        users[new_email] = users.pop(old_email)
        session['user'] = new_email
        message = f"Email changed to {new_email}"

    return render_template('change_email.html', message=message)


# ---------------- Attacker Page ----------------
@app.route('/attacker')
def attacker():
    return render_template('attacker.html')


# ---------------- Run App ----------------
if __name__ == '__main__':
    app.run(debug=True)
