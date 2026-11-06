from flask import Flask, request, render_template, redirect, url_for, session
from backend import users
import os
import sqlite3
from services.analysis import expected_num_cycles, summary_success_all
from services.analysis import bootstrap_linear, clean_all

app = Flask(__name__)
database = os.path.join(os.path.dirname(__file__), 'database.db')

def init_db():
    conn = sqlite3.connect(database)
    c = conn.cursor()

    c.execute(''' 
                CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
                )'''
                )
        
    c.execute("INSERT OR IGNORE INTO users (username, password) VALUES (?,?)", ('test','1234'))
    c.execute('''
                CREATE TABLE IF NOT EXISTS user_data(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                result REAL NOT NULL,
                description TEXT NOT NULL,
                location TEXT NOT NULL,
                type TEXT NOT NULL,
                breakout TEXT NOT NULL
                )'''
                )
    conn.commit()
    conn.close()
    print("Database Initialized.")
    

@app.route("/index")
def index():
    return "<p>Contents:</p>"

@app.route("/", methods=['GET','POST'])
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

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    username = None
    result = None
    description = None
    type_ = None
    location = None
    breakout = None
    if request.method == "POST":
        action = request.form.get("action")
        if action == "save":
            username = session.get('user')

            if not username:
                return redirect(url_for('login'))
            
            result = request.form.get("result")
            description = request.form.get("description")
            type_ = request.form.get("type")
            location = request.form.get("location")
            breakout = request.form.get("breakout")
            
            result = float(result) 
            
            conn = sqlite3.connect(database)
            c = conn.cursor()
            c.execute("INSERT INTO user_data (username, result, description, location, type, breakout) VALUES (?,?,?,?,?,?)", (username, result, description, location, type_, breakout))
            conn.commit()
            conn.close()
            
            return render_template("dashboard.html", message="Data saved successfully!", result=result, description=description, location=location, type=type_, breakout=breakout)
        elif action == "submit":
            
            state = request.form.get("State")
            attribute = request.form.get("Patient type")
            breakout = request.form.get("Breakout")
            user_input = {"LocationAbbr":state, "Type":attribute, "Breakout":breakout}

            result_dict = bootstrap_linear(clean_all, user_input)

            location = user_input["LocationAbbr"]
            type_ = user_input["Type"]
            breakout = user_input["Breakout"]
            result = result_dict["expected_success_rate"]
            description = result_dict

    return render_template("dashboard.html", result=result, description=description, location=location, type=type_, breakout=breakout)
    

def log_in_form():
    return render_template("login.html")

def log_in():
    username = request.form.get('username')
    password = request.form.get('password')

    user = users.read(database, username)

    if user and user[2] == password:
        session['user'] = username
        return redirect(url_for('dashboard'))
    else:
        return "Invalid Credentials", 401
    
if __name__ == "__main__":
    init_db()
    app.secret_key = "devkey"
    app.run(debug=True)


