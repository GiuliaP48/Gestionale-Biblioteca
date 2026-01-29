import random

class Utente:
    def __init__(self,nome):
        self.nome = nome
        self.numero_tessera = random.randint(10000000, 99999999)
        self.libri_in_prestito = []

    def __repr__(self):
        return f"Utente(Nome={self.nome},numerotessera={self.numero_tessera})"
    
    def __eq__(self,other):
        if not isinstance(self,other):
            return False
        return self.nome == other.nome and self.numero_tessera == other.numero_tessera