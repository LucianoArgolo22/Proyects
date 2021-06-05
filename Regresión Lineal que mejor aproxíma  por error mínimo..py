#PROGRAMA QUE CALCULA APROXIMACION POR MEJOR RECTA PARA REGRESION LINEAL
"""
Created on Sun Dec 27 12:40:52 2020

@author: Lucia
"""

def get__y(m, b, x): #calculo los valores que debería dar realmente la recta
    y = m * x + b
    return y

#print(get__y(1,0,7)) #pruebo un par
#print(get__y(5,10,3))


def calculate_error(m,b,point): #le paso valor de la pendiente, y de la constante, más el punto de coordenadas
    x_point = point[0]
    y_point = point[1]
    distance = abs(get__y(m,b,x_point) - y_point) #calculo el valor absoluto entre los puntos que me dan, y la recta
    return distance #devuelvo el error absoluto como distancia
    
print('')
print('')


def calculate_all_error(m,b,datapoints): #calculo la sumatoria de errores (no promedio) para todos los puntos dados de una serie de puntos
    total_error_summ = 0
    for point in datapoints:
        total_error_summ += calculate_error(m,b,point)
    return total_error_summ
"""

datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, 0, datapoints))
print('')


datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, 1, datapoints))
print('')


datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, -1, datapoints))
print('')



datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(-1, 1, datapoints))
"""

possible_ms = [round(m * 0.1,2) for m in range(-100,101)] #busco valores entre -10 y 10 para m
possible_bs = [round(b * 0.1,2) for b in range(-200,201)] #idem para b entre -20 y 20

def smallest_error(possible_ms,possible_bs,datapoints): #busco los valores que mejor aproximan de m y b
    smallest = 100
    for m in possible_ms: #itero dentro de la lista de m's
        for b in possible_bs: #itero dentro de la lista de b's para cada m dado
            error = calculate_all_error(m,b,datapoints) #obtengo error
            if error < smallest: #control de flujo para comparacion de errores
                smallest = error
                best_fist_values["Para m"] = m #guardo los valores obtenidos que me sirven
                best_fist_values["Para b"] = b
            else:
                pass
    return smallest,best_fist_values #devuelvo valores

datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)] #pruebo los m´s y b´s que mejor ajustan a los datos de puntos

best_fist_values = {} #armo diccionario para m´s y b´s, para mayor legibilidad
error,best_fist_values = smallest_error(possible_ms,possible_bs,datapoints) #guardo los valores obtenidos

#m = best_fist_values["Para m"]
#b = best_fist_values["Para b"]

print('La recta que mejor aproxima es: \ny = {}*x + {} \n\nCon un error absoluto de {}'.format(best_fist_values["Para m"],best_fist_values["Para b"],error))

       	 
