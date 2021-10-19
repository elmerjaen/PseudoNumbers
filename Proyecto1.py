data = []
def run(seed,numero,j):
    data.append([])
    data[j].append(j)
    count = 0
    numero += 1
    for i in seed: count += 1

    # 8 -> restar 2
    # 6 -> restar 1
    if numero > 0 and numero < 10:
        data[j].append(seed)
        seed = str(int(seed)**2)
        data[j].append(seed)
        if count == 8:
            seed = seed[2:len(seed)-2]
            data[j].append(seed)
            run(str(int(seed)**2),numero)
        elif count == 6:
            seed = seed[1:len(seed)-1]
            data[j].append(seed)
            run(str(int(seed)**2),numero)
        else:
            run("0"+seed,numero,0)
    else:
        print("Programa terminado")

def start():
    # el usuario ingresa la semilla y se eleva al cuadrado
    # seed = str(int(input('Ingrese el valor semilla: '))**2)
    seed = input('Ingrese el valor semilla: ')
    run(seed,0,0)

if __name__ == '__main__':
    start()