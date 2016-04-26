#!/usr/bin/python
import cgi, cgitb
import Cookie
import os
import MySQLdb as db
import requests
import json
import py.auth as auth

form = cgi.FieldStorage()
cookie = Cookie.SimpleCookie()
cookie_string = os.environ.get('HTTP_COOKIE')
if cookie_string:
	cookie.load(cookie_string)

	con = db.connect('localhost', 'hallucinate', 'enlightening news', 'hallucinate')
	cur = con.cursor()

	cur.execute("delete from session where session_id=%s", (cookie['sid'].value,))
	con.commit()
	cur.fetchall()
	cookie['sid'] = ''
	cookie['user'] = ''
	cookie['sid']['expires'] = 'Thu, 01 Jan 1970 00:00:00 GMT'
	cookie['user']['expires'] = 'Thu, 01 Jan 1970 00:00:00 GMT'
	print(cookie)
	result = {"success": True, "error": ""}
	print("Content-type: text/html\r\n\r\n")
	print(json.dumps(result))

	if cur:
		cur.close()

	if con:
		con.close()
else:
	result = {"success": False, "error": "user not logged in"}
	print("Content-type: text/html\r\n\r\n")
	print(json.dumps(result))

