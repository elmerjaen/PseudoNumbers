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

def power(seed):
  return str(int(seed)**2)

def new_row(iter):
  data.append([]) #create a new row
  data[iter].append(iter) #insert iteration number

def merge(seed,iter):
  data[iter].append(seed)

def medio(seed,iter,band):
  if band == True:
      merge(seed,iter)
      seed = power(seed)
      merge(seed,iter)
      medio(seed,iter,False)
  else:
      count = 0
      for i in seed:
        count += 1
      if count == 4:
          seed = power(seed)
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
                  medio("0"+seed,iter,False)

def start():
  print('Método del Cuadrado Medio.\n')
  seed = input('Ingrese el valor semilla: ')
  new_row(0)
  medio(seed,0,True)
  print("\nEl resultado es:\n")
  table()

if __name__ == '__main__':
  start()