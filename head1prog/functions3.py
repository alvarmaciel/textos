import urllib.request
import time
def get_price():
    page = urllib.request.urlopen("http://beans-r-us.appspot.com/prices-loyalty.html")
    text = page.read().decode("utf-8")
    position = text.find(">$")
    price = float (text[position+2:position+6])
    return (price)

answer = "Y"

while answer != "N":
    answer = input ("Necesita comprar ahora Y/N: ")
    if answer != "N":
        price = get_price()
        print (price)
        answer = "Y"
    else:
        price= float (get_price())
        if price < 4.74:
            print (price)
    print ("Esperando 20 segundos para buscar precios...")
    time.sleep(20)
    answer = input ("Quiere terminar el programa Y/N: ")
