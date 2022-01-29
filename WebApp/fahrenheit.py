from flask import Blueprint, render_template, request, redirect, url_for

fahrenheit = Blueprint(__name__, 'fahrenheit')

@fahrenheit.route('/')
def form():
    return render_template('form_fahrenheit.html')

@fahrenheit.route('/', methods=['POST'])
def form_post():
    fahrenheit = int(request.form['Fahrenheit'])
    return convert(fahrenheit)
    #return render_template('celsius.html', input=fahrenheit, output=celsius)

@fahrenheit.route('/<int:fahrenheit>')
def convert(fahrenheit):
    celsius = ((fahrenheit - 32) * 5) // 9
    return render_template('celsius.html', input=fahrenheit, output=celsius)