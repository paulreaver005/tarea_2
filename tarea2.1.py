todos = [
[177,145,167,190,140,150,180,130],
[165,176,145,189,170,189,159,190],
[145,136,178,200,123,145,145,134],
[201,110,187,175,156,165,156,135]
]

# imprime todas las alturas
print("Lista con todas las alturas - ", str(todos))

# encuentra la altura maxima de cada grupo y la ingresa en una sublista
ans = list(map(max, todos))

# encuentra la altura maxima de cada grupo de personas de la sublista y sacamos el indice de la posicion
indice = ans.index(max(ans))

# se imprime la lista con solo el grupo donde se encuentra la altura mayor de todas las personas
print('El grupo con la altura mayor de todas las personas es: ', todos[indice])