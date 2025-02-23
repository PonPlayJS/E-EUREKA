import gymnasium as gym
from stable_baselines3 import PPO

# Cargar el modelo desde la ubicación (puedes cambiarla)
model_path = "/home/joaco/Escritorio/vscode/cartpole_ppo"
model = PPO.load(model_path)

# "crea" el render
env = gym.make("CartPole-v1", render_mode="human")
observation, info = env.reset()

# Ejecutar política aprendida
for _ in range(1000):
    action, _ = model.predict(observation)
    observation, reward, terminated, truncated, info = env.step(action)
    
    if terminated or truncated:
        observation, info = env.reset()

env.close()