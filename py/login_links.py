def emit(user):
	print('<style>')
	if len(user) != 0:
		print('nav > ul > li#nav-login\n{\n\tdisplay: none;\n}')
	else:
		print('nav > ul > li#nav-logout\n{\n\tdisplay: none;\n}')
		print('nav > ul > li#nav-account\n{\n\tdisplay: none;\n}')
		print('#post-form\n{\n\tdisplay: none;\n}')
	print('</style>')

