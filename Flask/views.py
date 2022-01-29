from flask import Blueprint, render_template, request, redirect, url_for

views = Blueprint(__name__, 'views')

@views.route('/')
def home():
    return render_template('index.html', int='10')

@views.route('/profile/<int>')
def profile(int):
    return render_template('profile.html', int=int)

@views.route('/query')
def query():
    args = request.args
    int = args.get('int')
    return render_template('index.html', int=int)

@views.route('/links')
def links():
    return render_template('index.html', int='12')

@views.route('/discord')
def discord():
    return redirect(url_for('views.links'))