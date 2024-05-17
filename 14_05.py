import random
import time

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.humor = random.randint(0, 100)  #Estado de ánimo inicial aleatorio
        self.historial_interacciones = Historial()  #Historial de interacciones

    def __str__(self):
        #Devuelve una representación legible de la persona con su estado de ánimo
        estado_emocional = 'triste 😢' if self.humor <= 35 else 'contento 😃' if self.humor >= 70 else 'neutral 😶'
        return f'{self.nombre}: Humor actual = {self.humor} ({estado_emocional})'

    def interactuar(self, otra_persona, comportamiento):
        #Registra la interacción en el historial y aplica el comportamiento
        self.historial_interacciones.agregar_interaccion(
            Interaccion(self, otra_persona, comportamiento)
        )
        self.aplicar_comportamiento(comportamiento)

    def aplicar_comportamiento(self, comportamiento):
        #Ajusta el estado de ánimo según el comportamiento recibido
        if comportamiento.nombre == 'Cariñoso':
            impacto = random.randint(1, 10)
        elif comportamiento.nombre == 'Insulto':
            impacto = -random.randint(1, 10)
        self.humor += impacto
        self.humor = max(0, min(100, self.humor))  #Asegura que el estado de ánimo esté dentro del rango [0, 100]

class Comportamiento:
    def __init__(self, nombre, frecuencia):
        self.nombre = nombre  #Nombre del comportamiento (Cariñoso o Insulto)
        self.frecuencia = frecuencia  #Frecuencia con la que ocurre este comportamiento

    def __str__(self):
        #Devuelve una representación legible del comportamiento
        return f"Comportamiento: {self.nombre}, Frecuencia: {self.frecuencia}"

class Interaccion:
    def __init__(self, persona_emisora, persona_objetivo, comportamiento):
        self.persona_emisora = persona_emisora  #Persona que emitió el comportamiento
        self.persona_objetivo = persona_objetivo  #Persona objetivo del comportamiento
        self.comportamiento = comportamiento  #Comportamiento aplicado

class Historial:
    def __init__(self):
        self.interacciones = []  #Lista para almacenar las interacciones

    def agregar_interaccion(self, interaccion):
        #Agrega una interacción al historial
        self.interacciones.append(interaccion)

    def mostrar_historial(self):
        #Imprime el historial de interacciones
        for interaccion in self.interacciones:
            print(f'{interaccion.persona_emisora.nombre} -> {interaccion.persona_objetivo.nombre}: {interaccion.comportamiento.nombre}')

def simular_tiempo(personas, duracion_simulacion):
    #Lista de comportamientos posibles con sus frecuencias
    comportamientos = [
        Comportamiento('Cariñoso', 3),
        Comportamiento('Insulto', 2)
    ]
    print("Estado inicial:")
    for persona in personas:
        print(persona)

    time.sleep(2)  #Simula un tiempo de espera antes de iniciar la simulación

    #Simula la interacción entre personas durante la duración especificada
    for _ in range(duracion_simulacion):
        for persona in personas:
            #Selecciona otra persona aleatoria para interactuar
            persona_random = random.choice([p for p in personas if p != persona])
            #Selecciona un comportamiento aleatorio
            comportamiento_persona = random.choice(comportamientos)
            #Interactúa con la otra persona aplicando el comportamiento seleccionado
            persona.interactuar(persona_random, comportamiento_persona)
            #Imprime información sobre la interacción
            if comportamiento_persona.nombre == 'Cariñoso':
                print(f"{persona.nombre} interactúa con {persona_random.nombre} y suma {random.randint(1, 10)} puntos de humor")
            elif comportamiento_persona.nombre == 'Insulto':
                print(f"{persona.nombre} interactúa con {persona_random.nombre} y resta {random.randint(1, 10)} puntos de humor")
        time.sleep(2)  #Simula un tiempo de espera entre cada iteración de interacción

if __name__ == '__main__':
    #Crea una lista de personas con nombres aleatorios y edades aleatorias entre 18 y 80 años
    personas = [
        Persona(nombre, random.randint(18, 80))
        for nombre in [
            'Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Francisco', 'Gerardo', 'Isabel', 'Jorge', 'Laura'
        ]
    ]

    #Inicia la simulación del tiempo con una duración de 5 iteraciones
    simular_tiempo(personas, 5)

    #Imprime el estado final de todas las personas después de la simulación
    print("\nEstado final:")
    for persona in personas:
        print(persona)
