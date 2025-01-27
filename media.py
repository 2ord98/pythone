risposta = (input("ciao! hai un numero da darmi? se si, scrivi 'True' altrimenti 'False':  "))
numero =0
totale_numeri = 0
totale_cicli = 0

if risposta == "True" :
    #ciclowhile
    risposta_ciclo = "True"
    while risposta_ciclo == "True":
     numero = int(input("ehi dammi pure un numero: "))
     totale_numeri = numero + totale_numeri
     risposta_ciclo = str(input("hai un altro numero da darmi?:  "))
     totale_cicli = 1+ totale_cicli
else :
 totale_numeri= 0
 totale_cicli = 1

print ("la media dei tuoi numeri è " , totale_numeri/totale_cicli )
print (" grazie e arrivederci")
