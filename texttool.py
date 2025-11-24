#!/usr/bin/env python3

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
    """Main loop of the TextTool command-line program.

    Repeatedly prompts the user for a line, processes it with process_line,
    prints the result, and stops when an EOF (Ctrl+D / Ctrl+Z) is received.
    """
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
