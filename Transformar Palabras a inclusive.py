# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 21:01:55 2020

@author: Lucia
"""

frase = 'todos somos programadores'
#frase = '¿cómo transmitir a los otros el infinito Aleph?'
palabras = frase.split()
palabras_nuevas = []
for palabra in palabras:
    if len(palabra)>=2:
        if palabra[-2]=='o':
            palabra_nueva=palabra[:-2]+'e'+palabra[-1]
        elif palabra[-1]=='o':
            palabra_nueva=palabra[:-1]+'e'
        else:
            palabra_nueva=palabra
    else:
       palabra_nueva=palabra
    palabras_nuevas.append(palabra_nueva)
frase_t = ' '.join(palabras_nuevas)
print(frase_t)