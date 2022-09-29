from msilib.schema import File
from flask import Flask, render_template, request, redirect,send_file,  flash, abort, url_for
from scrap import app,db,mail
from scrap import app,db,mail
from scrap import app
from scrap.models import *

from flask_login import login_user, current_user, logout_user, login_required
from random import randint
import os
from PIL import Image
from flask_mail import Message
from io import BytesIO
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
# from datetime import datetime as dt
from datetime import datetime,date
# from datetime import timedelta
from werkzeug.utils import secure_filename


from datetime import datetime, timedelta






@app.route('/about',methods=['GET', 'POST'])
def about():
    return render_template("about.html")





@app.route('/contact',methods=['GET', 'POST'])
def contact():
    return render_template("contact.html")



@app.route('/',methods=['GET', 'POST'])
def index():
    return render_template("index.html")




@app.route('/register',methods=['GET', 'POST'])
def register():
    return render_template("register.html")



@app.route('/login',methods=['GET', 'POST'])
def login():
    return render_template("login.html")




