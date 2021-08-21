<p align="center">
  <img src="https://i.ibb.co/Bj9hYK9/SESPlogo.png" alt="SESPlogo" border="0" width="250">
<br />
<br />

--------------------------------------------------------------------------------

<div align="center">
  <strong>Sistema de Entrada y Salida de Personas</strong>
</div>

<div align="center">
  Proyecto Institucional para la Olimpiada Nacional Virtual de Programación, Computación, Informática 2021
</div>

<br />

## Situación Problemática

Sistema para la gestión de las capacidades máximas de los espacios cerrados

# Instalacion

Para realizar la instalacion, SESP requiere de Python 3.8, Node.js 10.0+ y Arduino IDE

## Descarga de archivos de repositorio

Para descargar los archivos de este repositorio tendremos que ejecutar los siguientes comandos en terminal

```bash
git init

git clone https://github.com/cettipao/ecoinclusion.git
```

## Correr el backend

En SESP/, creamos un virtualenv de python y corremos

```bash
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate

python manage.py runserver
```

## Correr el frontend

En SESP/sesp-frontend/ corremos

```bash
npm install
npm start
```

# Built With

* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [Materialize](https://materializecss.com/)
* [React](https://es.reactjs.org/)

# License

Bajo el Colegio [ITS Villada](https://www.itsv.edu.ar/)

