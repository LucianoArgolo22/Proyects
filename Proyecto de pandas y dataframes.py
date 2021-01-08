import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob 

files = glob.glob('states*.csv') #tengo varios dataframes, en distintos arhivos con el mismo nombre y distinto número
df_list = [] #armo lista vacía
for files in files:
  df = pd.read_csv(files) #voy leyendo cada csv y lo guardo como df
  df_list.append(df) #me armo la lista de df's

all_data = pd.concat(df_list) #con concat los junto todos, y obtengo un nuevo df con los atributos de todos
all_data.columns = all_data.columns.str.lower() #paso a minúscula los nombres de las columnas para trabajarlos más fácil

all_data = all_data.reset_index() #genero un nuevo index, dado que el anterior se repetía de 0 a 5 generandome errores 
all_data = all_data[['state','totalpop','hispanic','white','black','native','asian','pacific','genderpop','income']] #saco los index viejos

all_data = all_data.drop_duplicates(subset = ['state']).reset_index(drop = True) #saco las filas repetidas



gender_data = all_data.genderpop.replace('_','',regex=True).reset_index(drop= True) #empiezo a limpiar los datos

gender_data = gender_data.str.strip('F').reset_index(drop = True)#sigo limpando


women_data = gender_data.str.split('M',expand = True)[1] #separo datos en mujeres
men_data = gender_data.str.split('M',expand = True)[0]# tomo los datos de hombres
women_data = pd.to_numeric(women_data)  #paso a formato numérico dado que estaba en string
men_data = pd.to_numeric(men_data)
print(len(all_data)) #me fijo cual es la longitud de las filas

income_data = all_data.income.str.strip('$').reset_index() #limpio los datos del income
income_data.income = round(pd.to_numeric(income_data.income),2) #redondeo para que sea más prolijo (suponiendo que fueran decimales)
all_data['income'] = income_data.income #creo que está de más
all_data['menpop'] = men_data # genero nuevas columnas con los datos limpios
all_data['womenpop'] = women_data


#print(all_data)
all_data = all_data[['state','totalpop','hispanic','white','black','native','asian','pacific','income','womenpop','menpop']]
#print(all_data.womenpop)
#print(all_data)

all_data.totalpop = pd.to_numeric(all_data.totalpop)
all_data.womenpop = all_data.womenpop.fillna(all_data.totalpop - all_data.menpop)
#print(all_data.womenpop)
plt.scatter(all_data.womenpop,all_data.income) #armo un gráfico para mostrar como es la relación
plt.show()#muestro el gráfico

def from_percent_topop(x): # quiero pasar de porcentajes a unidades(personas) para toda la tabla, así que armo una función que haga el laburo 
  all_data.totalpop = pd.to_numeric(all_data.totalpop)
  clean_string = x.str.strip('%') #la variable x, es el equivalente a all_data.{columna de interés}, le saco el porcentual
  clean_string_numeric = pd.to_numeric(clean_string) # paso de string a numérico
  pop_number = clean_string_numeric * all_data.totalpop / 100 #busco el equivalente del porcentaje en población
  return round(pop_number,2) #devuelvo el valor redondeado (más prolijo)

all_data = all_data[['state','totalpop','hispanic','white','black','native','asian','pacific','income','womenpop','menpop']]

all_data.hispanic = from_percent_topop(all_data.hispanic) #actualizo todos los valores
all_data.white = from_percent_topop(all_data.white)
all_data.black = from_percent_topop(all_data.black)
all_data.native = from_percent_topop(all_data.native)
all_data.asian = from_percent_topop(all_data.asian)
all_data.pacific = from_percent_topop(all_data.pacific)
print(all_data) #lo corroboro
all_data.pacific = round(all_data.pacific.fillna(all_data.totalpop - (all_data.hispanic + all_data.white + all_data.black + all_data.native + all_data.asian )),2)
# no armo función para los valores nan de pacific, dado que solamente el atributo pacific presenta valores nan
print(all_data.pacific)

all_data.totalpop = pd.to_numeric(all_data.totalpop)
all_data.womenpop = all_data.womenpop.fillna(all_data.totalpop - all_data.menpop) #completo los valores nan

plt.scatter(all_data.womenpop,all_data.income) #muestro grafico de los ingresos por mujer en cada estado
plt.show()

all_data.hist(column = 'white')  #muestro histograma sobre una de las etnias vs estado
plt.show()
all_data.hist(column = 'womenpop') #muestro histograma sobre mujeres por estado
plt.show()

