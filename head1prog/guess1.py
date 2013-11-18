from random import randint
secret = randint(1, 10)
print ("¡Bienvenidos")
ping=1
while ping == 1:
    g = input ("Adivine el numero: ")
    guess = int (g)
    if guess == secret:
        ping=0
    else:
        if guess > secret:
            print ("Demasiado alto")
        else:
            print ("demasiado bajo")
print ("¡GANASTE!")
