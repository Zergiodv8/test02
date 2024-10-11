from flask import Flask, jsonify
import random

app = Flask(__name__)

# Listas de posibles excusas
excusa_motivos = [
    "llevar a mi hija a una pijamada",
    "acompañar a mi señora a lo de su amiga",
    "ir a una reunión familiar",
    "llevar el auto al taller",
    "ayudar a mi vecino con una mudanza",
    "terminar un trabajo urgente",
    "cuidar a mi mascota enferma",
    "ir al médico porque no me siento bien",
    "ayudar a mi suegra con algunas tareas",
    "recoger a los chicos de la escuela",
    "ir a una cena de negocios",
    "hacer una llamada importante de trabajo",
    "llevar a mi abuela al médico",
    "hacer una compra grande para la casa",
    "asistir a una cita con el dentista"
]

excusa_final = [
    "lo lamento mucho, ¡pero la próxima vez seguro me sumo!",
    "¡me encantaría ir, pero no puedo dejar esto pendiente!",
    "¡espero que lo pasen genial, lo compenso en la próxima salida!",
    "es una lástima, ¡pero la próxima estoy ahí sin falta!",
    "ojalá pudiera, ¡pero estaré ocupado con eso!"
]

# Función que genera una excusa aleatoria
def generar_excusa():
    motivo = random.choice(excusa_motivos)
    cierre = random.choice(excusa_final)
    return f"No puedo ir porque tengo que {motivo}, {cierre}"

@app.route('/')
def home():
    return jsonify({"excusa": generar_excusa()})

if __name__ == "__main__":
    app.run(debug=True)
