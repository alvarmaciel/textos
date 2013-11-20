import urllib.request

page = urllib.request.urlopen("http://beans-r-us.biz/prices.html")
text = page.read().decode("utf-8")

print (text)
