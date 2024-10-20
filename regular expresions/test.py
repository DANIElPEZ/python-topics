# Preguntas
preguntas = [
    "¿Te gusta trabajar en equipo?",
    "¿Disfrutas resolviendo problemas complejos?",
    "¿Eres creativo y te gusta proponer nuevas ideas?",
    "¿Te interesa el análisis de datos y estadísticas?",
    "¿Eres bueno comunicándote oralmente y por escrito?",
    "¿Prefieres trabajar en un ambiente estructurado y organizado?",
    "¿Te gusta liderar y tomar decisiones?",
    "¿Disfrutas aprender cosas nuevas constantemente?",
    "¿Eres hábil en el manejo de herramientas tecnológicas?",
    "¿Te sientes cómodo trabajando bajo presión?",
]

# Carreras y sus criterios
carreras = {
    "Ingeniería": [4, 4, 2, 3, 1, 2, 2, 3, 4, 3],
    "Medicina": [4, 4, 1, 2, 5, 4, 3, 4, 3, 5],
    "Derecho": [3, 3, 3, 2, 5, 4, 5, 3, 3, 4],
    "Arquitectura": [3, 3, 4, 2, 2, 3, 2, 4, 3, 3],
    "Psicología": [4, 4, 4, 3, 4, 4, 3, 4, 3, 4],
    "Marketing": [3, 3, 4, 3, 4, 3, 4, 4, 3, 4],
    "Informática": [4, 4, 3, 4, 3, 3, 2, 4, 5, 4],
    "Administración de Empresas": [3, 3, 3, 3, 4, 4, 5, 3, 3, 4],
    "Diseño Gráfico": [4, 3, 5, 3, 3, 3, 2, 4, 3, 3],
    "Contabilidad": [3, 3, 3, 2, 4, 4, 3, 3, 3, 4],
}

# Función para calcular la carrera
def calcular_carrera(respuestas_usuario):
    puntajes = {}

    for pregunta_index in range(len(respuestas_usuario)):
        respuesta = respuestas_usuario[pregunta_index]
        pregunta = preguntas[pregunta_index]
        
        for carrera in carreras:
            if carrera not in puntajes:
                puntajes[carrera] = 0

            puntajes[carrera] += carreras[carrera][pregunta_index] * respuesta

    carrera_final = max(puntajes, key=puntajes.get)
    return carrera_final

# Obtener respuestas del usuario
respuestas_usuario = []
for i, pregunta in enumerate(preguntas):
    respuesta = int(input(f"{pregunta} (1: Totalmente en desacuerdo, 2: En desacuerdo, 3: Neutral, 4: De acuerdo, 5: Totalmente de acuerdo): "))
    respuestas_usuario.append(respuesta)

# Calcular carrera recomendada
carrera = calcular_carrera(respuestas_usuario)
print("Carrera recomendada:", carrera)
