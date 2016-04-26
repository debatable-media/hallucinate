#!/usr/bin/python
import cgi, cgitb
import Cookie
import os
import MySQLdb as db
import py.html as html
import py.login_links as login_links

#form = cgi.FieldStorage()
cookie = Cookie.SimpleCookie()
cookie_string = os.environ.get('HTTP_COOKIE')
if cookie_string:
	cookie.load(cookie_string)

con = db.connect('localhost', 'hallucinate', 'enlightening news', 'hallucinate')
cur = con.cursor()

html.html()

user = ""
session = ""
if 'user' in cookie:
	user = cookie['user'].value
if 'sid' in cookie:
	session = cookie['sid'].value

html.head()
html.title('Hallucinate')
html.emit('html/meta.html')
html.css('css/style.css')
html.css('css/nav.css')
html.css('css/banner.css')
html.css('css/login.css')
html.css('css/posts.css')
html.css('https://fonts.googleapis.com/css?family=Roboto:400,100,300,700,500,900')
login_links.emit(user)
html.script('https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js')
html.script('https://www.google.com/recaptcha/api.js')
html.end_head()

html.body()
html.emit('html/banner.html')

print("<div id=\"main\">\n")

html.emit('html/post.html')

cur.execute("select content from posts")
results = cur.fetchall()
first = True
if results:
	for result in results:
		if not first:
			print('<hr />')
		else:
			first = False
		print(result[0])
else:
	print('<center><font size=18px>I don\'t know where the links went! I swear!</font><br><img src="images/kitten.jpg"></center>');

print("</div>\n")

html.emit('html/login.html')
html.script('js/load.js')
html.script('js/login.js')
html.script('js/post.js')
html.end_body()
html.end_html()

if cur:
	cur.close()

if con:
	con.close()

