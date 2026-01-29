import datetime

class Operazione:
    def __init__(self,tipo):
        self.tipo = tipo
        self.data = datetime.now()

    def __repr__(self):
        return f"Operazione(Tipo={self.tipo},Data={self.data})"
    
    def __eq__(self,other):
        if not isinstance(self,other):
            return False
        return self.tipo == other.tipo and self.data == other.data