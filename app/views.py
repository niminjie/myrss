from flask import render_template, flash, redirect, session, url_for, request, g
from app import app
from db import *
import os
from models import Feed

@app.route('/')
@app.route('/index')
def index():
    db = DBControler("./feed.db") 
    # db = DBControler("/Users/niminjie/Documents/workspace/webSite/RSSReader/feed.db") 
    feeds = db.query("feeds")
    print feeds[0].keys()
    return render_template('index.html', feeds=feeds)
