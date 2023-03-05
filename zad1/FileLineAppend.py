file = input("Podaj nazwę pliku: ")

with open(file, "a") as f:
    text = input("Podaj ciąg znaków: ")
    f.write("\n" + text)