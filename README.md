# Proyecto de Procesamiento de Encuestas - ADA I

## 📋 Descripción del Proyecto

Este proyecto implementa **dos soluciones algorítmicas diferentes** para el procesamiento y análisis de una gran encuesta divida por temas y preguntas, desarrollado como parte del curso **Análisis y Diseño de Algoritmos I** de la Universidad del Valle.

### Problema Principal

Una consultoría de datos necesita analizar los resultados de una encuesta organizada jerárquicamente para identificar temas con opiniones más favorables y generar análisis estadísticos detallados.

### Características de la Encuesta

- **K temas**, cada uno con un nombre específico
- **M preguntas** por tema
- **Nmin a Nmax encuestados** por pregunta (cada persona responde solo una pregunta)
- **Encuestados** con: ID, nombre, nivel de experticia (0-10), opinión (0-10)

## 🎯 Objetivos Cumplidos

### Requerimientos de Ordenamiento Implementados

1. **Encuestados por pregunta**: Descendente por opinión, luego experticia
2. **Preguntas por tema**: Descendente por promedio de opinión, experticia y cantidad de encuestados
3. **Temas generales**: Descendente por promedio de promedios de opiniones, experticia y total de encuestados
4. **Lista general de encuestados**: Descendente por experticia, luego ID (mayor primero)

### Análisis Estadístico Desarrollado

- Promedio, mediana y moda de opiniones por pregunta
- Identificación de preguntas con mayor/menor valores estadísticos
- Cálculo de extremismo (% opiniones en 0 o 10)
- Cálculo de consenso (% opiniones en la moda)

## 🔧 Soluciones Implementadas

### Solución 1: Arreglos y Matrices + Merge Sort

- **Estructura**: Clases con arreglos internos
- **Algoritmo**: Merge Sort personalizado
- **Complejidad**: O(n log n) para ordenamientos
- **Archivo**: `Soluciones/Solucion1_Arreglos/solucion1.py`

### Solución 2: Diccionarios + Árboles Binarios de Búsqueda

- **Estructura**: Diccionarios anidados
- **Algoritmo**: BST con comparadores personalizados
- **Complejidad**: O(n log n) promedio, O(n²) peor caso
- **Archivo**: `Soluciones/Solucion2_Diccionarios/solucion2.py`

## 📁 Estructura del Proyecto

```
Proyecto-Encuesta---ADA-I/
├── README.md                          # Este archivo
├── Contexto/
│   ├── Readme.md                      # Especificación completa del problema
│   ├── Guia entrada y salida.md       # Formato de entrada y salida
│   ├── Datos de entrada/
│   │   ├── Test1.txt                  # Caso de prueba 1
│   │   ├── Test2.txt                  # Caso de prueba 2
│   │   └── Test3.txt                  # Caso de prueba 3
│   └── Datos de salida/
│       ├── outputTest1V2.txt          # Salida esperada Test1
│       ├── outputTest2V2.txt          # Salida esperada Test2
│       └── outputTest3V3.txt          # Salida esperada Test3
└── Soluciones/
    ├── Solucion1_Arreglos/
    │   ├── solucion1.py               # Implementación con arreglos
    │   └── README.md                  # Documentación técnica
    ├── Solucion2_Diccionarios/
    │   ├── solucion2.py               # Implementación con diccionarios
    │   └── README.md                  # Documentación técnica
    ├── test_soluciones.py             # Script de pruebas automáticas
    ├── comparar_resultados.py         # Script de comparación
    ├── INSTRUCCIONES.md               # Instrucciones de ejecución
    └── README.md                      # Documentación general
```

## 🚀 Instalación y Ejecución

### Requerimientos

- **Python 3.6+**
- **No requiere librerías externas** (implementación pura)

### Ejecución Rápida

