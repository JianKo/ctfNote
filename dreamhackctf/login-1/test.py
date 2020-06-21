#!/usr/bin/python3
from flask import *
import sqlite3
import hashlib
import os
import time, random

app = Flask(__name__)
app.secret_key = os.urandom(32)

DATABASE = "database.db"

userLevel = {
    0: 'guest',
    1: 'admin'
}
MAXRESETCOUNT = 5

@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'GET':
        pass
    else:
        userid = request.form.get("userid")
        newpassword = request.form.get("newpassword")
        backupCode = request.form.get("backupCode", type=int)
    print(userid)
    print(newpassword)
    print(backupCode)

app.run(host='0.0.0.0', port=8000)
