# Lista base para pruebas
lista = [1, 2, 3]

# 1. append(e): Agrega un elemento al final de la lista
lista.append(4)
print("append(4) =>", lista)  # [1, 2, 3, 4]

# 2. insert(i, e): Inserta un elemento en una posición específica
lista.insert(1, 99)
print("insert(1, 99) =>", lista)  # [1, 99, 2, 3, 4]

# 3. count(e): Cuenta cuántas veces aparece un elemento
conteo = lista.count(2)
print("count(2) =>", conteo)  # 1

# 4. remove(e): Elimina la primera aparición de un elemento
lista.remove(99)
print("remove(99) =>", lista)  # [1, 2, 3, 4]

# 5. pop(i): Elimina y retorna el elemento en la posición dada
elemento = lista.pop(2)
print("pop(2) =>", elemento, "| Lista:", lista)  # 3, Lista: [1, 2, 4]

# 6. index(e): Devuelve el índice de la primera aparición del elemento
indice = lista.index(2)
print("index(2) =>", indice)  # 1

# 7. sort(): Ordena la lista de forma ascendente
lista.sort()
print("sort() =>", lista)  # [1, 2, 4]

# 8. reverse(): Invierte el orden de la lista
lista.reverse()
print("reverse() =>", lista)  # [4, 2, 1]

# 9. clear(): Vacía todos los elementos de la lista
lista.clear()
print("clear() =>", lista)  # []

# 10. copy(): Crea una copia independiente de la lista
original = [10, 20, 30]
copia = original.copy()
copia.append(40)
print("original =>", original)  # [10, 20, 30]
print("copy().append(40) =>", copia)  # [10, 20, 30, 40]