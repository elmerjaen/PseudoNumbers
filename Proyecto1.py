data = []
def potencia(seed):
    return str(int(seed)**2)

def new_row(numero):
    data.append([]) #se crea la fila
    data[numero].append(numero) #se inserta el número de iteración

def unir(data,seed,numero):
    data[numero].append(seed)

def medio(seed,numero,band):
    if band == True:
        unir(data,int(seed),numero)
        band = False
        seed = potencia(seed)
        unir(data,seed,numero)
        medio(seed,numero,band)
    else:
        count = 0
        for i in seed: count += 1
        if count == 4:
            seed = potencia(seed)
            unir(data,seed,numero)
            medio(seed,numero,band)
        else:
            if numero >= 0 and numero < 2:
                if count == 8:
                    seed = seed[2:len(seed)-2]
                    unir(data,seed,numero)
                    if numero == 1:
                        return
                    new_row(numero+1)
                    medio(seed,numero+1,True)
                elif count == 6:
                    seed = seed[1:len(seed)-1]
                    unir(data,seed,numero)
                    if numero == 1:
                        return
                    new_row(numero+1)
                    medio(seed,numero+1,True)
                else:
                    medio("0"+seed,numero,band)
            else:
                print("Programa terminado")

def run(seed,numero):
    new_row(numero)
    medio(seed,numero,True)

def start():
    # el usuario ingresa la semilla y se eleva al cuadrado
    # seed = str(int(input('Ingrese el valor semilla: '))**2)
    seed = input('Ingrese el valor semilla: ')
    run(seed,0)
    print(data)

if __name__ == '__main__':
    start()