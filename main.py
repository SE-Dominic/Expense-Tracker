from flask import Flask, render_template, request, redirect, url_for
import classes, sqlite3
app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('signup'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        f_user = request.form.get('username')
        f_pass = request.form.get('password')
    return render_template('login.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/add_expense', methods=['GET', 'POST'])
def add_expense():
    return render_template('add_expense.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        f_username = request.form.get('username')
        f_password = request.form.get('password')
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)
