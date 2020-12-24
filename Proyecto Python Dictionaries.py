#En este pequeño programa hago una serie de funciones para el análisis de datos obtenidos en relación a algunos 
#Huracanes sucedidos a lo largo de la historia 




# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]


# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

#--------------------------------------------

#Armo la primer función, partiendo de los daños hechos en dólares, por lo que transformo los strings en floats
# write your update damages function here:
    #armo la función de daños actualizados 
damages_updated = [] #guardo lista fuera de la funcion
def update_damages(damages):
  for damage in damages: #recorro todos los daños realizados
    if damage[-1] == "M": #para los daños con M, los multiplico por 1 millón y los agrego a mi lista vacía
      damage = round(float(damage[:-1]),2)
      damages_updated.append(damage*1000000)
    elif damage[-1] == "B": #para los daños con B, los multiplico por 1 Billón, idem lista vacía
      damage = round(float(damage[:-1]),2)
      damages_updated.append(damage*(1000000**2))
    else:#para el caso que no haya daños con M, o con B, se deduce que no hubo daños registrados
      damages_updated.append("Damages not recorded")
  #return print(damages_updated)
  
update_damages(damages)

#----------------------------------------------------
#armo función para generar base de datos mediante diccionario
#hago que las Keys sean los nombres, y el resto de los datos los valores, generando
#un diccionario dentro de otro

hurricane_data_base = {} #declaro mi diccionario por fuera para poder seguir utilizandolo sin necesidad de llamar la función
def dictionary_construct(names,months,years,max_sustained_winds,areas_affected,deaths,damages_updated):
  i = 0
  while i < 34 : #itero para los 34 datos correspondientes a cada huracán
    hurricane_data_base[names[i]] ={"Month": months[i], "Year": years[i], "Maximum Winds":max_sustained_winds[i], "Areas affected": areas_affected[i], "Deaths": deaths[i], "Damages": damages_updated[i]}
    i += 1
  #print(hurricane_data_base)
dictionary_construct(names,months,years,max_sustained_winds,areas_affected,deaths,damages_updated)
HDB = hurricane_data_base #simplifico el nombre de la base de datos que cree sobre huracanes
#---------------------------------------------------


#armo un diccionario otra vez, pero ésta vez con los años como Keys
HDBU = {}
def hurricane_by_year_dictionary(hurricanes_data_base): #armo nueva funcion que pone de Key los años
    hurricane_by_year = [] #armo lista vacía
    year = 1924    #hago ciclar desde el primer evento hasta el final
    while year < 2020:   #hago ciclar desde el primer evento hasta el final
        for name,values in hurricanes_data_base.items(): # itero dentro de mi diccionario
            if hurricanes_data_base[name]["Year"] == year: #comparo valores
                values["Nombre"] = name   #si el año es igual a un año ya ingresado en la lista
                hurricane_by_year.append(values) #entonces agrega el año a la lista
                HDBU[year] = hurricane_by_year   #generando un diccionario con lista formada por diccionarios
        year += 1
        hurricane_by_year = []  #reinicia la lista para evitar no repetir info
    return HDBU #devuelve la lista ya impecable
hurricane_by_year_dictionary(HDB)
#print(HDBU) #dejo como comentario los print de la mayoría de las funciones para en caso de probarla, no aparecer toda la información junta




#-------------------------------------------
#armo función que cuente que tan seguido cada área es afectada
#armo diccionario con esos datos, donde las Keys son las áreas afectadas y
#los valores cuentan ccuantas veces las áreas fueron o son afectadas
AAC = {} #armo lista de Area Affected Counts por fuera de la función para que no muera dentro
def damage_area_counts(hurricane_data_base):
    cont = 0 #pongo contador en 0
    for keys,values in hurricane_data_base.items(): #obtengo el diccionario dentro del diccionario y los recorro
        for values2 in values["Areas affected"]: #voy directo a los valores que me interesan dentro del key de interés y los recorro
            cont = values["Areas affected"].count(values2) #cuento cuantas veces se encuentra el valor particular dentro de esa lista
            if values2 in AAC.keys(): #si mis valores ya estaban en el diccionario, significa que tengo que actualizar y aumentar su cantidad de apariciones
                AAC[values2] = AAC[values2] + cont
            else:  #si mis valores no estaban en el diccionario los agrego
                AAC[values2] = cont
    #print(AAC)

damage_area_counts(hurricane_data_base) #pruebo función
#print(AAC) #corroboro que la lista sobrevive a la función, para posterior uso

#--------------------------------------------------

#armo una funcion que me dice cual fue el area mas afectada por huracanes
#y que ademas diga cuantas veces fue que golpeo esa area
def most_affected_area(AAC):
    maximum = 0 #inicializo contador
    for areas,times in AAC.items(): #separo keys y values e itero
        if times > maximum : #comparo cada valor con el anterior para ver si es mayor o no
            maximum = times
            area = areas
    #print("\n Most often affected area is:" + area + " - " + str(maximum) + " times")
