from flask import Flask, render_template
from celsius import celsius
from fahrenheit import fahrenheit

app = Flask(__name__)
app.register_blueprint(celsius, url_prefix='/celsius')
app.register_blueprint(fahrenheit, url_prefix='/fahrenheit')

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)