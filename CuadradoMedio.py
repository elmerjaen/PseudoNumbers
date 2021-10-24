# Método del Cuadrado Medio
# Louis Aguilar, Omar Flores, Elmer Jaén
import matplotlib.pyplot as plt

data = []
def table():
  fig, ax = plt.subplots(1,1)
  plt.rcParams.update({'font.size': 18}) #change font size
  column_labels=["n", "R(n)", "R(n)^2","M.R(n)^2"]
  ax.axis('tight')
  ax.axis('off')
  the_table = ax.table(cellText=data, colLabels=column_labels, loc="center", cellLoc='center')
  the_table.scale(2,3) #change table scale
  for i in range(0, 4):
    the_table[(0, i)].set_facecolor("#56b5fd")
  plt.show()

def new_row(iter):
  data.append([]) #create a new row
  data[iter].append(iter) #insert iteration number

def merge(iter,seed):
  data[iter].append(seed)

def medio(iter,seed):
  merge(iter,seed) #write seed
  tam1 = len(seed)
  seed = str(int(seed)**2)
  merge(iter,seed) #write seed**2
  tam2 = len(seed)
  firstc = int((tam2 - tam1) / 2) #calculate first digit
  new_seed = seed[firstc:firstc+tam1] #get new seed
  merge(iter,new_seed) #write new_seed
  if iter == 9:
    return
  new_row(iter+1)
  medio(iter+1,new_seed)

def start():
  print('Método del Cuadrado Medio.\n')
  seed = input('Ingrese el valor semilla: ')
  new_row(0)
  medio(0,seed)
  print("\nEl resultado es:\n")
  table()

if __name__ == '__main__':
  start()