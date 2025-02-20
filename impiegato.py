#ereditarietà di oggetti
class Employee :
    def __init__(self , nome , cognome, salario) :
        self._nome = nome
        self._cognome = cognome
        self._salary = salario
    def setName (self,nome):
        self._nome = nome
    def setSurname (self,cognome):
        self._cognome = cognome
    def setSalary (self,salario):
        self._salario = salario
    #def __repr__(self):
        #return (f"L'Employee {self._nome} {self._cognome} ha come salario {self._salary} euro ")

class Manager (Employee) :
    def __init__(self, nome , cognome , salario, repartoGestito) :
        super().__init__(nome,cognome, salario) #per fare riferimento alla classe padre
        self._repartoGestito = repartoGestito
    def __repr__(self):
        return (f"Il Manager {self._nome} {self._cognome} ha come salario {self._salary} euro e lavora nel reparto {self._repartoGestito}")
    
riccardo = Manager("Riccardo","Tamatti", 2000, "IT security")
print(riccardo)
