#!/usr/bin/env python3

"""Simple command-line tool to apply text transformations to a line of text.

This module reads commands such as 'uppercase', 'lowercase' (and others
implemented in the exercises) and applies them to the given text.
"""

def process_line(line):
    ...




def process_line(line):
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

<<<<<<< HEAD
    # 🌟 Commande ajoutée par l'utilisateur C (Exercice 3)
    # prefix → renvoie les 10 premiers caractères du texte
    if cmd == "prefix":
        return text[:10]

    return "Unknown command " + cmd

=======
    # 🌟 Commande ajoutée par l'utilisateur A (Exercice 3)
    # length → renvoie la longueur de text
    if cmd == "length":
        return str(len(text))
>>>>>>> B/master

def main():
    while True:
        try:
            line = input("commande> ")
        except EOFError:
            break

        print(process_line(line))

<<<<<<< HEAD

=======
>>>>>>> B/master
if __name__ == "__main__":
    main()
