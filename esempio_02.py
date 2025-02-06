numero=int(input("dammi un numero:  "))
lettera=input("dammi una lettera:  ")
for i in range(0, numero) :
    print (" " *(numero-i-1) + lettera * (2 * i+1) )