most_affected_area(AAC)

#--------------------------------------------------

#armo funcion que determina cual fue el huracan mas peligroso en funcion de las
#muertes, y asi mismo informo la cantidad de muertes ocasionadas
def most_dangerous_hurricane(hurricane_data_base):
    deaths_max = 0 #inicializo contador
    for keys,values in hurricane_data_base.items(): #itero entre los keys y los values
        if values["Deaths"] > deaths_max: #comparo valor actual con 
            deaths_max = values["Deaths"]
            hurricane_name = keys
    #print("The Hurricane that caused most deaths: " + str(deaths_max) + "\n was the : " + hurricane_name )

most_dangerous_hurricane(hurricane_data_base)

#--------------------------------------------------

# armo funcion según mortalidad de los huracanes, y
#armo nuevo diccionario
mortality_scale = {}
mortality_scale_organized = {}
mortality_scale_organized[0] = {}
print(HDBU.keys())
def mortality_scale_dictionary(HDB):
    lista1 = [] #armo listas para guardar cada Huracán dentro de ellas
    lista2 = []
    lista3 = []
    lista4 = []
    lista5 = []
    for keys,values in HDB.items(): #planteo 5 casos de mortalidad por parámetros
        if values["Deaths"] <= 100:
            lista1.append(keys) #agrego el nombre del huracán en caso de que cumpla
            mortality_scale[0] = lista1
            
        elif values["Deaths"] > 100 and values["Deaths"] <= 500:
            lista2.append(keys)  #idem el resto de las condiciones
            mortality_scale[1] = lista2
            
        elif values["Deaths"] > 500 and values["Deaths"] <= 1000:
            lista3.append(keys)
            mortality_scale[2] = lista3
            
        elif values["Deaths"] > 1000 and values["Deaths"] <= 10000:
            lista4.append(keys)
            mortality_scale[3] = lista4
            
        elif values["Deaths"] > 10000:
            lista5.append(keys)
            mortality_scale[4] = lista5

    i = 0
    #creo que la parte más importante, la legibilidad, organiza los datos obtenidos
    for keys in sorted(mortality_scale.keys()): #organizo las escalas de menor a mayor númericamente.
        mortality_scale_organized[keys] = mortality_scale[i] 
        i += 1
        
    #ordeno un poco más como muestro los datos y ahora quedo más prolijo.    
    print("\nEscala de mortalidad: \n____________________\n")
    for keys,values in mortality_scale_organized.items(): 
        print(str(keys) + ": " + str(values) + "\n")
    return sorted(mortality_scale_organized)

mortality_scale_dictionary(HDB)

#armo funcion que muestre escala de daños generados en dólares
damage_scale = {}
damage_scale_organized = {} # coloco ambos diccionarios por fuera de la función en caso de que quiera reutilizarlos
def damage_scale_function(HDB):
    lista1 = [] #armo listas para guardar cada Huracán dentro de ellas
    lista2 = []
    lista3 = []
    lista4 = []
    lista5 = []
    lista6 = [] #lista 6 para aquellos que no registraron daño
    for keys,values in HDB.items(): #planteo 5 casos de mortalidad por parámetros
        if values["Damages"] == "Damages not recorded":
            lista6.append(keys)
            damage_scale[6] = lista6
            
        elif values["Damages"] <= 100000000:
            lista1.append(keys) #agrego el nombre del huracán en caso de que cumpla
            damage_scale[0] = lista1
            
        elif values["Damages"] > 100000000 and values["Damages"] <= 1000000000:
            lista2.append(keys)  #idem el resto de las condiciones
            damage_scale[1] = lista2
        elif values["Damages"] > 1000000000 and values["Damages"] <= 10000000000:
            lista3.append(keys)
            damage_scale[2] = lista3
            
        elif values["Damages"] > 10000000000 and values["Damages"] <= 50000000000:
            lista4.append(keys)
            damage_scale[3] = lista4
            
        elif values["Damages"] > 50000000000:
            lista5.append(keys)
            damage_scale[4] = lista5   

    return damage_scale
print(damage_scale_function(HDB))

#armo función que busque cual fue el huracan más destructivo, en daños generados en dólares.

def find_mostdamage_cost(HDB):
    maxdamage = 0.0
    for keys,values in HDB.items(): #itero dentro de los keys y values
        if values["Damages"] == "Damages not recorded" : #comparo para los que no tienen daño
            print( keys + " has no damage recorded")
        elif float(values["Damages"]) > maxdamage: #comparo para los que si tienen daño
            maxdamage = values["Damages"]
            hurricane_name = keys
    #print("The most destructive hurricane was: " + hurricane_name + " with a damage in dollars of : " + str(maxdamage) + " Done")

find_mostdamage_cost(HDB)
    

