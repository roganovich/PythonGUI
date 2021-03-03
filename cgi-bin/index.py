import  cgi, html
request = cgi.FieldStorage()
value = html.escape(request.getvalue("text", ""))

print("Content-type: text/html; charset=utf-8")
print()
html = '''<!DOCTYPE html>
<html>
<body>
<h1>My First Heading</h1>
<p>My first paragraph.</p>
'''

html += '''
<form method="POST">
<input type="text" name="text" value=""/>
<input type="submit" value="Result"/>
</form>
'''
html += "<h1>" + value + "</h1>"

html += '''
</body>
</html>
'''
print(html)