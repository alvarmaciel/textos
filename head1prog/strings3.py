import urllib.request

page = urllib.request.urlopen("http://beans-r-us.appspot.com/prices-loyalty.html")
text = page.read().decode("utf-8")

price = text[234:238]

print (text)
