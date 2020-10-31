from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/blog')
def hey():
    return 'would you like some tea'
@app.route('/blog/dogs/pets')
def hi():
    return 'or some coffee perhaps'

