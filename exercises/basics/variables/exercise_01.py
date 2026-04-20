"""
Esercizio: Gestione Variabili

Descrizione:
    Crea variabili di diversi tipi e stampale

Requisiti:
    - Crea una stringa, un intero, un float e un booleano
    - Stampa il tipo di ogni variabile
"""

def main():
    """Funzione principale dell'esercizio."""
    # Il tuo codice qui
    nome = "Mario"
    eta = 25
    altezza = 1.75
    studente = True
    
    print(f"Nome: {nome} (tipo: {type(nome).__name__})")
    print(f"Eta: {eta} (tipo: {type(eta).__name__})")
    print(f"Altezza: {altezza} (tipo: {type(altezza).__name__})")
    print(f"Studente: {studente} (tipo: {type(studente).__name__})")


if __name__ == "__main__":
    main()
