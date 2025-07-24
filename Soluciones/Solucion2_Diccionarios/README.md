# Solución 2: Diccionarios con Árboles Binarios de Búsqueda

## Descripción de la Solución

Esta solución utiliza **diccionarios como estructura de datos principal** combinada con **Árboles Binarios de Búsqueda (BST)** para implementar todos los requerimientos de ordenamiento del problema.

## Estructuras de Datos Utilizadas

### 1. Diccionarios Anidados
- **Encuestado**: `{'id': int, 'nombre': str, 'experticia': int, 'opinion': int}`
- **Pregunta**: 
  ```python
  {
      'tema_id': int,
      'pregunta_id': int, 
      'encuestados': {id: encuestado_dict},
      'estadisticas': {stat_name: value}
  }
  ```
- **Tema**:
  ```python
  {
      'id': int,
      'preguntas': {pregunta_id: pregunta_dict},
      'estadisticas': {stat_name: value}
  }
  ```

### 2. Árboles Binarios de Búsqueda (BST)
- **Clase NodoArbol**: Representa cada nodo del árbol con clave, valor y comparador personalizado
- **Clase ArbolBST**: Implementa el árbol con métodos de inserción y recorrido
- **Comparadores personalizados**: Funciones específicas para cada tipo de ordenamiento
- **Recorrido in-orden**: Para obtener elementos ordenados según el criterio del comparador

## Algoritmos Implementados

### 1. Árbol Binario de Búsqueda (Complejidad Promedio: O(n log n), Peor Caso: O(n²))

Se implementaron BST personalizados para cada tipo de ordenamiento:

#### a) `bst_encuestados_pregunta()`
- **Propósito**: Ordenar encuestados dentro de una pregunta
- **Criterios**: Descendente por opinión, luego por experticia
- **Implementación**: BST con comparador personalizado

#### b) `bst_preguntas()`
- **Propósito**: Ordenar preguntas dentro de un tema  
- **Criterios**: Descendente por promedio de opinión, luego promedio de experticia, luego número de encuestados

#### c) `bst_temas()`
- **Propósito**: Ordenar temas
- **Criterios**: Descendente por promedio de promedios de opinión, luego experticia, luego total de encuestados

#### d) `bst_todos_encuestados()`
- **Propósito**: Ordenar lista general de encuestados
- **Criterios**: Descendente por experticia, luego por id (mayor primero)

### 2. Implementación de BST con Comparadores Personalizados

```python
class NodoArbol:
    def __init__(self, clave, valor, comparador=None):
        self.clave = clave
        self.valor = valor
        self.izquierdo = None
        self.derecho = None
        self.comparador = comparador
    
    def insertar(self, clave, valor):
        if self.comparador:
            # Usar comparador personalizado
            if self.comparador(valor, self.valor):
                # Insertar a la izquierda
            else:
                # Insertar a la derecha
        else:
            # Comparación estándar por clave
    
    def recorrido_inorden(self, resultado):
        # Recorrido que mantiene el orden según el comparador
```

### 3. Algoritmos de Cálculo Estadístico

#### Cálculo de Mediana con BST (O(n log n))
```python
opiniones_lista = list(opiniones.values())
opiniones_ordenadas = ordenar_con_arbol_simple(opiniones_lista)
n = len(opiniones_ordenadas)
if n % 2 == 0:
    mediana = (opiniones_ordenadas[n//2 - 1] + opiniones_ordenadas[n//2]) / 2
else:
    mediana = opiniones_ordenadas[n//2]
```

#### Cálculo de Moda con Diccionario de Frecuencias (O(n))
```python
frecuencias = {}
for op in opiniones.values():
    if op in frecuencias:
        frecuencias[op] += 1
    else:
        frecuencias[op] = 1

max_frecuencia = max(frecuencias.values())
moda = None
for valor, freq in frecuencias.items():
    if freq == max_frecuencia:
        if moda is None or valor > moda:
            moda = valor
```

## Complejidad Computacional

### Análisis por Operación:
1. **Lectura de datos**: O(n) donde n = total de encuestados
2. **Cálculo de estadísticas**: O(n) para cada pregunta
3. **Construcción del BST**: O(n log n) promedio, O(n²) peor caso (árbol degenerado)
4. **Recorrido in-orden**: O(n) para obtener elementos ordenados

### Complejidad Promedio Total: O(n log n + m² log m + k log k)
### Complejidad Peor Caso: O(n² + m³ + k²)

## Ventajas de la Implementación

1. **Ordenamiento natural**: Los BST mantienen elementos ordenados automáticamente
2. **Flexibilidad**: Comparadores personalizados permiten diferentes criterios de ordenamiento
3. **Estructura híbrida**: Combina la flexibilidad de diccionarios con el ordenamiento de árboles
4. **Eficiencia en promedio**: O(n log n) para la mayoría de casos

## Características Específicas de los BST

1. **Comparadores personalizados**: Cada BST usa una función específica para determinar el orden
2. **Recorrido in-orden**: Garantiza que los elementos se obtengan en el orden deseado
3. **Inserción dinámica**: Los elementos se insertan y ordenan automáticamente
4. **Balance no garantizado**: Puede degenerar en O(n²) con datos ya ordenados

## Instrucciones de Ejecución

```bash
python solucion2.py <archivo_entrada>
```

### Ejemplo:
```bash
python solucion2.py "../../Contexto/Datos de entrada/Test1.txt"
```

## Comparación con Solución 1

| Aspecto | Solución 1 (Merge Sort + Arreglos) | Solución 2 (BST + Diccionarios) |
|---------|-------------------------------------|----------------------------------|
| **Estructura de datos** | Arreglos y matrices | Diccionarios y árboles binarios |
| **Algoritmo de ordenamiento** | Merge Sort | Árbol Binario de Búsqueda |
| **Complejidad promedio** | O(n log n) | O(n log n) |
| **Complejidad peor caso** | O(n log n) | O(n²) |
| **Estabilidad** | Sí | Depende del comparador |
| **Uso de memoria** | Menor | Moderado (nodos de árbol) |
| **Acceso a datos** | Secuencial (índices) | Directo (claves) + Ordenado (BST) |
| **Flexibilidad** | Menor | Mayor (comparadores personalizados) |

## Archivos de Prueba Soportados

La solución funciona con todos los archivos de prueba del proyecto:
- Test1.txt
- Test2.txt  
- Test3.txt

Y genera salidas en el formato especificado en la guía del proyecto.
