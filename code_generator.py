import openai
import sys

# Configura tu clave de api de open ia
openai.api_key = "OPENIA_KEY"

def generate_reward_policy(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",  # Cambia a "gpt-4" si tienes acceso
            messages=[
                {"role": "system", "content": "Eres un asistente experto en aprendizaje por refuerzo."},
                {"role": "user", "content": prompt}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        print(f"Error al generar la política de recompensa: {e}")
        sys.exit(1)

# Ejemplo: Generar una política de recompensa para CartPole (ejemplo)
prompt = """
Genera una función de recompensa personalizada para el entorno CartPole-v1.
La función debe penalizar al agente si el ángulo del poste se aleja demasiado de la vertical,
y recompensarlo si mantiene el poste equilibrado durante más tiempo.
Proporciona SOLO el código Python de la función, sin explicaciones adicionales, ni si quiera los "```"
aparte tiene que tener un formato parecido a este(pero ojala sea mucho mejor):
def custom_reward(observation):
    angle = observation[2]  # El ángulo del poste
    reward = 1.0  # Recompensa base por estar en el paso de tiempo

    # Penalización si el ángulo se aleja de la vertical
    if abs(angle) > 0.2:  # umbral de ángulo
        reward -= 1.0  # penalización

    return reward
"""

custom_reward = generate_reward_policy(prompt)

# Guardar la política de recompensa en un archivo .py
file_name = "custom_reward.py"
with open(file_name, "w") as file:
    file.write(custom_reward)

print(f"Política de recompensa guardada en '{file_name}'")
