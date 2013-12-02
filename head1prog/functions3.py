import urllib.request
import time
def get_price():
    page = urllib.request.urlopen("http://beans-r-us.appspot.com/prices-loyalty.html")
    text = page.read().decode("utf-8")
    position = text.find(">$")
    return float (text[position+2:position+6])

precio_ahora = input ("Necesita ver ahora el precio Y/N: ")
if precio_ahora == "Y":
    print (get_price())
else:
    price = 99.99
    while price > 4.74:
        time.sleep(20)
        price = get_price()
print ("Comprar a : ", price)