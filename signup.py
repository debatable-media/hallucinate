#!/usr/bin/python
import cgi, cgitb
import Cookie
import os
import MySQLdb as db
import requests
import json
import py.auth as auth

form = cgi.FieldStorage()
#cookie = Cookie.SimpleCookie()

con = db.connect('localhost', 'hallucinate', 'enlightening news', 'hallucinate')
cur = con.cursor()

# headers

response = requests.post('https://www.google.com/recaptcha/api/siteverify', params={'secret': '6Lcuox0TAAAAAGAp-yoM2vAXJYWgXHRv6riTTSF3', 'response': form['g-recaptcha-response'].value}).json()

user = form["username"].value
if response["success"] == True:
	cur.execute("select user_name from users where user_name=%s", (user,))
	if cur.fetchall():
		result = {"success": False, "error": "username already claimed"}
		print("Content-type: text/html\r\n\r\n")
		print(json.dumps(result))
	else:
		pw = auth.hash_password(form["password"].value)
		cur.execute("insert into users (user_name, hash) values (%s,%s)", (user, pw,));
		con.commit()
		cur.fetchall()
		cur.execute("select user_id from users where user_name=%s", (user,))
		uid = cur.fetchall()[0][0];
		result = {"success": True, "error": ""}
		cookie = Cookie.SimpleCookie()
		sid = auth.get_session()
		cookie['sid'] = sid
		cookie['user'] = user
		cur.execute("insert into session (session_id,user_id) values (%s,%s)", (sid, uid,));
		con.commit()
		cur.fetchall()
		print(cookie)
		print("Content-type: text/html\r\n\r\n")
		print(json.dumps(result))
else:
	result = {"success": False, "error": "you seem to be a robot"}
	print("Content-type: text/html\r\n\r\n")
	print(json.dumps(result))

if cur:
	cur.close()

if con:
	con.close()

