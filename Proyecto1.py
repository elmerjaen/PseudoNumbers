data = []
def potencia(seed):
    return str(int(seed)**2)

def new_row(iter):
    data.append([]) #create a new row
    data[iter].append(iter) #insert iteration number

def merge(seed,iter,data):
    data[iter].append(seed)

def medio(seed,iter,band):
    if band == True:
        merge(seed,iter)
        band = False
        seed = potencia(seed)
        merge(seed,iter)
        medio(seed,iter,band)
    else:
        count = 0
        for i in seed: count += 1
        if count == 4:
            seed = potencia(seed)
            merge(seed,iter)
            medio(seed,iter,band)
        else:
            if iter >= 0 and iter < 10:
                if count == 8:
                    seed = seed[2:len(seed)-2]
                    merge(seed,iter)
                    if iter == 9:
                        return
                    new_row(iter+1)
                    medio(seed,iter+1,True)
                elif count == 6:
                    seed = seed[1:len(seed)-1]
                    merge(seed,iter)
                    if iter == 9:
                        return
                    new_row(iter+1)
                    medio(seed,iter+1,True)
                else:
                    medio("0"+seed,iter,band)
            else:
                print("Programa terminado")

def run(seed,iter):
    new_row(iter)
    medio(seed,iter,True)

def start():
    # el usuario ingresa la semilla y se eleva al cuadrado
    # seed = str(int(input('Ingrese el valor semilla: '))**2)
    seed = input('Ingrese el valor semilla: ')
    run(seed,0)
    print(data)

if __name__ == '__main__':
    start()