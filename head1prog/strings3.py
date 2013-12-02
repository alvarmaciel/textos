import urllib.request

page = urllib.request.urlopen("http://beans-r-us.appspot.com/prices-loyalty.html")
text = page.read().decode("utf-8")

position = text.find(">$")
price = text[position+1:position+4]

print (price)
