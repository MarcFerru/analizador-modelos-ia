# Analizador de modelos de IA

## Descripción

Este proyecto consiste en una aplicación sencilla en Python que permite cargar, analizar y comparar resultados de distintos modelos de inteligencia artificial.

El objetivo principal del proyecto es simular un entorno de desarrollo colaborativo utilizando Git y GitHub. Para ello, el equipo trabaja mediante ramas de funcionalidad, commits significativos, pull requests, revisiones de código y resolución de conflictos de integración.

## Funcionalidades principales

* Lectura de resultados desde ficheros CSV.
* Lectura de resultados desde ficheros JSON.
* Análisis de modelos según su score.
* Obtención del mejor modelo.
* Cálculo del score medio.
* Filtrado de modelos por tipo.
* Menú básico por consola.
* Pruebas automáticas sencillas.

## Estructura del proyecto

```text
analizador-modelos-ia/
│
├── main.py
├── modelo.py
├── lector_csv.py
├── lector_json.py
├── analisis.py
│
├── datos/
│   ├── resultados.csv
│   └── resultados.json
│
├── tests/
│   └── test_analisis.py
│
├── README.md
└── .gitignore
```

## Flujo de trabajo colaborativo

El equipo utiliza un flujo de trabajo basado en ramas de funcionalidad:

* `feature/lectura-datos`
* `feature/analisis-resultados`
* `feature/menu-tests-documentacion`

Cada integrante trabaja en una rama distinta, realiza commits significativos y abre un pull request para integrar sus cambios en la rama `main`.

Antes de fusionar cada pull request, el código es revisado por otros integrantes del grupo mediante comentarios, sugerencias de mejora y aprobación o solicitud de cambios.

## Integrantes y responsabilidades

| Integrante     | Rama                               | Responsabilidad                         |
| -------------- | ---------------------------------- | --------------------------------------- |
| Marc Ferrer    | `feature/lectura-datos`            | Lectura de CSV, JSON y datos de ejemplo |
| Mauro Tognetti | `feature/analisis-resultados`      | Funciones de análisis de modelos        |
| Elena C        | `feature/menu-tests-documentacion` | Menú, pruebas y documentación           |

## Ejecución del proyecto

Para ejecutar el programa principal:

```bash
python main.py
```

Para ejecutar las pruebas:

```bash
python -m unittest discover tests
```

## Objetivo académico

Este repositorio forma parte de una actividad evaluable sobre trabajo colaborativo con Git. El propósito es aplicar un flujo completo de colaboración usando repositorio remoto, ramas, commits, pull requests, revisión de código y resolución de conflictos.
ón de conflictos.
