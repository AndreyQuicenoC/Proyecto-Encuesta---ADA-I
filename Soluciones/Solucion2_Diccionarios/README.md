# Solución 2: Diccionarios con Árboles Binarios de Búsqueda

## Descripción de la Solución

Esta solución implementa el procesamiento de encuestas utilizando **diccionarios y árboles binarios de búsqueda (BST)** como estructuras de datos principales para almacenar, procesar y ordenar la información.

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
- **Recorrido in-orden**: Obtiene elementos ordenados según el criterio especificado

## Algoritmos de Ordenamiento

### 1. BST Especializados por Tipo de Ordenamiento

#### a) `bst_encuestados_pregunta()`
- **Propósito**: Ordenar encuestados dentro de una pregunta
- **Criterios**: Descendente por opinión, luego por experticia

#### b) `bst_preguntas()`
- **Propósito**: Ordenar preguntas dentro de un tema
- **Criterios**: Descendente por promedio de opinión, luego promedio de experticia, luego número de encuestados

#### c) `bst_temas()`
- **Propósito**: Ordenar temas en el resultado final
- **Criterios**: Descendente por promedio total de opinión, luego experticia promedio, luego total de encuestados

#### d) `bst_todos_encuestados()`
- **Propósito**: Ordenar lista general de encuestados
- **Criterios**: Descendente por experticia, luego por ID

### 2. Implementación de BST con Comparadores

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
            if self.comparador(valor, self.valor):
                # Insertar a la izquierda
            else:
                # Insertar a la derecha
        else:
            # Comparación estándar por clave
    
    def recorrido_inorden(self, resultado):
        # Recorrido que retorna elementos ordenados
        if self.izquierdo:
            self.izquierdo.recorrido_inorden(resultado)
        resultado[self.clave] = self.valor
        if self.derecho:
            self.derecho.recorrido_inorden(resultado)
```

## Cálculos Estadísticos

### 1. Mediana con BST
```python
def calcular_mediana_con_bst(opiniones_dict):
    # Crear BST para ordenar opiniones
    arbol = ArbolBST()
    frecuencias = {}
    
    # Construir BST con frecuencias
    for opinion in opiniones_dict.values():
        if opinion in frecuencias:
            frecuencias[opinion] += 1
        else:
            frecuencias[opinion] = 1
            arbol.insertar(opinion, opinion)
    
    # Obtener valores ordenados y calcular mediana
    valores_ordenados = arbol.obtener_ordenado()
    total_elementos = len(opiniones_dict)
    
    # Calcular posición de mediana
    if total_elementos % 2 == 1:
        posicion_mediana = total_elementos // 2
    else:
        posicion_mediana = total_elementos // 2 - 1
    
    # Encontrar elemento en posición de mediana
    contador = 0
    for valor in valores_ordenados.keys():
        contador += frecuencias[valor]
        if contador > posicion_mediana:
            return valor
```

### 2. Moda con Diccionario de Frecuencias
```python
frecuencias = {}
for opinion in opiniones.values():
    if opinion in frecuencias:
        frecuencias[opinion] += 1
    else:
        frecuencias[opinion] = 1

max_frecuencia = max(frecuencias.values())
moda = None
for valor, freq in frecuencias.items():
    if freq == max_frecuencia:
        if moda is None or valor < moda:
            moda = valor
```

### 3. Otros Cálculos
- **Promedio**: Suma de valores dividida por cantidad
- **Extremismo**: Porcentaje de opiniones en valores 0 o 10
- **Consenso**: Porcentaje de encuestados con la moda de opinión

## Procesamiento de Archivos

### Lectura de Datos
```python
def leer_archivo_entrada(ruta_archivo):
    # Leer y procesar líneas del archivo
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()
    
    # Procesar encuestados y estructura de preguntas
    # Crear diccionarios de encuestados y temas
    # Retornar estructuras de datos organizadas
```

## Complejidad Computacional

### Análisis por Operación
1. **Lectura de datos**: O(n) donde n = total de encuestados
2. **Cálculo de estadísticas**: O(n) para cada pregunta
3. **Construcción del BST**: O(n log n) promedio, O(n²) peor caso
4. **Recorrido in-orden**: O(n) para obtener elementos ordenados
5. **Ordenamiento total**: O(n log n + m² log m + k log k)

Donde:
- **n**: Total de encuestados
- **m**: Promedio de preguntas por tema
- **k**: Número de temas

### Complejidad Total
- **Caso promedio**: O(n log n)
- **Peor caso**: O(n²) cuando los BST degeneran

## Ventajas de la Implementación

1. **Flexibilidad**: Comparadores personalizados para diferentes criterios de ordenamiento
2. **Estructuras dinámicas**: Los BST se construyen y ordenan automáticamente
3. **Acceso eficiente**: Diccionarios permiten acceso directo por clave
4. **Ordenamiento natural**: Los BST mantienen elementos ordenados durante la inserción
5. **Escalabilidad**: Maneja eficientemente datasets de diferentes tamaños

## Criterios de Ordenamiento y Desempate

### Ordenamiento de Elementos
- **Encuestados en pregunta**: Por opinión (desc), luego experticia (desc)
- **Preguntas en tema**: Por promedio opinión (desc), luego experticia (desc), luego cantidad
- **Temas**: Por promedio total opinión (desc), luego experticia (desc), luego total encuestados
- **Lista general**: Por experticia (desc), luego ID (desc)

### Manejo de Empates
- **Mediana**: En caso de número par de elementos, se toma el menor de los dos valores centrales
- **Moda**: En caso de empate de frecuencias, se selecciona el menor valor
- **Preguntas**: En empate de estadísticas, se elige la pregunta con menor identificador

## Instrucciones de Ejecución

```bash
python solucion2.py <archivo_entrada>
```

### Ejemplo:
```bash
python solucion2.py "../../Contexto/Datos de entrada/Test1.txt"
```

## Archivos de Prueba Soportados

La solución procesa correctamente todos los archivos de prueba del proyecto:
- Test1.txt
- Test2.txt
- Test3.txt
- Test4.txt
- Test5.txt  
- Test6.txt

Generando salidas en el formato especificado en la guía del proyecto.

## Comparación con Otros Enfoques

| Aspecto | Merge Sort + Arreglos | BST + Diccionarios |
|---------|----------------------|-------------------|
| **Complejidad promedio** | O(n log n) garantizado | O(n log n) promedio |
| **Complejidad peor caso** | O(n log n) | O(n²) |
| **Flexibilidad ordenamiento** | Media | Alta |
| **Acceso a datos** | Secuencial | Directo por clave |
| **Uso de memoria** | Menor | Moderado |
| **Estabilidad** | Sí | Configurable |
