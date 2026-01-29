from utente import Utente
from operazione import Operazione
from autore import Autore
from libro import Libro
from biblioteca import Biblioteca

l1 = Libro("Io sono l'abisso","978-8830453500","Donato Carrisi")
print(l1)
b1 = Biblioteca("Biblioteca1")
b1.aggiungi_libro(l1) # libro aggiunto
b1.aggiungi_libro(l1) # libro gia presente nel catalogo

u1 = Utente("Giulia")
b1.prestito(u1,l1) # libro preso in prestito