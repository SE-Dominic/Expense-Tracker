from flask import Flask, render_template, request, redirect, url_for
import classes
app = Flask(__name__)

main_db = classes.DB()

@app.route('/')
def home():
    return redirect(url_for('signup'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html')
@app.route ('/to_database', methods=['GET', 'POST'])
def sendToDatabase():
    if request.method == 'POST':
        f_username = request.form.get('username')
        f_password = request.form.get('password')
        t_user = classes.User(f_username, f_password)
        main_db.insertVal(t_user)
        return "Insertion was successful."
    else:
        print("Insertion failed.")
        return render_template('signup.html')



@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
