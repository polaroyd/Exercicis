
def cub(numero):
    return numero ** 3

try:
    numero_enter = int(input("Ingresa un número enter: "))
    
    resultat = cub(numero_enter)
    
    print(f"El cub de {numero_enter} es {resultat}")
except ValueError:
    print("Por favor, ingresa un número entero válido.")
