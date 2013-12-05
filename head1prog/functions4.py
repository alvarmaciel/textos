import urllib.request
import time
def get_price():
    page = urllib.request.urlopen("http://beans-r-us.appspot.com/prices-loyalty.html")
    text = page.read().decode("utf-8")
    position = text.find(">$")
    return float (text[position+2:position+6])

def send_to_twitter(msg):
    import sys
    import tweepy
    CONSUMER_KEY = '...'
    CONSUMER_SECRET = '...'
    ACCESS_KEY = '...'
    ACCESS_SECRET = '...'
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    api.update_status(msg)




precio_ahora = input ("Necesita ver ahora el precio Y/N: ")
if precio_ahora == "Y":
#    print (get_price())
    price = (get_price())
else:
    price = 99.99
    print ("Esperando que el precio sea menor a $ 4.74")
    while price > 4.74:
        time.sleep(20)
        price = get_price()
print ("Comprar a : ", price)
