# Soluciones al Problema de Procesamiento de Encuesta

Este directorio contiene dos soluciones completamente diferentes al problema de procesamiento de encuesta, cada una utilizando estructuras de datos y algoritmos de ordenamiento distintos según los requerimientos del proyecto.

## Estructura del Proyecto

```
Soluciones/
├── Solucion1_Arreglos/
│   ├── solucion1.py          # Implementación con arreglos y Merge Sort
│   └── README.md             # Documentación detallada
├── Solucion2_Diccionarios/
│   ├── solucion2.py          # Implementación con diccionarios y Quick Sort
│   └── README.md             # Documentación detallada
├── README.md                 # Este archivo
├── test_soluciones.py        # Script para probar ambas soluciones
└── comparar_resultados.py    # Script para comparar salidas
```

## Diferencias Principales entre las Soluciones

### Solución 1: Arreglos y Matrices con Merge Sort

- **Estructuras de datos**: Arreglos, matrices y clases con arreglos internos
- **Algoritmo de ordenamiento**: Merge Sort (O(n log n) garantizado)
- **Ventajas**: Estabilidad, predictibilidad, uso eficiente de memoria
- **Características**: Implementación más tradicional y directa

### Solución 2: Diccionarios con Árboles Binarios de Búsqueda

- **Estructuras de datos**: Diccionarios anidados con Árboles Binarios de Búsqueda
- **Algoritmo de ordenamiento**: BST (O(n log n) promedio, O(n²) peor caso)
- **Ventajas**: Ordenamiento natural, comparadores personalizados, estructura híbrida
- **Características**: Implementación moderna que combina flexibilidad de diccionarios con eficiencia de árboles

## Requerimientos

- Python 3.6 o superior
- No se requieren librerías externas (implementación pura de algoritmos)

## Ejecución de las Soluciones

### Solución 1 (Arreglos + Merge Sort)

```bash
cd Solucion1_Arreglos
python solucion1.py "../../Contexto/Datos de entrada/Test1.txt"
```

### Solución 2 (Diccionarios + BST)

```bash
cd Solucion2_Diccionarios
python solucion2.py "../../Contexto/Datos de entrada/Test1.txt"
```

## Scripts de Utilidad

### Probar Ambas Soluciones

```bash
python test_soluciones.py
```

Este script ejecuta ambas soluciones con todos los archivos de prueba y muestra los resultados.

### Comparar Resultados

```bash
python comparar_resultados.py
```

Este script compara las salidas de ambas soluciones para verificar que sean idénticas.

## Archivos de Prueba Disponibles

- `Test1.txt`: Ejemplo básico con 2 temas, 2 preguntas por tema
- `Test2.txt`: Caso más complejo con 3 temas, diferentes números de preguntas
- `Test3.txt`: Caso de prueba adicional para validación

## Formato de Entrada

Los archivos de entrada siguen el formato especificado en la guía:

```
Nombre1, Experticia: X, Opinión: Y
Nombre2, Experticia: X, Opinión: Y
...

{id1, id2, id3}  # Pregunta 1.1
{id4, id5}       # Pregunta 1.2

{id6, id7, id8}  # Pregunta 2.1
{id9, id10}      # Pregunta 2.2
```

## Formato de Salida

Ambas soluciones generan exactamente el mismo formato de salida:

```
Resultados de la encuesta:

[X.XX] Tema N:
 [Y.YY] Pregunta N.M: (id1, id2, ...)

Lista de encuestados:
 (id, Nombre:'...', Experticia:X, Opinión:Y)

Resultados:
  Pregunta con mayor promedio de opinion: [X.XX] Pregunta: N.M
  ...
```

## Análisis de Complejidad

### Solución 1 (Merge Sort)

- **Complejidad temporal**: O(n log n) garantizado
- **Complejidad espacial**: O(n) para arreglos auxiliares
- **Estabilidad**: Sí

### Solución 2 (BST)

- **Complejidad temporal**: O(n log n) promedio, O(n²) peor caso
- **Complejidad espacial**: O(n) para nodos del árbol
- **Estabilidad**: Depende del comparador

## Validación

Ambas soluciones han sido probadas con todos los archivos de entrada proporcionados y generan resultados idénticos que coinciden con las salidas esperadas del proyecto.

## Cumplimiento de Requerimientos

✅ **Dos soluciones diferentes**: Estructuras de datos completamente distintas  
✅ **No reutilización**: Arreglos vs Diccionarios  
✅ **Algoritmos diferentes**: Merge Sort vs Árbol Binario de Búsqueda  
✅ **Implementación manual**: Sin uso de funciones predefinidas como `sort()`  
✅ **Carga y ordenamiento**: Los datos se cargan, ordenan y muestran por la estructura elegida  
✅ **Formato correcto**: Salidas idénticas al formato especificado
