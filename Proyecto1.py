def run(seed,numero):
    count = 0
    numero -= 1
    for i in seed: count += 1

    # 8 -> restar 2
    # 6 -> restar 1
    if numero > 0:
        if count == 8:
            seed = seed[2:len(seed)-2]
            print(seed)
            run(str(int(seed)**2),numero)
        elif count == 6:
            seed = seed[1:len(seed)-1]
            print(seed)
            run(str(int(seed)**2),numero)
        else:
            run("0"+seed,numero)
    else:
        print("Programa terminado")

def start():
    # el usuario ingresa la semilla y se eleva al cuadrado
    seed = str(int(input('Ingrese el valor semilla: '))**2)
    run(seed,10)

if __name__ == '__main__':
    start()