```powershell
# Clonar/descargar el proyecto
cd "Proyecto-Encuesta---ADA-I"

# Ejecutar Solución 1 (Arreglos + Merge Sort)
cd "Soluciones\Solucion1_Arreglos"
python solucion1.py "..\..\Contexto\Datos de entrada\Test1.txt"

# Ejecutar Solución 2 (Diccionarios + BST)
cd "..\Solucion2_Diccionarios"
python solucion2.py "..\..\Contexto\Datos de entrada\Test1.txt"

# Ejecutar todas las pruebas automáticamente
cd ".."
python test_soluciones.py

# Comparar resultados
python comparar_resultados.py
```

### Pruebas Disponibles

- **Test1.txt**: Caso base del enunciado (K=2, M=2, 12 encuestados)
- **Test2.txt**: Caso intermedio con mayor complejidad
- **Test3.txt**: Caso extenso para análisis de rendimiento

### Ejecución Manual Detallada

#### Solución 1: Arreglos y Matrices con Merge Sort

```powershell
# Navegar al directorio de la solución 1
cd "Soluciones\Solucion1_Arreglos"

# Ejecutar con archivos de prueba individuales
python solucion1.py "..\..\Contexto\Datos de entrada\Test1.txt"
python solucion1.py "..\..\Contexto\Datos de entrada\Test2.txt"
python solucion1.py "..\..\Contexto\Datos de entrada\Test3.txt"
```

#### Solución 2: Diccionarios con Árboles Binarios de Búsqueda

```powershell
# Navegar al directorio de la solución 2
cd "Soluciones\Solucion2_Diccionarios"

# Ejecutar con archivos de prueba individuales
python solucion2.py "..\..\Contexto\Datos de entrada\Test1.txt"
python solucion2.py "..\..\Contexto\Datos de entrada\Test2.txt"
python solucion2.py "..\..\Contexto\Datos de entrada\Test3.txt"
```

#### Scripts de Prueba Automática

```powershell
# Probar ambas soluciones automáticamente (desde directorio Soluciones/)
cd Soluciones
python test_soluciones.py

# Comparar resultados detalladamente
python comparar_resultados.py
```

**Archivos de prueba permiten:**

- Ejecutar ambas soluciones con todos los archivos de prueba
- Medir tiempos de ejecución y mostrar estadísticas de rendimiento
- Comparar resultados entre soluciones
- Analizar diferencias línea por línea
- Guardar salidas en archivos para revisión manual

## Formatos de Entrada y Salida

### Formato de Archivo de Entrada

Los archivos de entrada deben seguir este formato:

```
Nombre1, Experticia: X, Opinión: Y
Nombre2, Experticia: X, Opinión: Y
...
NombreN, Experticia: X, Opinión: Y


{id1, id2, id3}  # Pregunta 1.1
{id4, id5}       # Pregunta 1.2


{id6, id7, id8}  # Pregunta 2.1
{id9, id10}      # Pregunta 2.2
```

**Notas importantes:**

- Los IDs en las preguntas corresponden a la posición del encuestado en la lista (1-indexado)
- Las líneas vacías separan temas
- Cada bloque de preguntas constituye un tema

### Formato de Salida

Ambas soluciones generan salidas idénticas en el siguiente formato:

```
Resultados de la encuesta:

[X.XX] Tema N:
 [Y.YY] Pregunta N.M: (id1, id2, ...)

Lista de encuestados:
 (id, Nombre:'...', Experticia:X, Opinión:Y)

Resultados:
  Pregunta con mayor promedio de opinion: [X.XX] Pregunta: N.M
  Pregunta con menor promedio de opinion: [X.XX] Pregunta: N.M
  ...
```

- **Test2.txt**: Caso intermedio con mayor complejidad
- **Test3.txt**: Caso extenso para análisis de rendimiento

## Análisis de Complejidad

### Solución 1 - Arreglos + Merge Sort

- **Carga de datos**: O(n)
- **Ordenamiento por pregunta**: O(n log n)
- **Ordenamiento por tema**: O(m log m)
- **Ordenamiento general**: O(k log k + n log n)
- **Análisis estadístico**: O(n)
- **Complejidad total**: O(n log n)

