def emit(path):
	with open(path, 'r') as html_file:
		print(html_file.read())

def script(path):
	print('<script src="' + path + '"></script>')

def html():
	print('Content-type: text/html\r\n\r\n')
	print('<!DOCTYPE HTML>')
	print('<html>')

def end_html():
	print('</html>')

def body():
	print('<body>')

def end_body():
	print('</body>')

def head():
	print('<head>')

def end_head():
	print('</head>')

def title(val):
	print('<title>' + val + '</title>')

def css(path):
	print('<link rel="stylesheet" href="' + path + '" type="text/css">')
