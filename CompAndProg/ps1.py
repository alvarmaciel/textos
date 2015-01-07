primo = True ## Verificador de primalidad
num = 2 ## Número por el que empiezo asumiendo que 1 no lo consideramos primo
numMod = 1 ## Número por el que voy a dividir para sacar el módulo
resMod = 0 ## Valor del módulo calculado entre 2 y n-1
cantPrimo= 0 ## Verificador de cantidades de primos que llevo calculados
while cantPrimo < 1000: ## Mientras la cantidad de primos descubiertos sea menor a mil ejecutar el loo
    if num > 3: ## así obvio 2 y 3 que ya se que son primos :D
        while numMod < num/2+1: ## itera entre 2 y n-1 para verificar si el modulo es distinto de cero
            resMod = num%numMod ## calculo el modulo de n y n' (distinto de 1 y n)
            if resMod == 0: ## si da cero en numMod es divisor de n po lo cual no es primo
                primo = False
                numMod = num ## salgo del loop
            else:
                primo = True ## si no da 0 el numero aprenta ser primo
            numMod = numMod + 1 ## aumento numMod para seguir buscando la divisibilidad
    if primo == True: ## si no encontré divisores es que n es primo entonces imprimo
        print num
        cantPrimo=cantPrimo +1 ## aumento la cantidad de primos encontrados en 1
    num = num + 1 ## amuento el número a descubrir
    numMod = 2 ## fijo la primer división
print 'Cantidad de números Primos:', cantPrimo
