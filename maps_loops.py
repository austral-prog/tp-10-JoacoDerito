def find_max_value(dict):
    a = ""
    max = 0

    for k, v in dict.items():
        if v > max:
            max = v
            a = k 

    return a

dict = {
    "John": 85,
    "Emma": 92,
    "Sophia": 78
}

a = find_max_value(dict)
print(a)

def reverse_dict(dict):
       a = {}
    for k, v in dicc.items():
        if v in a:
            a[v]+=(k)
        else:
            a[v] = k

    return a

dict = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 3,
    "e": 2
}

a = reverse(dict)
print(a)

def word_freq_counter(words):
    d = dict()
    for word in words:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    return d

frutas = ["apple", "banana", "apple", "orange", "banana", "apple"]

frecuencia = word_freq_counter(frutas)
print(frecuencia)

def find_biggest_expense(expenses):
    answer = ('', 0)
    for key, value in expenses.items():
        average = 0
        for i in value:
            average += i
        average = average / len(value)
        if answer[1] < average:
            answer = (key, average)
    return answer[0]
gasto= {
    'Food': [60, 80, 100],
        'Transport': [10, 1, 2],
        'Games': [10, 20, 30]
}
resultado = find_biggest_expense(gasto)
print(resultado)


def sum_of_expenses(dic):
    a = {}
    for clave, valor in dic.items():
        suma = 0
        for nro in valor:
            suma += nro
        a[clave] = suma
    return a
gasto= {
    'Food': [60, 80, 100],
        'Transport': [10, 1, 2],
        'Games': [10, 20, 30]
}
resultado = sum_of_expenses(gasto)
print(resultado)


def sum_of_expenses_by_type(expenses):
     a={}
    for k, v in dict.items():
        for type, expense in v:
            if type in a:
                a[type]+= expense
            else:
                a[type]= expense
    return a
b={
    'Food': [("A", 60), ("B", 100), ("A", 20)], 
    'Transport': [("A", 10), ("B", 50), ("C", 5)], 
    'Games': [("A", 6), ("B", 24), ("C", 99)]
}
resultado = sum_of_expenses_by_type(b)
print(resultado)
