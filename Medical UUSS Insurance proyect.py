"""El programa tiene por objetivo el análisis de una base de datos de 1334 muestras
las cuales son utilizadas para obtener datos relacionados a los seguros médicos en
Estados Unidos, cada función tiene una descripción para poder comprender mejor 
que realiza"""

import csv

def average_age(list_insurances):  #obtiene el promedio de edad de las muestras
    aver_age = 0
    i = 0
    for values in list_insurances: #itero dentro de la lista de diccionarios
        aver_age += float(values["age"]) #obtengo el valor y lo sumo
        i += 1
    aver_age = round(aver_age/i,2) # saco el promedio
    #print("The average age of the data set is: {}".format(aver_age))
    return aver_age

def average_cost(list_insurances): #obtiene el promedio de costo de seguro de las muestras
    aver_cost = 0
    i = 0
    for values in list_insurances: #itero dentro de la lista de diccionarios
        aver_cost += float(values["charges"]) # obtengo el valor y lo sumo
        i += 1
    aver_cost = round(aver_cost/i,2) # saco el promedio
    print("The average cost of the data set is: {}".format(aver_cost))
    return aver_cost

def age_for_region(list_insurances): #obtengo de forma porcentual la edad promedio por region y devuelvo un diccionario con la edad y region.
    list_dict = []
    list_dict2 = []
    over30_percent = 0
    dict_north_age_average = {}
    region_percent = 0
    
    for data in list_insurances: #itero dentro de la lista de diccionarios
        age_region_dict = {'age': data["age"],'region': data['region']} #armo mi nuevo diccionario
        list_dict.append(age_region_dict) #genero lista de diccionarios
        
        if int(data["age"]) > 30 and ('northwest' in data['region'] or 'northeast' in data['region']):#realizo control de flujo para evaluar cual es el promedio de edad en la region del norte
            over30_percent += 1
            dict_north_age_average = {'age': data["age"]}  #me genero un diccionario para luego utilizar la funcion average_age
            list_dict2.append(dict_north_age_average) #armo lista de diccionarios
            
        if  'northwest' in data['region'] or 'northeast' in data['region']: #me fijo el porcentaje que vive en el norte
            region_percent += 1
            
    list_dict2 = average_age(list_dict2) #aprovecho funciones ya armadas
    over30_percent = round(100/len(list_insurances) * over30_percent,2)
    region_percent = round(100/len(list_insurances) * region_percent,2)
    #print("For {} region the average age is: {}".format('north',north_age_average))
    print("The amount of people that is over 30 is '{}%'\nAnd the amount of people belonging to the north is '{}%'".format(over30_percent,region_percent))
    return list_dict,list_dict2

def smoker_north_people(list_of_dict): #armo función para evaluar la cantidad de gente del norte que fuma, y de esa cantidad, la cantidad que fuma teniendo hijos
    smoker_count = 0
    children_count = 0
    for data in list_of_dict: #itero dentro de lista de diccionarios
        if  ('northwest' in data['region'] or 'northeast' in data['region']) and data['smoker'] == 'yes' : #me fijo cuantos fuman
            smoker_count += 1
        if ('northwest' in data['region'] or 'northeast' in data['region']) and data['smoker'] == 'yes' and int(data['children']) > 0: #me fijo cuantos fuman y tienen hijos
            children_count += 1
    smoker_average_with_children = 100/len(list_of_dict) * children_count #saco promedio
    smoker_average = 100/len(list_of_dict) * smoker_count #saco promedio
    return round(smoker_average,2),round(smoker_average_with_children,2) #devuelvo valores en forma de porcentaje redondeados 
    
            
list_insurances = []  #armo lista fuera del archivo para poder seguir usando
with open("insurance.csv", 'r') as insurance_csv: #abro archivo para poder obtener los datos
    list_raw_data = csv.DictReader(insurance_csv)
    for raw in list_raw_data:
        list_insurances.append(raw)
        

#pruebo las funciones armadas para poder generar cierto análisis
age_region,average_age_for_region = age_for_region(list_insurances)
print("The average age for the north is {} years old".format(average_age_for_region))
smk_average,smk_childen = smoker_north_people(list_insurances)
print("The amount of people from the north that smokes is '{}%'\nAnd for the same region, the amount of people that smokes and have/has children is '{}%'".format(smk_average,smk_childen))

#guardo uno de los archivos como una nueva lista de diccionario
with open("age_for_region.csv", 'w', newline = '') as age_for_region_csv:
    fields = ['age','region']
    output = csv.DictWriter(age_for_region_csv , fieldnames = fields)
    output.writeheader()
    for data in age_region:
        output.writerow(data)  
