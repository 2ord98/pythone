class Message:
    def __init__ (self, destinatario = "", mittente = "", messaggio= ""):
        self._destinatario = destinatario
        self._mittente = mittente
        self._messaggio = messaggio
    def destinatario(self) :
     return self._destinatario
    def mittente(self) :
     return self._mittente
    def messaggio(self):
     return self._messaggio
    def append_riga(self, riga =""):
      self._messaggio += (" " + riga) if self._messaggio else riga   #Append riga
    def toString_riga(self):
      return (f"Da: {self._mittente} \n A: {self._destinatario} \n Messaggio: \n {self._messaggio}")
      

mess = Message("riccardo", "lorenzo" , "Ciao! riccardo sono Lorenzo e ti scrivo oggi,")
mess.append_riga("come stai?")
mess.append_riga("e sei andato ieri a bambini?")
print(mess.toString_riga())