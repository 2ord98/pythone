#apertura file
import os  #importa il modulo os per trovare se file esiste o no nel sistema operativo

nomeFile = input ("metti il nome del file:  ")
if os.path.exists(nomeFile):
 with open (f"{nomeFile}" , "r") as infile:
    rows = infile.readlines() 
    for line in reversed(rows):  
        inversa = line.strip()[::-1]  # Rimuove gli spazi e inverte la riga
        print(inversa)
else:
   print("File non trovato")

#stampa
