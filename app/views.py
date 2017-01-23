from flask import render_template
from flask import request
from app import app

@app.route('/')
@app.route('/index')
def index():
    #user = {'twitter_handle': 'Mike'}
    user = ""
    return render_template('index.html', title='Home', user=user)
    