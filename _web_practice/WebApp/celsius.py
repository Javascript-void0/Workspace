from flask import Blueprint, render_template, request, redirect, url_for

celsius = Blueprint(__name__, 'celsius')

@celsius.route('/')
def form():
    return render_template('form_celsius.html')

@celsius.route('/', methods=['POST'])
def form_post():
    celsius = int(request.form['Celsius'])
    return convert(celsius)
    #return render_template('fahrenheit.html', input=celsius, output=fahrenheit)


@celsius.route('/<int:celsius>')
def convert(celsius):
    fahrenheit = ((celsius * 9) // 5 ) + 32
    return render_template('fahrenheit.html', input=celsius, output=fahrenheit)