import urllib.request

page = urllib.request.urlopen("http://beans-r-us.appspot.com")
text = page.read().decode("utf-8")

print (text)
