# Instrucciones de Ejecución - Proyecto ADA I

## Estructura del Proyecto

```
ADA I - Proyecto/
├── Contexto/
│   ├── Readme.md                    # Especificación completa del problema
│   ├── Guia entrada y salida.md     # Formato de entrada y salida
│   ├── Datos de entrada/
│   │   ├── Test1.txt               # Archivo de prueba 1
│   │   ├── Test2.txt               # Archivo de prueba 2
│   │   └── Test3.txt               # Archivo de prueba 3
│   └── Datos de salida/
│       ├── outputTest1V2.txt       # Salida esperada Test1
│       ├── outputTest2V2.txt       # Salida esperada Test2
│       └── outputTest3V3.txt       # Salida esperada Test3
└── Soluciones/
    ├── Solucion1_Arreglos/
    │   ├── solucion1.py            # Implementación con arreglos + Merge Sort
    │   └── README.md               # Documentación técnica
    ├── Solucion2_Diccionarios/
    │   ├── solucion2.py            # Implementación con diccionarios + BST
    │   └── README.md               # Documentación técnica
    ├── README.md                   # Documentación general
    ├── test_soluciones.py          # Script de prueba automática
    ├── comparar_resultados.py      # Script de comparación
    └── INSTRUCCIONES.md            # Este archivo
```

## Requerimientos

- **Python 3.6 o superior**
- **Sistema operativo**: Windows, Linux, macOS
- **No requiere librerías externas** (implementación pura)

## Ejecución Manual de las Soluciones

### Solución 1: Arreglos y Matrices con Merge Sort

```bash
# Navegar al directorio de la solución 1
cd "Soluciones/Solucion1_Arreglos"

# Ejecutar con un archivo de prueba
python solucion1.py "../../Contexto/Datos de entrada/Test1.txt"
python solucion1.py "../../Contexto/Datos de entrada/Test2.txt"
python solucion1.py "../../Contexto/Datos de entrada/Test3.txt"
```

### Solución 2: Diccionarios con Árboles Binarios de Búsqueda

```bash
# Navegar al directorio de la solución 2
cd "Soluciones/Solucion2_Diccionarios"

# Ejecutar con un archivo de prueba
python solucion2.py "../../Contexto/Datos de entrada/Test1.txt"
python solucion2.py "../../Contexto/Datos de entrada/Test2.txt"
python solucion2.py "../../Contexto/Datos de entrada/Test3.txt"
```

## Prueba Automática

### Probar Ambas Soluciones

```bash
# Desde el directorio Soluciones/
cd Soluciones
python test_soluciones.py
```

Este archivo permite:

- Ejecutar ambas soluciones con todos los archivos de prueba
- Medir tiempos de ejecución
- Comparar resultados entre soluciones
- Mostrar estadísticas de rendimiento

### Comparar Resultados Detalladamente

```bash
# Desde el directorio Soluciones/
cd Soluciones
python comparar_resultados.py
```

Este archivo permite:

- Analizar diferencias línea por línea
- Guardar salidas en archivos para revisión manual
- Generar reportes de comparación detallados

## Formato de Archivo de Entrada

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

...
```

**Notas importantes:**

- Los IDs en las preguntas corresponden a la posición del encuestado en la lista (1-indexado)
- Las líneas vacías separan temas
- Cada bloque de preguntas constituye un tema

## Formato de Salida

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

## Diferencias Técnicas entre Soluciones

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

## Solución de Problemas

### Error: "No such file or directory"

- Verificar que estás en el directorio correcto
- Usar rutas absolutas si es necesario
- Verificar que el archivo de entrada existe

### Salidas diferentes entre soluciones

- Es esperado en casos de empate (BST puede variar según comparador)
- Verificar que los promedios y estadísticas sean iguales
- Las diferencias deben ser solo en orden de elementos equivalentes

## Análisis de Complejidad

### Complejidad Temporal

- **Solución 1**: O(n log n) en todos los casos
- **Solución 2**: O(n log n) promedio, O(n²) peor caso

### Complejidad Espacial

- **Solución 1**: O(n) para arreglos auxiliares
- **Solución 2**: O(log n) promedio (altura del BST), O(n) peor caso

## Contacto y Soporte

Para dudas sobre la implementación:

1. Revisar la documentación en `README.md` de cada solución
2. Verificar el formato de entrada según `Guia entrada y salida.md`
3. Consultar la especificación completa en `Contexto/Readme.md`

---
