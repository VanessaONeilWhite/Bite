from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html.j2')
     #return "<h1>Bite</h1>"

@app.route('/login', methods = ['GET', 'POST'])
def login():
    return render_template('login.html.j2')

@app.route('/logout', methods = [])
def logout():
    return render_template('logout.html.j2')

@app.route('/register', methods = [])
def register():
    return render_template('register.html.j2')

@app.route('/my_bites', methods=[])
def my_bites():
    return render_template('my_bites.html.j2')

@app.route('/bite', methods =['GET', 'POST'])
def bite():
    if request.method =='POST':
        zip = request.form.get('zip')
        restaurant = request.form.get('restaurant')

        ## this is where we need to put in the url for the api with the requests.
        ##may need to install requests
        ## may need to pip install requests 
    return render_template('bite.html.j2')