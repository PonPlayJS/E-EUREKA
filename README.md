# M-Eureka
Eureka simplified
Ubuntu 24.04

## requisitos
* pip
* miniconda
* api de OpenIA
## crear entorno virtual conda
```
conda create --name ekmini python=3.10
conda activate ekmini # puedes desactivarlo con "conda deativate"
```

## dependencias
```
pip install gym stable-baselines3 
pip3 install openai==0.28
pip install gym[classic_control]
conda install numpy=1.23.5
pip install 'shimmy>=2.0'
```

## clonar repo e ir a la carpeta
```
git clone https://github.com/PonPlayJS/M-Eureka
cd M-Eureka
```

## importante
- Luego de todo eso, abre algun editor de codigo y ve a la carpeta M-Eureka
- ahora ve a "code_generator.py" y donde pone "OPENIA_KEY" 
- inserta entre las comillas tu clave de api de OpenIA luego de eso, puedes ejecutar "orden.sh" con el siguiente comando en la terminal

```
chmod +x orden.sh
./orden.sh
```
