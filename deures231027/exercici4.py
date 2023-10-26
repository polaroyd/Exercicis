numero_secret = 42

try:
    intenta = int(input("Intenta adivinar el nombre secret: "))

    if intenta == numero_secret:
        print("¡Felicitats! Has adivinat el nombre secret.")
    else:
        print(f"Llàstima, el nombre secreto es {numero_secret}. ¡Intenta-ho de nou!")
except ValueError:
    print(" Ingresa un nombre enter vàlid.")
