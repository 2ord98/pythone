#esercizio corretto
class Message:
    def __init__ (self, destinatario, mittente):
      self._destinatario = destinatario
      self._mittente = mittente
      self._messaggio = [] #oppure self._messaggio = []
    def destinatario(self) :
      return self._destinatario
    def mittente(self) :
      return self._mittente
    def messaggio(self):
      return self._messaggio
    def append(self, riga):
      self._messaggio.append(riga) #Append riga oppure questo metodo
    def toString(self):
      messaggio_formattato = " ".join(self._messaggio)
      print (f"Da:{self._mittente}\nA:{self._destinatario}\nMessaggio:\n{messaggio_formattato}")

mess = Message("riccardo", "lorenzo")
mess.append("Ciao, come stai?")
mess.append("e sei andato ieri a funghi?")
mess.toString()
