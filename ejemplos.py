#1. x.append(e)
#Agrega a la lista x el elemento e.

x = [1, 2, 3]
x.append(4)
print(x)  # [1, 2, 3, 4] 


#2. x.insert(i, e)
#Inserta e en la posición i de la lista x.


x = [1, 2, 3]
x.insert(1, 10)
print(x)  # [1, 10, 2, 3]

#3. x.count(e)
#Cuenta cuántas veces aparece e en la lista x.


x = [1, 2, 2, 3, 2]
print(x.count(2))  # 3
#4. x.remove(e)
#Elimina la primera aparición de e en la lista x.


x = [1, 2, 3, 2]
x.remove(2)
print(x)  # [1, 3, 2]
#5. x.pop(i)
#Devuelve el elemento en la posición i y lo elimina de la lista.


x = [1, 2, 3]
elemento = x.pop(1)
print(elemento)  # 2
print(x)         # [1, 3]
#6. x.index(e)
#Devuelve la posición de la primera aparición de e en la lista x.


x = [1, 2, 3, 2]
print(x.index(2))  # 1
#7. x.sort()
#Ordena la lista x en forma creciente.


x = [3, 1, 2]
x.sort()
print(x)  # [1, 2, 3]
#8. x.reverse()
#Invierte la lista x.


x = [1, 2, 3]
x.reverse()
print(x)  # [3, 2, 1]
#9. x.clear()
#Vacía la lista x.


x = [1, 2, 3]
x.clear()
print(x)  # []
#10. x.copy()
#Devuelve una copia de la lista x.


x = [1, 2, 3]
y = x.copy()
y.append(4)
print(x)  # [1, 2, 3]
print(y)  # [1, 2, 3, 4]