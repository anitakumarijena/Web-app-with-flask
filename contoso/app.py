from flask import Flask, render_template

app = Flask(__name__)
@app.route('/', methods=['GET'])     # By using @app.route, we indicate the route we want to createThe path will be /, which is the default route. We indicate this will be used for GET. If a GET request comes in for /, Flask will automatically call the function declared immediately below the decorator, index in our case. In the body of index, we indicate that we'll return an HTML template named index.html to the user.
def index():
    return render_template('index.html')