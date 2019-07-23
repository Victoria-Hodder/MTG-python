from flask import Flask, jsonify, render_template, url_for 
from MTGblog import app

@app.route('/')
def get_homepage():
    return render_template('index.html')

@app.route('/about')
def get_about():
    return render_template('about.html')

@app.route('/blog')
def get_blog():
    return render_template('blog.html')

@app.route('/booklessons')
def get_booklessons():
    return render_template('booklessons.html')

@app.route('/contact')
def get_contact():
    return render_template('contact.html')