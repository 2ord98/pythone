#esercizio rifatto per il prof 
voti =[]

# Apro il file
with open("/Users/lorenzocassiani/Desktop/corso.py/elenco.voti.txt", "r") as file:
    voto = file.readline().strip()  #dichiaro variabile voto
    while voto != "fine" and voto != "":  #Continua fino a che non trova "fine" o una riga vuota
        if voto.isdigit():  # Controlla se il voto è valido , se non è numero scarta dall'array
            voti.append(float(voto))
        else:
            print("Il voto non è valido")  

        voto = file.readline().strip()  #cicla la lettura di ogni riga del file
            

valore_min = min(voti)
voti.remove(valore_min)  # Rimuovo il valore minimo
valore_max = max(voti)
voti.remove(valore_max)  # Rimuovo il valore massimo

media = sum(voti) / len(voti)  # Calcolo la media
print(f"La media dei tuoi voti (escludendo il minimo e il massimo voto) è: {media:.2f}")
