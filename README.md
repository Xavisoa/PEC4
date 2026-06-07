# PEC4 - Liga de futbol 1995-2025

Autor: Xavier Soler Alonso

## Estructura del proyecto

La estructura del proyecto es:

En la carpeta `src/exercises/` están las funciones de cada ejercicio.

El archivo `src/main.py` es el que ejecuta los ejercicios.

Las imagenes se guardan en `src/img/`.

## Instalacion

Primero se puede crear un entorno virtual:

```bash
python -m venv .venv
```

Despues se instalan las librerias necesarias:

```bash
pip install -r requirements.txt
```

## Ejecucion

El proyecto se ejecuta desde la carpeta raiz.

Para ver la ayuda:

```bash
python -m src.main -h
```

Para ejecutar los ejercicios:

```bash
python -m src.main -ex 1
python -m src.main -ex 2
python -m src.main -ex 3
python -m src.main -ex 4
python -m src.main -ex 5
python -m src.main -ex 6
python -m src.main -ex 7
```

El argumento `-ex` indica hasta que ejercicio se quiere ejecutar. Por ejemplo, `-ex 5` ejecuta del ejercicio 1 al 5.

## Linting

Para comprobar el codigo con pylint:

```bash
pip install pylint
python -m pylint src tests
```

## Documentacion

La documentacion se puede generar con `pydoc`:

```bash
python -m pydoc -w src.main src.exercises.ex1 src.exercises.ex2 src.exercises.ex3 src.exercises.ex4 src.exercises.ex5 src.exercises.ex6 src.exercises.ex7
```

Los archivos generados se guardan o se mueven a la carpeta `doc/`.

## Tests

El test del ejercicio 6 se ejecuta con:

```bash
python -m unittest tests.tests_ex6
```

Este test comprueba la función `fun_total_goals`.

## requitements.txt

Librerias necesarias para la ejecución del proyecto:
- pandas
- matplotlib
- networkx

## LICENCE

Este proyecto se distribuye bajo la licencia MIT.

## Git y GitHub

Comandos basicos para guardar el proyecto con Git:

```bash
git init
git add .
git commit -m "Primer commit PEC4"
```

Para subirlo a GitHub:

```bash
git remote add origin URL_DEL_REPOSITORIO
git branch -M main
git push -u origin main
```
