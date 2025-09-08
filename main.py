from flask import Flask, render_template, request, redirect, url_for
import classes
import datetime
app = Flask(__name__)

main_db = classes.DB()

@app.route('/')
def home():
    return redirect(url_for('signup'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        f_user = request.form.get('username')
        f_pass = request.form.get('password')
        idx = main_db.find(f_user)
        if idx < 1:
            print("User not found in database. ")
        check_pass = main_db[idx].getPassword()
        if f_pass == check_pass:
            print("User is verified. ")
        else:
            print("User is not verified. Access denied. ")
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
        t_user = classes.User(f_username, f_password)
        main_db.insertVal(t_user)
        print("Accepted")
        return render_template('signup.html')
    else:
        return "<h1>Insertion failed</h1>"

if __name__ == '__main__':
    app.run(debug=True)
