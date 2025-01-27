#rifatto per il prof
totale_numeri = 0
totale_cicli = 0
numero = "poldo"  # Inizializza con un valore che non è "fine" per iniziare il ciclo

# Ciclo while
while numero != "fine":
    numero = input("Ehi, dammi pure un numero (o 'fine' per terminare): ")

    if numero == "fine":
        break  # Esce dal ciclo quando l'utente scrive "fine"
    
    else :
        totale_numeri += int(numero)  # Converte l'input in un numero intero e aggiunge al totale
        totale_cicli += 1  # Incrementa il conteggio dei numeri inseriti
    
print ("la media dei tuoi numeri è " , totale_numeri/totale_cicli )
print (" grazie e arrivederci")
