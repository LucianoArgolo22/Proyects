#si bien no utilizo el lenguaje "inclusivo", el programa me pareció un tanto divertido de plantear

frase = 'todos somos programadores'
#frase = '¿cómo transmitir a los otros el infinito Aleph?'
palabras = frase.split() #divido la frase por defaulto en sus espacios//i split the phrase by default by its spaces
palabras_nuevas = [] #arranco una lista nueva vacía // i run a new empty list
for palabra in palabras: #ciclo mediante un for para ir recorriendo palabra por palabra // i iterate through the word's list
    if len(palabra)>=2: #pongo de condición inicial que mi palabra sea mayor a longitud 2 // i set my I.C. so that my word be longer than 2
        if palabra[-2]=='o': #si la letra a cambiar es la anteúltima//if the letter to change is the anteultimate
            palabra_nueva=palabra[:-2]+'e'+palabra[-1] #agrego la última letra para rearmar la palabra nueva // i add the last letter so i remake, the new word
        elif palabra[-1]=='o':#idem si es la última letra / Idem if its the last letter
            palabra_nueva=palabra[:-1]+'e'
        else:
            palabra_nueva=palabra #en caso que no cumpla , la palabra se mantiene igual//in case no if statements are triggered, the word remains the same
    else:
       palabra_nueva=palabra
    palabras_nuevas.append(palabra_nueva) #rearmamos la frase mediante una lista //i rejoin the phrase within a list
frase_t = ' '.join(palabras_nuevas)#y unimos cada palabra de la lista con un espacio de por medio recuperando la frase
                                   #we join the new word's list into a whole phrase (being a string now) with a space as delimiter
print(frase_t) 
