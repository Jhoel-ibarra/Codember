'''
Nos ha pedido ayuda. Y nos ha dado algunas pistas:

- Es una contraseña de 5 dígitos.
- La contraseña tenía el número 5 repetido como mínimo dos veces.
- El número a la derecha siempre es mayor o igual que el que
 tiene a la izquierda.

Nos ha puesto algunas ejemplos:
55678 es correcto lo cumple todo
12555 es correcto, lo cumple todo
55555 es correcto, lo cumple todo
12345 es incorrecto, no tiene el 5 repetido.
57775 es incorrecto, los números no van de forma creciente

Dice que el password está entre los números 11098 y 98123. 
¿Le podemos decir cuantos números cumplen esas reglas dentro de ese rango?
'''

if __name__ =="__main__":
    rango = list(range(11155,98056))
    new_list = list(filter(lambda elem: str(elem).count("5") > 1 ,rango))
    print(new_list)
    cadena = []
    for elem in new_list:
      l = str(elem)
      if all( l[carcter] <= l[carcter+1] for carcter in range(len(l) -1)):
        cadena.append(elem)
     # if(all(test_list[i] <= test_list[i + 1] for i in range(len(test_list)-1))): 
    print("**" *45)
    print(cadena)  
    print(len(cadena))
    print(cadena[55])

    
