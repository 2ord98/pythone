numero = float(input("dammi un mumero:  "))
totale_numeri = 0


while True:
    if numero == 0:  # Se l'utente inserisce 0, chiede un altro numero
        altronumero = float(input("Dammi un altro numero: "))
        if altronumero == 0:
            print("Hai inserito due zeri, quindi desideri uscire.")
            break  # Esce dal ciclo
        else:
            numero = altronumero  # Aggiorna numero per continuare
    totale_numeri += numero  # Somma il numero corrente
    numero = float(input("Dammi un altro numero: "))  # Chiede il prossimo numero
  
print("il totale dei numeri inseriti è:", totale_numeri)
  