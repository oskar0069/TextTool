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

    # 🌟 Commande ajoutée par l'utilisateur A (Exercice 3)
    # length → renvoie la longueur de text
    if cmd == "length":
        return str(len(text))

    return "Unknown command " + cmd


def main():
    while True:
        try:
            line = input("commande> ")
        except EOFError:
            break

        print(process_line(line))


if __name__ == "__main__":
    main()
