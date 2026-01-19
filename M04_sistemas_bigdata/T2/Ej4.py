canciones = [
    {
        "titulo": "Imagine",
        "genero": "Pop",
        "duracion": 4,
        "calificacion": 4.8
    },
    {
        "titulo": "Bohemian Rhapsody",
        "genero": "Rock",
        "duracion": 6,
        "calificacion": 4.9
    },
    {
        "titulo": "Billie Jean",
        "genero": "Pop",
        "duracion": 5,
        "calificacion": 4.7
    },
    {
        "titulo": "Smells Like Teen Spirit",
        "genero": "Rock",
        "duracion": 5,
        "calificacion": 4.6
    }
]

for cancion in canciones:
    if (cancion["genero"] == "Rock" or cancion["genero"] == "Pop") and cancion["duracion"] <= 5 and cancion["calificacion"] >= 4:
        print(cancion["titulo"])
        