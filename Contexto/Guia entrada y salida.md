## Proyecto ADA I 2025-1

### Archivos de entrada

Los archivos de entrada tendrán el siguiente formato:

- Lista de participantes
- Salto de línea
- Salto de línea
- Pregunta 1.1
- …

- Pregunta 1.n
- Salto de línea
- Salto de línea
- Pregunta 2.1
- …

- Pregunta 2.n
- Salto de línea
- Salto de línea
- …

**Ejemplo de entrada**

> Sofía García, Experticia: 1, Opinión: 6
> Alejandro Torres, Experticia: 7, Opinión: 10
> Valentina Rodríguez, Experticia: 9, Opinión: 0
> Juan López, Experticia: 10, Opinión: 1
> Martina Martínez, Experticia: 7, Opinión: 0
> Sebastián Pérez, Experticia: 8, Opinión: 9
> Camila Fernández, Experticia: 2, Opinión: 7
> Mateo González, Experticia: 4, Opinión: 7
> Isabella Díaz, Experticia: 7, Opinión: 5
> Daniel Ruiz, Experticia: 2, Opinión: 9
> Luciana Sánchez, Experticia: 1, Opinión: 7
> Lucas Vásquez, Experticia: 6, Opinión: 8
>
> {10, 2}
> {1, 9, 12, 6}
>
> {3, 4, 5}
> {11, 8, 7}

1. **Resultados de la encuesta**

2. **Tema 1:**

   - **Pregunta 1.1:** [Promedio Pregunta 1.1]
   - **Pregunta 1.n:** [Promedio Pregunta 1.n]

3. **(Salto de línea)**

4. **Tema m:**

   - **Pregunta m.1:** [Promedio Pregunta m.1]
   - **Pregunta m.n:** [Promedio Pregunta m.n]

5. **(Salto de línea)**

6. **Lista de encuestados:**

   - participante1
   - participante2
   - …

7. **(Salto de línea)**

8. **Resultados:**
   - **Pregunta con mayor promedio de opinión:** [Promedio] pregunta
   - **Pregunta con menor promedio de opinión:** [Promedio] pregunta
   - **Pregunta con mayor promedio de experticia:** [Promedio] pregunta
   - **Pregunta con menor promedio de experticia:** [Promedio] pregunta
   - **Pregunta con mayor mediana:** [Mediana] pregunta
   - **Pregunta con menor mediana:** [Mediana] pregunta
   - **Pregunta con mayor moda:** [Moda] pregunta
   - **Pregunta con menor moda:** [Moda] pregunta
   - **Pregunta con mayor extremismo:** [Extremismo] pregunta
   - **Pregunta con mayor consenso:** [Consenso] pregunta

> **Nota:** Todos los promedios deberán mostrarse con 2 decimales.

**Ejemplo de salida**

> Resultados de la encuesta:
>
> [8.25] Tema 1:  
> [9.50] Pregunta 1.1: (2, 10)  
> [7.00] Pregunta 1.2: (6, 12, 1, 9)
>
> [3.67] Tema 2:  
> [7.00] Pregunta 2.2: (8, 7, 11)  
> [0.33] Pregunta 2.1: (4, 3, 5)
>
> Lista de encuestados:
>
> (4, Nombre:'Juan López', Experticia:10, Opinión:1)  
> (3, Nombre:'Valentina Rodríguez', Experticia:9, Opinión:0)  
> (6, Nombre:'Sebastián Pérez', Experticia:8, Opinión:9)  
> (9, Nombre:'Isabella Díaz', Experticia:7, Opinión:5)  
> (5, Nombre:'Martina Martínez', Experticia:7, Opinión:0)  
> (2, Nombre:'Alejandro Torres', Experticia:7, Opinión:10)  
> (12, Nombre:'Lucas Vásquez', Experticia:6, Opinión:8)  
> (8, Nombre:'Mateo González', Experticia:4, Opinión:7)  
> (10, Nombre:'Daniel Ruiz', Experticia:2, Opinión:9)  
> (7, Nombre:'Camila Fernández', Experticia:2, Opinión:7)  
> (11, Nombre:'Luciana Sánchez', Experticia:1, Opinión:7)  
> (1, Nombre:'Sofía García', Experticia:1, Opinión:6)
>
> Resultados:  
> Pregunta con mayor promedio de opinion: [9.5] Pregunta: 1.1  
> Pregunta con menor promedio de opinion: [0.33] Pregunta: 2.1  
> Pregunta con mayor promedio de experticia: [8.67] Pregunta: 2.1  
> Pregunta con menor promedio de experticia: [2.33] Pregunta: 2.2  
> Pregunta con Mayor mediana de opinion: [9] Pregunta: 1.1  
> Pregunta con menor mediana de opinion: [0] Pregunta: 2.1  
> Pregunta con menor moda de opinion: [0] Pregunta: 2.1  
> Pregunta con mayor moda de opinion: [7] Pregunta: 2.1  
> Pregunta con mayor extremismo: [0.67] Pregunta: 2.1  
> Pregunta con mayor consenso: [1.0] Pregunta: 2.2
