#!/usr/bin/python
import cgi, cgitb
import Cookie
import os
import MySQLdb as db
import requests
import json
import py.auth as auth

form = cgi.FieldStorage()

con = db.connect('localhost', 'hallucinate', 'enlightening news', 'hallucinate')
cur = con.cursor()

# headers

cur.execute("select user_id,hash from users where user_name=%s", (form["username"].value,))
user = cur.fetchall()
if user:
	if auth.check_password(user[0][1], form["password"].value) == True:
		cookie = Cookie.SimpleCookie()
		sid = auth.get_session()
		cookie['sid'] = sid
		cookie['user'] = form["username"].value
		cur.execute("insert into session (session_id,user_id) values (%s,%s)", (sid, user[0][0],));
		con.commit()
		cur.fetchall()
		print(cookie)
		result = {"success": True, "error": ""}
		print("Content-type: text/html\r\n\r\n")
		print(json.dumps(result))
	else:
		result = {"success": False, "error": "login doesn't match our records"}
		print("Content-type: text/html\r\n\r\n")
		print(json.dumps(result))
else:
	result = {"success": False, "error": "login doesn't match our records"}
	print("Content-type: text/html\r\n\r\n")
	print(json.dumps(result))

if cur:
	cur.close()

if con:
	con.close()

