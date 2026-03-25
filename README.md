# Práctica: Autómatas Finitos (AFD, AFN y AFN-λ)

## Alumnos
-López Toledo Kevin Antonio

-Hernández Ríos Cristian Sebastian

## Introducción

La presente práctica aborda la construcción, análisis e implementación de autómatas finitos como herramientas formales para el reconocimiento de lenguajes definidos sobre distintos alfabetos. Se consideran tres modelos fundamentales: Autómatas Finitos Deterministas (AFD), Autómatas Finitos No Deterministas (AFN) y Autómatas Finitos con transiciones λ (AFN-λ).

El desarrollo de la práctica permite estudiar el comportamiento de cada modelo, así como sus relaciones mediante procesos de conversión, particularmente de AFN y AFN-λ hacia AFD, apoyándose en el uso de la herramienta JFLAP.

---

## Objetivo

Implementar y analizar autómatas finitos que reconozcan lenguajes formales específicos, utilizando modelos deterministas y no deterministas, y comprender los mecanismos de construcción y conversión entre dichos modelos.

---

## Instrucciones de instalación y ejecución

### Requisitos

* Entorno de ejecución de Java (JRE o JDK)
* Software JFLAP

### Procedimiento

1. Clonar o descargar el repositorio:

   ```bash
   git clone <URL_DEL_REPOSITORIO>
   ```

2. Abrir el programa JFLAP.

3. Cargar un archivo de autómata:

   * Seleccionar **File → Open**
   * Abrir cualquier archivo con extensión `.jff`

4. Ejecutar pruebas de cadenas:

   * Utilizar **Input → Step** para ejecución paso a paso, o
   * **Input → Fast Run** para ejecución directa
   * Ingresar las cadenas a evaluar

---

## Descripción de los autómatas implementados

En el repositorio se incluyen implementaciones de:

* Autómatas Finitos Deterministas (AFD)
* Autómatas Finitos No Deterministas (AFN)
* Autómatas Finitos No Deterministas con transiciones λ (AFN-λ)

Los autómatas fueron diseñados para resolver problemas relacionados con:

* Reconocimiento de subcadenas
* Restricciones sobre prefijos y sufijos
* Condiciones de paridad y conteo de símbolos
* Validación de estructuras específicas en cadenas
* Combinación de condiciones mediante no determinismo

La descripción detallada de cada autómata, incluyendo su análisis, justificación del modelo, validación mediante ejemplos y recorridos de ejecución, se encuentra documentada en el archivo:

**`reporte.tex`**

Este documento constituye el reporte formal de la práctica.

---

## Estructura del repositorio

```
/automatas
    ├── afd/
    ├── afn/
    ├── afn_lambda/

reporte.tex
README.md
```

## Observaciones

* Todos los autómatas fueron diseñados y verificados mediante JFLAP.
* Se incluyen ejemplos de validación en el reporte para cada problema.
* Se aplicaron procesos de conversión de AFN y AFN-λ a AFD cuando fue requerido.
