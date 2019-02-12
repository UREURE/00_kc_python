# KC_EJ10
# Crear un programa que reciba un número del 1 al 7 y
# muestre el nombre de la película StarWars correspondiente.
# Ejemplo
# >>Entrada: 5 (o bien V)
# >>Salida: StarWars V - El imperio contraataca.

peliculas = ("StarWars Episodio I - La amenaza fantasma",
             "StarWars Episodio II - El ataque de los clones",
             "StarWars Episodio III - La venganza de los Sith",
             "StarWars Episodio IV - Una nueva esperanza",
             "StarWars Episodio V - El Imperio contraataca",
             "StarWars Episodio VI - El retorno del Jedi",
             "StarWars Episodio VII - El despertar de la Fuerza")

dicc = {"1": peliculas[0], "I": peliculas[0],
        "2": peliculas[1], "II": peliculas[1],
        "3": peliculas[2], "III": peliculas[2],
        "4": peliculas[3], "IV": peliculas[3],
        "5": peliculas[4], "V": peliculas[4],
        "6": peliculas[5], "VI": peliculas[5],
        "7": peliculas[6], "VII": peliculas[6]}

pelicula = ""
while not pelicula in dicc:
    pelicula = input(
        "Introduzca el número de la película (1..7 ó I..VII): ").upper()
    if not pelicula in dicc:
        print("Número de película no válido, debe estar entre 1..7 ó I..VII.")

print(f"Película: {dicc[pelicula]}.")
