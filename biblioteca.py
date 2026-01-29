class Biblioteca:
    def __init__(self,nome):
        self.nome = nome
        self.catalogo = []

    def __repr__(self):
        return f"Biblioteca(Nome={self.nome})"
    
    def __eq__(self, other):
        if not isinstance(self,other):
            return False
        return self.nome == other.nome
    
    def aggiungi_libro(self,libro):
        if libro in self.catalogo:
            print("Il libro è già stato aggiunto nel catalogo")
            return False 
        else:
            self.catalogo.append(libro)
            print("Il libro è stato aggiunto")
            return True

    # risolvere bug
    def prestito(self,utente,libro):
        if libro in self.catalogo and (len(utente.libri_in_prestito) < 3):
            utente.libri_in_prestito.append(libro)
            print("Il libro è stato preso in prestito")
            return self.catalogo.remove(libro)
        print("Massima disponibilità prestito raggiunta!")
        return False
    
    # risolvere bug
    def restituzione(self,libro,utente):
        if libro in utente.libri_in_prestito:
            utente.libri_in_prestito.remove(libro)
            self.catalogo.append(libro)
            return True
        return False
