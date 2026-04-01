# series de preguntas


preguntas = [
    ("¿Cuál es la capital de Francia?", ["A) Madrid", "B) París", "C) Roma"], "B"),
    ("¿Cuánto es 5 x 3?", ["A) 15", "B) 20", "C) 10"], "A"),
    ("¿Qué lenguaje estamos usando?", ["A) c++", "B) java", "C) python"], "B"),
    ("¿ cual es el planeta mas cercano al sol ?", ["A) venus" ,"B) mercurio", "c) marte"], "B"),
    ("¿ caul es el mejor centro superate ?" , ["A) superate chorrera ", " B) superate chiriqui ", "C) superate colon"], "C"),
    ("¿ para que sirve superate ?" , ["A) para aprender a programar ", "B) para aprender a bailar ", "C) para aprender a cocinar"] , "A"),
    ("¿ cual es el mejor teacher de superate ?" , ["A) teacher cristel ", "B) teacher vernice ", "C) teacher vladi"] , "C"),
]

# diccionario
resultados = {
    "correctas": 0,
    "incorrectas": 0
}

# Programa l
print("Bienvenido al juego de preguntas!\n")

for pregunta, opciones, respuesta_correcta in preguntas:
    print(pregunta)
    for opcion in opciones:
        print(opcion)
    
    respuesta_usuario = input("Tu respuesta: ").upper()
    
    if respuesta_usuario == respuesta_correcta:
        print(" Correcto!\n")
        resultados["correctas"] += 1
    else:
        print(" Incorrecto!\n")
        resultados["incorrectas"] += 1

# Mostrar resultados finales
print("Resultados finales:")
print(f"Respuestas correctas: {resultados['correctas']}")
print(f"Respuestas incorrectas: {resultados['incorrectas']}")