#esercizio sconto promozione

class Customer:
    def __init__(self, name):
        self.name = name
        self.total_spent = 0
        self.has_discount = False
    
    def makePurchase(self, amount):
        if amount <= 0:
            print("Errore! L'importo deve essere positivo.")
            return  # Esce senza registrare l'acquisto
        
        if self.has_discount:
            print(f"{self.name} ha usato uno sconto di $10.")
            amount -= 10  # Applica lo sconto
            self.has_discount = False  # Reset dello sconto dopo l'utilizzo

        print(f"{self.name} ha speso ${amount}.")
        self.total_spent += amount  # Registra la spesa effettiva
        
        # Controllo se il cliente ha raggiunto il limite per il nuovo sconto
        while self.total_spent >= 100:
            self.has_discount = True
            self.total_spent -= 100  # Sottrae la soglia per evitare accumuli errati
            print(f"{self.name} ha raggiunto i $100 spesi e ottiene uno sconto di $10 sul prossimo acquisto!")

    def discountReached(self):
        return self.has_discount

# Creazione del cliente
customer_name = input("Inserisci il nome del cliente: ")
cliente = Customer(customer_name)

# Ciclo per gestire acquisti multipli
while True:
    try:
        acquisto = float(input("Inserisci l'importo dell'acquisto: "))
        cliente.makePurchase(acquisto)
    except ValueError:
        print("Errore! Inserisci un numero valido.")
        continue

    # Chiediamo se vuole fare un altro acquisto
    desiderio = input("Vuoi fare un altro acquisto? (si/no): ").strip().lower()
    if desiderio == "no":
        print("Grazie per gli acquisti! Alla prossima.")
        break  # Esce dal ciclo se l'utente risponde "no"


##inizio programma di Collaudo.....

## a parte - test manuale Programma di collaudo di Lollo
#customer = Customer("Lorenzo")

# # Il cliente ottiene uno sconto dopo aver speso più di $100
#customer.makePurchase(50)
#customer.makePurchase(60)  #Ora ha diritto allo sconto

# # Usa lo sconto su un acquisto tra $90 e $100, senza guadagnare un altro sconto
#customer.makePurchase(95)  #Paga 85 dopo lo sconto

# # Un altro acquisto che porta a ottenere un secondo sconto
#customer.makePurchase(20)  #Non ottiene sconto qui
#customer.makePurchase(80)  #Ora raggiunge i $100 di spesa e ottiene un nuovo sconto

