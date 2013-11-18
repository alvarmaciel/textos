print ("¡Bienvenidos")
g=input ("Adivine el numero: ")
guess =int (g)
if guess == 5:
    print ("¡Ganaste!")
else:
    if guess > 5:
        print ("Demasiado alto")
    else:
        print ("demasiado bajo")
print ("¡GAME OVER!")
