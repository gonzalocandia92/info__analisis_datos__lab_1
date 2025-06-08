# Análisis de Datos 2025 - Entrega 1

Repositorio del curso de **Análisis de Datos**.

---

## 🎯 Objetivo

Desarrollar una aplicación modular en Python que permita:

- Cargar **al menos 2 tipos de archivos de datos** (`.csv`, `.xlsx`, `.json`, `.txt`, etc.)
- Realizar **validaciones básicas**
- Guardar los datos en una **base de datos relacional** utilizando **SQLAlchemy**
- Demostrar claramente los **cuatro pilares de la Programación Orientada a Objetos (POO)**
- Ejecutarse desde consola mediante una **clase principal**

---

## ✅ Requisitos Técnicos

### 🔹 Lenguaje y Paradigma

- **Lenguaje:** Python 3.10+
- **Paradigma:** Programación Orientada a Objetos (POO)

### 🔹 Manejo de Archivos

- Soporte para múltiples formatos: `.csv`, `.xlsx`, `.json`, `.txt`, etc.
- Carga automática desde el directorio `files/`

### 🔹 Validaciones

- Validación de **tipos de datos**: número, texto, fecha
- Validación de **campos obligatorios** (no nulos)
- Eliminación de **duplicados**
- Eliminación de **valores nulos**

### 🔹 Persistencia

- Uso de **SQLAlchemy** con `engine`
- Una tabla por cada archivo cargado

### 🔹 Flujo Esperado de la Aplicación

1. El usuario ejecuta `main.py`
2. El sistema carga automáticamente todos los archivos del directorio `files/`
3. Cada archivo es validado
4. Los datos se guardan en su tabla correspondiente en la base de datos
5. La aplicación finaliza indicando qué se cargó exitosamente y qué falló

---

## 🧱 Requisitos de POO

| Pilar           | Evaluación Esperada                                                                 |
|-----------------|--------------------------------------------------------------------------------------|
| **Abstracción**     | Separación clara entre lectura de archivos, validación y persistencia               |
| **Encapsulamiento** | Atributos y métodos privados o protegidos donde corresponda                        |
| **Herencia**        | Clases de modelo que heredan de una clase base (por ejemplo, `Base`)               |
| **Polimorfismo**    | Métodos redefinidos para manejar distintos formatos de archivo (`leer_csv`, etc.) |

---

