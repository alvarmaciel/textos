print ("¡Bienvenidos")
ping=1
while ping == 1
    g = input ("Adivine el numero: ")
    guess = int (g)
    if guess == 5:
        ping=1
    else:
        if guess > 5:
            print ("Demasiado alto")
        else:
            print ("demasiado bajo")
print ("¡GAME OVER!")
