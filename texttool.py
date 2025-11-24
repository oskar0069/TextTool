#!/usr/bin/env python3

def process_line(line):
    """
    Analyse la ligne entrée par l’utilisateur : extrait la commande,
    sépare le texte associé et exécute l’opération demandée
    (uppercase, lowercase, count-words, length, etc.).
    Retourne le résultat sous forme de chaîne de caractères.
    """
    if " " not in line:
        return "No command or no argument given"

    cmd, text = line.split(" ", maxsplit=1)

    # Commandes existantes
    if cmd == "uppercase":
        return text.upper()
    if cmd == "lowercase":
        return text.lower()
    if cmd == "count-words":            # ← TA NOUVELLE COMMANDE
        return len(text.split())

    # 🌟 Commande ajoutée par l'utilisateur A (Exercice 3)
    # length → renvoie la longueur de text
    if cmd == "length":
        return str(len(text))

def main():
    while True:
        try:
            line = input("commande> ")
        except EOFError:
            break

        print(process_line(line))

if __name__ == "__main__":
    main()
