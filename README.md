# M-Eureka 
- Pre-prototipo
- Eureka simplified (https://eureka-research.github.io/)
- Ubuntu 24.04

## Requisitos
* pip
* miniconda
* api de OpenIA
## Crear entorno virtual conda
```
conda create --name ekmini python=3.10
conda activate ekmini # puedes desactivarlo con "conda deativate"
```

## Dependencias
```
pip install gym stable-baselines3 
pip3 install openai==0.28
pip install gym[classic_control]
pip3 install numpy==1.23.1
pip install 'shimmy>=2.0'
```

## Clonar repo e ir a la carpeta
```
git clone https://github.com/PonPlayJS/M-Eureka
cd M-Eureka
```

## Importante
- Luego de todo lo anterior, abre algún editor de código, dirigete a la carpeta M-Eureka
- Ahora ve a "code_generator.py", donde dice "OPENIA_KEY" allí pon tu clave de OpenIA
- Al mismo tiempo, ve al archivo traning.py y modifica entre las comillas "USER_PATH"
- Específica donde quieres que los videos se guarden
```        #Modifica aca
model.save("USER_PATH")
```
- Inserta entre las comillas tu clave de api de OpenIA luego de eso, puedes ejecutar "orden.sh" con el siguiente comando en la terminal

```
chmod +x orden.sh
./orden.sh
```

## Para ver tus simulaciones
```
cd [USER_PATH]
python view.py
```
![imagen](https://github.com/user-attachments/assets/c899c84a-e098-45e2-9579-eec26a2d510d)
