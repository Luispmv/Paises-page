# Paises-Page
En este proyecto tomaremos un csv con la informacion de paises y lo convertiremos a una pagina web.

![App Screenshot](https://i.imgur.com/m9p3Xrg.png)

***
## Corre el proyecto en tu maquina

Clone the project

```bash
  git clone https://github.com/Luispmv/Paises-page.git
```

Dirigete al directorio del proyecto

```bash
  cd proyecto
```

Una vez ubicado en el proyecto crea un nuevo entorno virtual
```bash
  python3 -m venv env
```

Activa tu nuevo entorno virtual
```bash
  source env/bin/activate
```

Verifica que python y pip corran desde tu proyecto
```bash
  which python3
  which pip3
```

Verifica el archivo requirements.txt

```bash
  cat requirements.txt
```

Instala las dependencias del proyecto

```bash
  pip install -r requirements.txt
```

Una vez instalamos las dependencias corremos nuestro servidor FastAPI
```bash
  uvicorn main:app --reload
```

Para poder ver la informacion de un pais en especifco nos dirigimos a main.py y cambiamos la variable country por el pais cuyos datos querramos ver:
```python
#main.py

country = "Mexico" # Cambia el nombre del pais al de tu preferencia y ve los cambios reflejados
```

***
## Corriendo el proyecto en un contendor Docker

Con los archivos Dockerfile y docker-compose.yml creados lo que haremos sera ejcutar los siguientes comandos para montar nuestro contenedor

```bash
  docker-compose build
```
```bash
  docker-compose up -d
```
```bash
  docker-compose ps
```

Una vez corremos los comandos anteriores tenemos nuestro contenedor montado.

***
## Manejando cambios en un contenedor Docker

En el archivo docker-compose.yml tenemos la instruccion volumes, esta nos permite actualizar nuestro contenedor a los cambios que hagamos en proyecto.
Sabiendo esto para poder ver reflejado en el servidor FastAPI los cambios que hagamos corremos los siguientes comandos:

```bash
  docker-compose restart
```
```bash
  docker-compose exec paises bash
```

o tambien puedes correr solamente
```bash
  docker-compose restart
```

Al dirigirte a localhost en tu navegador veras los cambios reflejados
