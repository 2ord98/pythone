#esercizio partita di tennis Sinner(1) vs Alcaraz(2)
punteggio_uno = 0
punteggio_due = 0

while punteggio_uno <= 40 and punteggio_due <= 40 :
    scambio= int(input("Stai tenendo il punteggio del match di tennis. Inserisci il numero 1, se vince lo scambio Sinner, 2 per Alcaraz: "))
    if scambio == 1 and punteggio_uno < 30 :
        punteggio_uno += 15
        print("Punteggio:" , punteggio_uno , "-" , punteggio_due)
    elif scambio == 1 and punteggio_uno == 30:
        punteggio_uno += 10
        print("Punteggio:" , punteggio_uno , "-" , punteggio_due)
    elif scambio == 1 and punteggio_uno == 40:
        print ("Vince il game Sinner")
        break   
    elif scambio == 2 and punteggio_due < 30 :
        punteggio_due += 15
        print("Punteggio:" , punteggio_uno , "-" , punteggio_due)
    elif scambio == 2 and punteggio_due == 30:
        punteggio_due += 10
        print("Punteggio:" , punteggio_uno , "-" , punteggio_due)
    elif scambio == 2 and punteggio_due == 40:
        print ("Vince il game Alcaraz")
        break 
    else: 
        print("Errore, inserisci un valore corretto")
    if punteggio_uno == 40 and punteggio_due == 40 :
        break

#siamo arrivati al tie break o 'vantaggi'
if punteggio_uno == punteggio_due == 40 :  
    print("Siamo al tie break ")
    while True :
        scambio = int(input("Inserisci il numero 1, se vince lo scambio dei Vantaggi, Sinner; 2 per Alcaraz: "))
        if scambio == 1 and punteggio_uno == 40 :
           punteggio_uno = "VANT"
           print("Punteggio:" , punteggio_uno , "-" , punteggio_due)
        elif scambio == 1 and punteggio_uno == "VANT" and punteggio_due == "VANT":
           punteggio_uno = "VANT"
           punteggio_due = 40
           print("Punteggio:" , punteggio_uno , "-" , punteggio_due)
        elif scambio == 1 and punteggio_uno == "VANT" :
           print ("Vince il game Sinner")
           break   
        elif scambio == 2 and punteggio_due == 40 :
           punteggio_due = "VANT"
           print("Punteggio:", punteggio_uno , "-" , punteggio_due )
        elif scambio == 2 and punteggio_uno == "VANT" and punteggio_due == "VANT":
           punteggio_uno = 40
           punteggio_due = "VANT"
           print("Punteggio:" , punteggio_uno , "-" , punteggio_due)
        else:
            print ("Vince il game Alcaraz")
            break
else:
    print("Prossimo Game")
