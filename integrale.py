#esercizio del prof sugli integrali
from math import sqrt

n= int(input("inserisci il numero di segmenti: "))

def integrale_y (n):
    area_totale = 0
    dx = 1/n
    for i in range (n):
     x = i * dx
     area = ((dx) * (sqrt(1-x**2)))
     area_totale += area
    return area_totale

risultato = integrale_y(n)
print(f"L'approssimazione dell'integrale con segmenti {n} è: {risultato}")
print(f"confronto con il Valore esatto che è: {3.1415926535 / 4}") #pigreco/4 è quello perche è un quarto di circonferenza e il parametro resta stabile tra 0-1

valore= integrale_y(n)/3.1415926535
print(f"questo è il valore diviso pi greco: {valore}")

#è piu accurato o meno accurato a seconda del numero di segmenti che si inseriscono nella n
