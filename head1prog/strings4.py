import urllib.request
price = 99.99
while price > 4.74 :
    page = urllib.request.urlopen("http://beans-r-us.appspot.com/prices-loyalty.html")
    text = page.read().decode("utf-8")
    position = text.find(">$")
    price = float (text[position+2:position+6])
print ("¡Comprar!")
