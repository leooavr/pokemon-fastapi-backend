<img src="">
# Pokemon FastAPI

## Bienvenido a mi backend simulando la captura de pokemons

En el proyecto actual se utilizaron las siguientes tecnologías:
```
Python 
FastAPI
MongoDB
```
## Pasos para la ejecución del proyecto
1. Clonamos el repositorio en alguna carpeta alojada en su ordenador
2. Ingresamos a la carpeta por medio de comandos y abrimos Visual Studio o cualquier editor de código
3. Desde consola creamos un entorno virtual, en mi caso utilizo **virtualenv**
4. En caso de no tener instalado virtualenv ejecutar
```
pip install virtualenv
```
5. Una vez instalado y alojados en la carpeta del proyecto creamos un entorno virtual
```
virtualenv <nombre_carpeta>
```
6. Veremos que en nuestro proyecto se creó una carpeta, entonces activamos el entorno ingresando a la siguiente ruta
```
\venv\Scripts\activate.ps1
```
7. Instalamos los requerimientos alojados en el .txt
```
pip install -r requirements.txt
```
8. Por ultimo ejecutamos 
```
python main.py
```
9. Ingresamos a http://localhost:8000/docs 
y ya con eso tenemos listos nuestros endpoints documentados 