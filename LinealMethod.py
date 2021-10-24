# Método Congruencial Lineal
# Louis Aguilar, Omar Flores, Elmer Jaén
import matplotlib.pyplot as plt

data = []
def table():
  fig, ax = plt.subplots(1,1)
  plt.rcParams.update({'font.size': 18}) #change font size
  column_labels=["n", "R(n)", "a*X(n)+c","[a*X(n)+c] mod m"]
  ax.axis('tight')
  ax.axis('off')
  the_table = ax.table(cellText=data, colLabels=column_labels, loc="center", cellLoc='center')
  the_table.scale(2,3) #change table scale
  for i in range(0, 4):
    the_table[(0, i)].set_facecolor("#56b5fd") #change first row color
  plt.show()

def new_row(iter):
  data.append([]) #create a new row
  data[iter].append(iter) #insert iteration number.

def merge(seed,iter):
  data[iter].append(seed)

def lineal(seed,iter,a,c,m):
  if iter >= 0 and iter < 10:
    merge(seed,iter)
    seed = seed*a+c
    merge(seed,iter)
    seed = seed % m
    merge(seed,iter)
    if iter == 9:
        return
    new_row(iter+1)
    lineal(seed,iter+1,a,c,m)

def start():
  print('Método Congruencial Lineal.\n')
  seed = int(input('Ingrese el valor para X0: '))
  a = int(input('Ingrese el valor para a: '))
  c = int(input('Ingrese el valor para c: '))
  m = int(input('Ingrese el valor para m: '))
  new_row(0)
  lineal(seed,0,a,c,m)
  print('\nEl resultado es: \n')
  table()

if __name__ == '__main__':
  start()
