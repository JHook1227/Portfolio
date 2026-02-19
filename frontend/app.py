from flask import Flask, request, render_template, redirect, url_for, session
from backend import users
import os
import sqlite3

app = Flask(__name__)
database = os.path.join(os.path.dirname(__file__), 'database.db')

def init_db():
    if not os.path.exists(database):
        conn = sqlite3.connect(database)
        c = conn.cursor()

        c.execute(''' 
                  CREATE TABLE users(
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  username TEXT NOT NULL UNIQUE,
                  password TEXT NOT NULL
                  )'''
                  )
        
        c.execute("INSERT INTO users (username, password) VALUES (?,?)", ('test','1234'))
        conn.commit()
        conn.close()
        print("Database Initialized.")
    else:
        print("Database exists already")

@app.route("/index")
def index():
    return "<p>Contents:</p>"

@app.route("/login", methods=['GET','POST'])
def login():
    print("Login route hit")
    print("Request method:", request.method)
    if request.method == 'POST':
        print("Post detected")    
        return log_in()
    else:
        print("Get detected")
        return log_in_form()
    
@app.route("/informational")
def display_info():
    # general information on findings
    return (render_template)

@app.route("/calculator")
def compute_demos():
    #application itself
    #zip code
    #api to search state based on zipcode?
    #if zipcode in an province, range of values like 641--- need to group zip codes together and if not there closest available
    #attribute drop down for selection
    #button to click for computation -- returns expected number of cycles -- expected cost
    return("computation")

@app.route("/graphs")
def generate_graphs():
    #shows trends based on demographics
    #matplotlibe selection
    return("graphs")
    

def log_in_form():
    return render_template("login.html")

def log_in():
    username = request.form.get('username')
    password = request.form.get('password')

    user = users.read(database, username)

    if user and user[2] == password:
        session['user'] = username
        return redirect(url_for('index'))
    else:
        return "Invalid Credentials", 401
    
if __name__ == "__main__":
    init_db()
    app.secret_key = "devkey"
    app.run(debug=True)


