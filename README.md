# PEC4 - Liga de futbol 1995-2025

Autor: Xavier Soler Alonso

Este proyecto corresponde a la PEC4 de la asignatura Programacion para la ciencia de datos. El objetivo es analizar los resultados historicos de la Liga espanola de futbol entre 1995 y 2025 utilizando Python.

El proyecto carga un dataset de partidos, realiza analisis exploratorio, calcula estadisticas por equipo, genera graficas y construye un grafo de enfrentamientos entre los equipos con mayor puntuacion historica.

## Estructura del proyecto

```text
PEC4/
|-- src/
|   |-- main.py
|   |-- data/
|   |   `-- LaLiga_Matches.csv
|   |-- exercises/
|   |   |-- ex1.py
|   |   |-- ex2.py
|   |   |-- ex3.py
|   |   |-- ex4.py
|   |   |-- ex5.py
|   |   |-- ex6.py
|   |   `-- ex7.py
|   `-- img/
|-- tests/
|-- doc/
|-- screenshots/
|-- config.py
|-- requirements.txt
|-- README.md
`-- LICENSE
```

## Instalacion

Desde la carpeta raiz del proyecto, crear un entorno virtual:

```bash
python -m venv .venv
```

Activar el entorno virtual en Windows:

```bash
.venv\Scripts\activate
```

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

## Ejecucion del proyecto

El fichero principal es `src/main.py`. Se ejecuta desde la carpeta raiz del proyecto.

Mostrar la ayuda:

```bash
python -m src.main -h
```

Ejecutar hasta un ejercicio concreto:

```bash
python -m src.main -ex 1
python -m src.main -ex 5
python -m src.main -ex 7
```

El argumento `-ex` ejecuta los ejercicios de forma incremental. Por ejemplo, `-ex 5` ejecuta los ejercicios del 1 al 5.

Las graficas generadas se guardan en la carpeta:

```text
src/img/
```

## Linting

Para comprobar el estilo del codigo con pylint:

```bash
pip install pylint
python -m pylint src tests
```

El objetivo es revisar posibles errores de estilo, imports no utilizados y aspectos de calidad del codigo.

## Documentacion

La documentacion puede generarse con `pydoc`. Desde la raiz del proyecto:

```bash
python -m pydoc -w src.main src.exercises.ex1 src.exercises.ex2 src.exercises.ex3 src.exercises.ex4 src.exercises.ex5 src.exercises.ex6 src.exercises.ex7
```

Despues, mover los ficheros `.html` generados a la carpeta:

```text
doc/
```

## Tests

Los tests se ejecutan con la libreria estandar `unittest`:

```bash
python -m unittest tests.tests_ex6
```

El test principal solicitado en la PEC comprueba la funcion `fun_total_goals` del ejercicio 6.

## Git y GitHub

Inicializar el repositorio:

```bash
git init
git add .
git commit -m "Version inicial del proyecto PEC4"
```

Crear un repositorio en GitHub y asociarlo al proyecto:

```bash
git remote add origin URL_DEL_REPOSITORIO
git branch -M main
git push -u origin main
```

Para guardar cambios posteriores:

```bash
git add .
git commit -m "Actualiza ejercicios de la PEC4"
git push
```

## Notas de entrega

Antes de entregar el proyecto en formato zip, no se deben incluir carpetas de entorno virtual como `.venv/` ni carpetas de cache como `__pycache__/`.

Tambien se recomienda dejar en `src/img/` solo las graficas finales necesarias para la entrega.
