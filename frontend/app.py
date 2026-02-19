from flask import Flask

app = Flask(__name__)

@app.route("/index")
def index():
    return "<p>Contents:</p>"

@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'POST':
        return log_in()
    else:
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

@app.route("/graphs")
def generate_graphs:
    #shows trends based on demographics
    #matplotlibe selection
    




