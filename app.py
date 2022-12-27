import datetime
from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
import os
from werkzeug.utils import secure_filename
import app

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///twitter.db"
db = SQLAlchemy(app)

class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account = db.Column(db.String(140))
    content = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)


@app.route('/')
def homepage():
    with app.app_context():
        db.create_all()
    tweets = Tweet.query.all()
    #Print them to console
    # for tweet in Tweet.query.all():
    #     print(tweet.content)
    print(tweets)
    user = Tweet.query.all()
    return render_template('index.html', tweets=tweets, user=user)

@app.route('/post', methods=['POST'])
def post_tweet():
    account = request.form['account']
    content = request.form['content']
    timestamp = datetime.datetime.utcnow()
    tweet = Tweet(account=account, content=content, timestamp=timestamp)
    db.session.add(tweet)
    db.session.commit()
    print(content)
    return redirect(url_for('homepage'))

@app.route('/clear', methods=['POST'])
def clear_database():
    with app.app_context():
        db.drop_all()
        db.create_all()
    return 'Database cleared and recreated'


@app.route('/profile/<username>')
def profile(username):
    user = Tweet.query.filter_by(username=username).first()
    # code to render the profile page goes here
    print(username)
    return render_template('profile.html', user=user)

if __name__ == '__main__':
    app.run()
