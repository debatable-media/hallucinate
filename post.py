#!/usr/bin/python
import cgi, cgitb
import Cookie
import os
import MySQLdb as db
import requests
import json
import py.auth as auth
import bleach 

form = cgi.FieldStorage()
cookie = Cookie.SimpleCookie()
cookie_string = os.environ.get('HTTP_COOKIE')
if cookie_string:
	cookie.load(cookie_string)

con = db.connect('localhost', 'hallucinate', 'enlightening news', 'hallucinate')
cur = con.cursor()

# headers

if 'sid' in cookie:
	cur.execute("select user_id from session where session_id=%s", (cookie['sid'].value,))
	users = cur.fetchall()
	if users:
		cur.execute("insert into posts (user_id, content) values (%s,%s)", (users[0][0],bleach.clean(form['content'].value),))
		con.commit()
		cur.fetchall()
		result = {"success": True, "error": ""}
		print("Content-type: text/html\r\n\r\n")
		print(json.dumps(result))
	else:
		result = {"success": False, "error": "invalid session"}
		print("Content-type: text/html\r\n\r\n")
		print(json.dumps(result))
else:
	result = {"success": False, "error": "you must be logged in"}
	print("Content-type: text/html\r\n\r\n")
	print(json.dumps(result))

if cur:
	cur.close()

if con:
	con.close()

