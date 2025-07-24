# El Problema del Procesamiento de una Encuesta

## Descripción del Problema

Una consultoría de datos desea realizar un análisis de los resultados de una gran encuesta, con la finalidad de identificar cuáles temas, con base en ciertas preguntas, tienen opiniones más favorables y poder también responder otras preguntas afines.

Esta gran encuesta está dividida en diversos temas, cada tema tiene diferentes preguntas, donde cada pregunta consulta sobre hasta qué punto se está de acuerdo sobre una propuesta; a su vez cada pregunta fue realizada a ciertas personas (encuestados), cada persona solo puede participar respondiendo sólo una pregunta.

## Estructura de la Encuesta

La encuesta está organizada de la siguiente manera:

- **K temas**: cada uno con un nombre
- **M preguntas** por tema
- **Nmin y Nmax**: cantidad mínima y máxima de encuestados por pregunta
- **Encuestados**: cada uno con:
  - Número identificador
  - Nombre
  - Nivel de experticia (entero entre 0 y 10)
  - Opinión-respuesta (entero entre 0 y 10, donde 0 = completamente desfavorable, 10 = completamente favorable)

**Restricciones**: K, M, Nmin y Nmax son enteros positivos, además Nmin < Nmax.

## Requerimientos de Ordenamiento

### 1. Ordenamiento de Encuestados por Pregunta

Los encuestados dentro de cada pregunta deben ordenarse **descendentemente** según:

1. Valor de opinión (criterio principal)
2. Nivel de experticia (criterio de desempate)

### 2. Ordenamiento de Preguntas por Tema

Las preguntas dentro de cada tema deben ordenarse **descendentemente** según:

1. Promedio del valor de opinión (criterio principal)
2. Promedio de experticia (primer desempate)
3. Número de encuestados (segundo desempate)

### 3. Ordenamiento de Temas

Los temas deben ordenarse **descendentemente** según:

1. Promedio de los promedios de los valores de las opiniones (criterio principal)
2. Promedio de promedios de experticia (primer desempate)
3. Número total de encuestados (segundo desempate)

### 4. Lista General de Encuestados

Generar una lista de todas las personas encuestadas ordenadas **descendentemente** por:

1. Nivel de experticia (criterio principal)
2. Identificador (criterio de desempate - mayor identificador primero)

## Ejemplo de Instancia

**Parámetros**: K = 2, M = 2, Nmin = 2, Nmax = 4

### Encuestados:

1. Sofia García, Experticia: 1, Opinión: 6
2. Alejandro Torres, Experticia: 7, Opinión: 10
3. Valentina Rodriguez, Experticia: 9, Opinión: 0
4. Juan López, Experticia: 10, Opinión: 1
5. Martina Martinez, Experticia: 7, Opinión: 0
6. Sebastián Pérez, Experticia: 8, Opinión: 9
7. Camila Fernández, Experticia: 2, Opinión: 7
8. Mateo González, Experticia: 4, Opinión: 7
9. Isabella Díaz, Experticia: 7, Opinión: 5
10. Daniel Ruiz, Experticia: 2, Opinión: 9
11. Luciana Sánchez, Experticia: 1, Opinión: 7
12. Lucas Vásquez, Experticia: 6, Opinión: 8

### Distribución por Temas:

**Tema 1:**

- Pregunta 1.1: {10, 2}
- Pregunta 1.2: {1, 9, 12, 6}

**Tema 2:**

- Pregunta 2.1: {11, 8, 7}
- Pregunta 2.2: {3, 4, 5}

### Salida Esperada:

```
[8.25] Tema 1:
[9.50] Pregunta 1.1: (2, 10)
[7.00] Pregunta 1.2: (6, 12, 1, 9)
[3.67] Tema 2:
[7.00] Pregunta 2.2: (8, 7, 11)
[0.33] Pregunta 2.1: (4, 3, 5)
Lista de encuestados:
{4, 3, 6, 9, 5, 2, 12, 10, 7, 11, 1}
```

_Los valores entre corchetes son los promedios tanto de la pregunta como del tema_

## Análisis Estadístico Requerido

La consultoría también necesita obtener los siguientes datos:

1. **Pregunta con mayor promedio de opiniones**
2. **Pregunta con menor promedio de opiniones**
3. **Pregunta con mayor mediana de opiniones**
4. **Pregunta con menor mediana de opiniones**
5. **Pregunta con el mayor valor de moda de opiniones**
6. **Pregunta con el menor valor de moda de opiniones**
7. **Pregunta con mayor valor de extremismo**
   - Extremismo = porcentaje de encuestados con opinión completamente desfavorable (0) o completamente favorable (10)
8. **Pregunta con mayor consenso**
   - Consenso = porcentaje de encuestados con la opinión moda (más frecuente)

## Aspectos de Implementación

### 1. Diferencia de Soluciones

Las 2 soluciones se consideran diferentes siempre y cuando no se reutilicen estructuras de datos. Si se usa un arreglo para la solución 1, esta no podrá ser reutilizada en la solución 2.

### 2. Ordenamiento e Impresión

Los datos deben ser cargados, ordenados y mostrados por la estructura de datos elegida. No es válido usar una estructura pero haber ordenado previamente en otra. En caso de que la estructura elegida no tenga métodos de ordenamiento, sí puede usar una estructura auxiliar implementando sus métodos.

### 3. Métodos Predefinidos

Se deben usar métodos propios (implementarlos en código). **No es válido usar funciones predeterminadas** como `sort()` para listas en Python.

## Requerimientos del Proyecto

### Debe Entregar:

1. **2 soluciones al problema planteado**
   - Cada solución debe usar diferentes estructuras de datos
   - Diferentes algoritmos para manipular los datos

### Para Cada Solución:

1. **Explicación clara** de la idea de solución
2. **Estructuras de datos** a utilizar
3. **Algoritmos** a usar (con descripción detallada)
4. **Complejidad computacional teórica** de cada algoritmo
5. **Implementación manual** de algoritmos existentes (no usar librerías)
6. **Set de pruebas** mínimo 4 instancias del problema
7. **Código fuente** en Java, C++ o Python
8. **Instrucciones de ejecución**

## Informe Requerido

### Por Cada Estrategia:

- Explicación clara de la solución
- Estructuras de datos utilizadas
- Algoritmos utilizados con descripción algorítmica
- Análisis de complejidad computacional teórica
- Implementación manual de algoritmos (sin librerías)

### Análisis de Resultados:

1. **Comparaciones** de complejidad teórica vs complejidad real
2. **Relación** tamaño de entrada vs tiempo de salida
3. **Gráficos** de tamaño de entrada vs tiempo de salida
4. **Comparación** de tiempos entre las distintas soluciones
5. **Uso** de todos los archivos de prueba proporcionados y propuestos

### Conclusiones:

- Conclusiones claras que reflejen:
  - Lo descrito en el informe
  - Lo desarrollado en la implementación
  - La experiencia adquirida durante el desarrollo

---

_Proyecto desarrollado para el curso ADA I - Universidad del Valle_