### Solución 2 - Diccionarios + BST

- **Carga de datos**: O(n)
- **Construcción de BST**: O(n log n) promedio, O(n²) peor caso
- **Recorrido ordenado**: O(n)
- **Análisis estadístico**: O(n)
- **Complejidad total**: O(n log n) promedio, O(n²) peor caso

## Características Técnicas

### Implementación Manual

- **Algoritmos de ordenamiento** implementados desde cero
- **Estructuras de datos** construidas sin librerías externas
- **Análisis estadístico** con fórmulas propias
- **Sin uso** de `sort()`, `sorted()` u otros métodos predefinidos

### Validación y Pruebas

- **Scripts de prueba automática** para ambas soluciones
- **Comparación de resultados** con salidas esperadas
- **Análisis de rendimiento** con diferentes tamaños de entrada
- **Verificación de correctitud** en todos los casos de prueba

## Resultados y Rendimiento

### Comparación de Soluciones

- **Solución 1**: Más estable, complejidad garantizada O(n log n)
- **Solución 2**: Más flexible, pero puede degradarse a O(n²)
- **Uso de memoria**: Ambas soluciones tienen uso similar O(n)
- **Tiempo de ejecución**: Merge Sort generalmente más rápido en casos grandes

### Casos de Uso Recomendados

- **Arreglos + Merge Sort**: Datos de gran volumen, garantía de rendimiento
- **Diccionarios + BST**: Flexibilidad en consultas, estructuras dinámicas

## � Diferencias Técnicas entre Soluciones

### Solución 1: Arreglos + Merge Sort

- **Estructuras**: Clases con arreglos internos, matrices
- **Ordenamiento**: Merge Sort (O(n log n) garantizado)
- **Estabilidad**: Sí (mantiene orden relativo en empates)
- **Memoria**: Menor uso, estructuras fijas
- **Complejidad peor caso**: O(n log n)

### Solución 2: Diccionarios + Árboles Binarios de Búsqueda (BST)

- **Estructuras**: Diccionarios anidados con árboles binarios
- **Ordenamiento**: Árbol Binario de Búsqueda (O(n log n) promedio)
- **Estabilidad**: Depende del comparador personalizado
- **Memoria**: Mayor flexibilidad, nodos de árbol + diccionarios
- **Complejidad peor caso**: O(n²) (árbol degenerado)

## Validación de Resultados

Para validar que las soluciones funcionan correctamente:

1. **Ejecutar ambas soluciones** con el mismo archivo de entrada
2. **Comparar salidas** - deben ser idénticas o muy similares
3. **Verificar con salidas esperadas** en `Contexto/Datos de salida/`
4. **Revisar tiempos de ejecución** para análisis de rendimiento

### Análisis de Complejidad Detallado

#### Complejidad Temporal

- **Solución 1**: O(n log n) en todos los casos
- **Solución 2**: O(n log n) promedio, O(n²) peor caso

#### Complejidad Espacial

- **Solución 1**: O(n) para arreglos auxiliares
- **Solución 2**: O(log n) promedio (altura del BST), O(n) peor caso

## Solución de Problemas

### Error: "No such file or directory"

- Verificar que estás en el directorio correcto
- Usar rutas absolutas si es necesario
- Verificar que el archivo de entrada existe

### Salidas diferentes entre soluciones

- Es esperado en casos de empate (BST puede variar según comparador)
- Verificar que los promedios y estadísticas sean iguales
- Las diferencias deben ser solo en orden de elementos equivalentes

## Información del Proyecto

### Desarrolladores

- **Universidad del Valle**
- **Curso**: Análisis y Diseño de Algoritmos I
- **Año**: 2025

### Contacto y Soporte

Para consultas sobre el proyecto, revisar:

1. `Contexto/Readme.md` - Especificación completa del problema
2. `Contexto/Guia entrada y salida.md` - Formato de entrada y salida
3. Archivos README.md en cada carpeta de solución (`Solucion1_Arreglos/` y `Solucion2_Diccionarios/`)

---
