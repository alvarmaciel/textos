import urllib.request
import time
def get_price():
    page = urllib.request.urlopen("http://beans-r-us.appspot.com/prices-loyalty.html")
    text = page.read().decode("utf-8")
    position = text.find(">$")
    price = float (text[position+2:position+6])
    return (price)

answer = input ("Necesita comprar ahora Y/N: ")

while answer != "N":
    price = get_price()
    print (price)
else:
    time.sleep(20)
    price = get_price()
    print ("¡Comprar!")
