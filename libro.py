class Libro:
    def __init__(self,titolo,codice_isbn,autore):
        self.titolo = titolo
        self.codice_isbn = codice_isbn
        self.autore = autore

    def __repr__(self):
        return f"Libro(Titotlo={self.titolo},Codice ISBN={self.codice_isbn},Autore={self.autore})"
    
    def __eq__(self, other):
        if not isinstance(self,other):
            return False
        return self.titolo == other.titolo and self.codice_isbn == other.codice_isbn and self.autore == other.autore
