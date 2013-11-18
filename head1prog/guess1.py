print ("¡Bienvenidos")
ping=True
while ping == True
    g = input ("Adivine el numero: ")
    guess = int (g)
    if guess == 5:
        ping=True
    else:
        if guess > 5:
            print ("Demasiado alto")
        else:
            print ("demasiado bajo")
print ("¡GAME OVER!")
