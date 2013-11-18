from random import randint
secret = randint(1, 10)
guess = 0
print ("¡Bienvenidos")
while guess != secret:
    g = input ("Adivine el numero: ")
    guess = int (g)
    if guess == secret:
        print ("¡GANASTE!")
    else:
        if guess > secret:
            print ("Demasiado alto")
        else:
            print ("demasiado bajo")
print ("El número es:", secret)
print ("¡GAME OVER!")
