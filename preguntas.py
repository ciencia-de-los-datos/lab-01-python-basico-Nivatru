"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
with open('data.csv', mode ='r')as file:
  data = [line.split() for line in file]

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    return sum([int(x[1]) for x in data])


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """

    return sorted([(y, [x[0] for x in data].count(y)) for y in set([x[0] for x in data])])

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    registry = [(x[0], int(x[1])) for x in data]
    reg_dict = {x:0 for (x,_) in registry}
    for x in registry:
        reg_dict[x[0]] = reg_dict[x[0]] + x[1]
    registry = sorted(reg_dict.items())
    

    return registry


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """

    return sorted([(y, [x[2].split("-")[1] for x in data].count(y)) for y in set([x[2].split("-")[1] for x in data])])

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]
    

    """

    local = [(x[0], int(x[1])) for x in data]
    local_dict = {x[0]:[] for x in local}
    for i in local:
        local_dict[i[0]].append(i[1])
    local = list(local_dict.items())
    local = sorted([(x[0], max(x[1]), min(x[1])) for x in local])

    return local


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]
    
    """

    local = [x[4].split(",") for x in data]
    local_dict = {}
    for x in local:
        for y in x:
            key = y[:3]
            value = int(y[4:])
            if key not in local_dict:
                local_dict[key] = [value]
            else:
                local_dict[key].append(value)
    local = list(local_dict.items())
    local = sorted([(x[0], min(x[1]), max(x[1])) for x in local])

    return local

def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]
    
    """
    local = [(x[0], int(x[1])) for x in data]
    local_dict = {x[1]:[] for x in local}
    for i in local:
        local_dict[i[1]].append(i[0])

    return sorted(list(local_dict.items()))


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """

    local = [(x[0], int(x[1])) for x in data]
    local_dict = {x[1]:[] for x in local}
    for i in local:
        local_dict[i[1]].append(i[0])
    local = sorted(list(local_dict.items()))
    local = [(x[0], sorted(list(set(x[1])))) for x in local]
    return local


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """

    local = [x[4].split(",") for x in data]
    local_dict = {}
    for x in local:
        for y in x:
            key = y[:3]
            value = int(y[4:])
            if key not in local_dict:
                local_dict[key] = [value]
            else:
                local_dict[key].append(value)
    local = list(local_dict.items())
    local = {x[0]:len(x[1]) for x in local}
    return local


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]
    

    """
    local = [(x[0], len(x[3].split(",")), len(x[4].split(","))) for x in data]
    return local

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    local = [(int(x[1]), x[3].split(",")) for x in data]
    local_dir = {}
    for i in local:
        for y in i[1]:
            if y not in local_dir:
                local_dir[y] = i[0]
            else:
                local_dir[y] = local_dir[y] + i[0]
    return local_dir

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    local = [(x[0], sum([int(y[4:]) for y in x[4].split(",")])) for x in data]
    local_dir = {x[0]:0 for x in set([y[0] for y in local])}
    for i in local:
        local_dir[i[0]] = local_dir[i[0]] + i[1]
    return local_dir

