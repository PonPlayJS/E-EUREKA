from stable_baselines3 import PPO
from int_gym import CustomCartPoleEnv # Importa el entorno personalizado
import numpy as np

# Crear el entorno personalizado
env = CustomCartPoleEnv()
# Crear el modelo con una política personalizada
model = PPO(
    "MlpPolicy", 
    env, 
    verbose=1, 
    policy_kwargs={"net_arch": [64, 64]}  # Puedes, cuando quieras, no te apures, puedes personalisar la red neuronal
)
# Entrenar el modelo :c
print("Entrenando agente...")
model.learn(total_timesteps=50000)

# Probar el modelo :D
print("Probando el agente entrenado...")
obs = env.reset()  # Resetear en ambiente (literamente)

if isinstance(obs, tuple):  # Si devuelve observation, info (solo esos)
    obs, _ = obs

for _ in range(1000):
    action, _states = model.predict(obs)
    obs, rewards, done, info = env.step(action)  
    
    # Renderizar el entorno >:c
    env.render()
    
    if done:
        obs = env.reset()  # Reiniciar el entorno si el episodio termina
        
        # Manejar el retorno de reset() para versiones modernas de Gym (hay nuevas pesas)
        if isinstance(obs, tuple):
            obs, _ = obs

# guarda el fukin modelo
model.save("/home/joaco/Escritorio/vscode/cartpole_ppo")

env.close()  # Cerrar el entorno >:D
