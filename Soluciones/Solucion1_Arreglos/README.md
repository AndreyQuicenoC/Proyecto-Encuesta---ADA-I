# Solución 1: Arreglos y Matrices con Merge Sort

## Descripción de la Solución

Esta solución utiliza **exclusivamente arreglos y matrices** como estructuras de datos principales, implementando el algoritmo de ordenamiento **Merge Sort** para los requerimientos del problema al ordenar.

## Estructuras de Datos Utilizadas

### 1. Clases con Arreglos Internos

- **Clase Encuestado**: Almacena id, nombre, experticia y opinión
- **Clase Pregunta**: Contiene un arreglo de objetos Encuestado
- **Clase Tema**: Contiene un arreglo de objetos Pregunta

### 2. Arreglos Simples

- Arreglos para almacenar opiniones durante cálculos estadísticos
- Matrices de frecuencias para cálculo de moda (arreglo de 11 posiciones para opiniones 0-10)
- Arreglos auxiliares para operaciones de merge

## Algoritmos Implementados

### 1. Merge Sort (Complejidad: O(n log n))

Se implementaron diferentes versiones de Merge Sort para cada tipo de ordenamiento:

#### a) `merge_sort_encuestados_pregunta()`

- **Propósito**: Ordenar encuestados dentro de una pregunta
- **Criterios**: Descendente por opinión, luego por experticia
- **Complejidad**: O(n log n) donde n = número de encuestados por pregunta

#### b) `merge_sort_preguntas()`

- **Propósito**: Ordenar preguntas dentro de un tema
- **Criterios**: Descendente por promedio de opinión, luego promedio de experticia, luego número de encuestados
- **Complejidad**: O(m log m) donde m = número de preguntas por tema

#### c) `merge_sort_temas()`

- **Propósito**: Ordenar temas
- **Criterios**: Descendente por promedio de promedios de opinión, luego experticia, luego total de encuestados
- **Complejidad**: O(k log k) donde k = número de temas

#### d) `merge_sort_todos_encuestados()`

- **Propósito**: Ordenar lista general de encuestados
- **Criterios**: Descendente por experticia, luego por id (mayor primero)
- **Complejidad**: O(n log n) donde n = total de encuestados

### 2. Algoritmos de Cálculo Estadístico

#### Cálculo de Mediana (O(n log n))

```python
def calcular_mediana_opinion(self):
    opiniones = []
    for encuestado in self.encuestados:
        opiniones.append(encuestado.opinion)

    opiniones_ordenadas = merge_sort_simple(opiniones)
    n = len(opiniones_ordenadas)

    if n % 2 == 0:
        return (opiniones_ordenadas[n//2 - 1] + opiniones_ordenadas[n//2]) / 2
    else:
        return opiniones_ordenadas[n//2]
```

#### Cálculo de Moda (O(n))

```python
def calcular_moda_opinion(self):
    frecuencias = [0] * 11  # Arreglo para opiniones 0-10
    for encuestado in self.encuestados:
        frecuencias[encuestado.opinion] += 1

    max_frecuencia = 0
    moda = 0
    for i in range(11):
        if frecuencias[i] > max_frecuencia:
            max_frecuencia = frecuencias[i]
            moda = i

    return moda
```

## Complejidad Computacional Total

### Análisis por Operación:

1. **Lectura de datos**: O(n) donde n = total de encuestados
2. **Ordenamiento de encuestados por pregunta**: O(n log n) total
3. **Ordenamiento de preguntas por tema**: O(m² log m) donde m = promedio de preguntas por tema
4. **Ordenamiento de temas**: O(k log k) donde k = número de temas
5. **Cálculos estadísticos**: O(n) para cada cálculo

### Complejidad Total: O(n log n + m² log m + k log k)

En el caso promedio donde n >> m >> k, la complejidad se reduce a **O(n log n)**.

## Ventajas de la Implementación

1. **Estabilidad**: Merge Sort es un algoritmo estable
2. **Predictibilidad**: Siempre O(n log n), sin casos peores
3. **Simplicidad**: Estructuras de datos simples y directas
4. **Memoria**: Uso eficiente con arreglos de tamaño fijo para frecuencias

## Instrucciones de Ejecución

```bash
python solucion1.py <archivo_entrada>
```

### Ejemplo:

```bash
python solucion1.py "../../Contexto/Datos de entrada/Test1.txt"
```

## Archivos de Prueba Soportados

La solución funciona con todos los archivos de prueba del proyecto:

- Test1.txt
- Test2.txt
- Test3.txt

Y genera salidas en el formato especificado en la guía del proyecto.
