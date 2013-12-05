import urllib.request
import time
def get_price():
    page = urllib.request.urlopen("http://beans-r-us.appspot.com/prices-loyalty.html")
    text = page.read().decode("utf-8")
    position = text.find(">$")
    return float (text[position+2:position+6])

def send_to_twitter(msg):
    password_manager = urllib.request.HTTPPasswordMgr()
	password_manager.add_password("Twitter API",
	"http://twitter.com/statuses", "...", "...")
	http_handler = urllib.request.HTTPBasicAuthHandler(password_manager)
	page_opener = urllib.request.build_opener(http_handler)
	urllib.request.install_opener(page_opener)
	params = urllib.parse.urlencode( {'status': msg} )
	resp = urllib.request.urlopen("http://twitter.com/statuses/update.json", params)
	resp.read()


precio_ahora = input ("Necesita ver ahora el precio Y/N: ")
if precio_ahora == "Y":
#    print (get_price())
#    price = (get_price())
    send_to_twitter (get_price())
else:
    price = 99.99
    print ("Esperando que el precio sea menor a $ 4.74")
    while price > 4.74:
        time.sleep(20)
        price = get_price()
#print ("Comprar a : ", price)
send_to_twitter(get_price())
