# Demanar que el primer jugador escolleixi la seva jugada
jugador1 = input("Jugador 1, escolleix pedra, paper o tisora: ").lower()

# Demanar que el segon jugador escolleixi la seva jugada
jugador2 = input("Jugador 2, escolleix pedra, paper o tisora: ").lower()

# Comprobar qui ha guanyat
if jugador1 == jugador2:
    print("Empate", jugador1)
elif (jugador1 == "pedra" and jugador2 == "tisores") or (jugador1 == "paper" and jugador2 == "pedra") or (jugador1 == "tisores" and jugador2 == "papel"):
    print("¡Jugador 1 ha guanyat! {} guanya a {}".format(jugador1, jugador2))
else:
    print("¡Jugador 2 ha guanyat! {} guanya a {}".format(jugador2, jugador1))
