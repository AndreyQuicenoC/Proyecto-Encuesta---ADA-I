"""
SOLUCIÓN 1: PROCESAMIENTO DE ENCUESTA CON ARREGLOS Y MATRICES
Algoritmo de ordenamiento: Merge Sort
Estructuras de datos: Arreglos y matrices exclusivamente
"""


import sys
import os

# ----------------- Clases para la encuesta -----------------
class Encuestado:
    def __init__(self, id, nombre, experticia, opinion):
        self.id = id
        self.nombre = nombre
        self.experticia = experticia
        self.opinion = opinion

class Pregunta:
    def __init__(self, tema_id, pregunta_id):
        self.tema_id = tema_id
        self.pregunta_id = pregunta_id
        self.encuestados = []  # Arreglo de objetos Encuestado
        
    def agregar_encuestado(self, encuestado):
        self.encuestados.append(encuestado)
    
    def calcular_promedio_opinion(self):
        if len(self.encuestados) == 0:
            return 0.0
        suma = 0
        for encuestado in self.encuestados:
            suma += encuestado.opinion
        return suma / len(self.encuestados)
    
    def calcular_promedio_experticia(self):
        if len(self.encuestados) == 0:
            return 0.0
        suma = 0
        for encuestado in self.encuestados:
            suma += encuestado.experticia
        return suma / len(self.encuestados)
    
    def calcular_mediana_opinion(self):
        if len(self.encuestados) == 0:
            return 0
        
        # Crear arreglo de opiniones
        opiniones = []
        for encuestado in self.encuestados:
            opiniones.append(encuestado.opinion)
        
        # Ordenar usando merge sort
        opiniones_ordenadas = merge_sort_simple(opiniones)
        n = len(opiniones_ordenadas)
        
        if n % 2 == 0:
            # Si hay empate (n par), se elige la mediana de menor valor según los requisitos
            return opiniones_ordenadas[n//2 - 1]
        else:
            return opiniones_ordenadas[n//2]
    
    def calcular_moda_opinion(self):
        if len(self.encuestados) == 0:
            return 0
        
        frecuencias = [0] * 11  # Opiniones van de 0 a 10
        for encuestado in self.encuestados:
            frecuencias[encuestado.opinion] += 1
        
        max_frecuencia = 0
        moda = 0
        for i in range(11):
            if frecuencias[i] > max_frecuencia:
                max_frecuencia = frecuencias[i]
                moda = i
        
        return moda
    
    def calcular_extremismo(self):
        if len(self.encuestados) == 0:
            return 0.0
        
        extremos = 0
        for encuestado in self.encuestados:
            if encuestado.opinion == 0 or encuestado.opinion == 10:
                extremos += 1
        
        return extremos / len(self.encuestados)
    
    def calcular_consenso(self):
        if len(self.encuestados) == 0:
            return 0.0
        
        moda = self.calcular_moda_opinion()
        contador_moda = 0
        for encuestado in self.encuestados:
            if encuestado.opinion == moda:
                contador_moda += 1
        
        return contador_moda / len(self.encuestados)

class Tema:
    def __init__(self, id):
        self.id = id
        self.preguntas = []  
    
    def agregar_pregunta(self, pregunta):
        self.preguntas.append(pregunta)
    
    def calcular_promedio_total_opinion(self):
        if len(self.preguntas) == 0:
            return 0.0
        suma = 0
        for pregunta in self.preguntas:
            suma += pregunta.calcular_promedio_opinion()
        return suma / len(self.preguntas)
    
    def calcular_promedio_total_experticia(self):
        if len(self.preguntas) == 0:
            return 0.0
        suma = 0
        for pregunta in self.preguntas:
            suma += pregunta.calcular_promedio_experticia()
        return suma / len(self.preguntas)
    
    def calcular_total_encuestados(self):
        total = 0
        for pregunta in self.preguntas:
            total += len(pregunta.encuestados)
        return total

# ----------------- Funciones de ordenamiento con Merge Sort -----------------
def merge_sort_simple(arr):
    """Implementación de merge sort para arreglos simples"""
    if len(arr) <= 1:
        return arr[:]
    
    mid = len(arr) // 2
    left = merge_sort_simple(arr[:mid])
    right = merge_sort_simple(arr[mid:])
    
    return merge_simple(left, right)

def merge_simple(left, right):
    """Función auxiliar para merge de arreglos simples"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    while i < len(left):
        result.append(left[i])
        i += 1
    
    while j < len(right):
        result.append(right[j])
        j += 1
    
    return result

def merge_sort_encuestados_pregunta(encuestados):
    """Merge sort para encuestados dentro de una pregunta (descendente por opinión, luego experticia)"""
    if len(encuestados) <= 1:
        return encuestados[:]
    
    mid = len(encuestados) // 2
    left = merge_sort_encuestados_pregunta(encuestados[:mid])
    right = merge_sort_encuestados_pregunta(encuestados[mid:])
    
    return merge_encuestados_pregunta(left, right)

def merge_encuestados_pregunta(left, right):
    """Merge para encuestados por pregunta"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        # Orden descendente por opinión, luego por experticia, luego por ID (menor primero)
        if (left[i].opinion > right[j].opinion or 
            (left[i].opinion == right[j].opinion and left[i].experticia > right[j].experticia) or
            (left[i].opinion == right[j].opinion and left[i].experticia == right[j].experticia and left[i].id < right[j].id)):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    while i < len(left):
        result.append(left[i])
        i += 1
    
    while j < len(right):
        result.append(right[j])
        j += 1
    
    return result

def merge_sort_preguntas(preguntas):
    """Merge sort para preguntas dentro de un tema"""
    if len(preguntas) <= 1:
        return preguntas[:]
    
    mid = len(preguntas) // 2
    left = merge_sort_preguntas(preguntas[:mid])
    right = merge_sort_preguntas(preguntas[mid:])
    
    return merge_preguntas(left, right)

def merge_preguntas(left, right):
    """Merge para preguntas por tema"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        left_prom_op = left[i].calcular_promedio_opinion()
        right_prom_op = right[j].calcular_promedio_opinion()
        left_prom_exp = left[i].calcular_promedio_experticia()
        right_prom_exp = right[j].calcular_promedio_experticia()
        left_num_enc = len(left[i].encuestados)
        right_num_enc = len(right[j].encuestados)
        
        # Orden descendente por promedio opinión, luego experticia, luego número encuestados
        if (left_prom_op > right_prom_op or
            (left_prom_op == right_prom_op and left_prom_exp > right_prom_exp) or
            (left_prom_op == right_prom_op and left_prom_exp == right_prom_exp and left_num_enc > right_num_enc)):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    while i < len(left):
        result.append(left[i])
        i += 1
    
    while j < len(right):
        result.append(right[j])
        j += 1
    
    return result

def merge_sort_temas(temas):
    """Merge sort para temas"""
    if len(temas) <= 1:
        return temas[:]
    
    mid = len(temas) // 2
    left = merge_sort_temas(temas[:mid])
    right = merge_sort_temas(temas[mid:])
    
    return merge_temas(left, right)

def merge_temas(left, right):
    """Merge para temas"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        left_prom_op = left[i].calcular_promedio_total_opinion()
        right_prom_op = right[j].calcular_promedio_total_opinion()
        left_prom_exp = left[i].calcular_promedio_total_experticia()
        right_prom_exp = right[j].calcular_promedio_total_experticia()
        left_num_enc = left[i].calcular_total_encuestados()
        right_num_enc = right[j].calcular_total_encuestados()
        
        # Orden descendente por promedio opinión, luego experticia, luego número encuestados
        if (left_prom_op > right_prom_op or
            (left_prom_op == right_prom_op and left_prom_exp > right_prom_exp) or
            (left_prom_op == right_prom_op and left_prom_exp == right_prom_exp and left_num_enc > right_num_enc)):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    while i < len(left):
        result.append(left[i])
        i += 1
    
    while j < len(right):
        result.append(right[j])
        j += 1
    
    return result

def merge_sort_todos_encuestados(encuestados):
    """Merge sort para lista general de encuestados"""
    if len(encuestados) <= 1:
        return encuestados[:]
    
    mid = len(encuestados) // 2
    left = merge_sort_todos_encuestados(encuestados[:mid])
    right = merge_sort_todos_encuestados(encuestados[mid:])
    
    return merge_todos_encuestados(left, right)

def merge_todos_encuestados(left, right):
    """Merge para lista general de encuestados"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        # Orden descendente por experticia, luego por id (mayor primero)
        if (left[i].experticia > right[j].experticia or 
            (left[i].experticia == right[j].experticia and left[i].id > right[j].id)):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    while i < len(left):
        result.append(left[i])
        i += 1
    
    while j < len(right):
        result.append(right[j])
        j += 1
    
    return result


# ----------------- Funciones de lectura de archivos -----------------
def leer_archivo_entrada(ruta_archivo):
    """Lee el archivo de entrada y retorna encuestados y estructura de temas"""
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()
    
    # Limpiar líneas
    lineas = [linea.strip() for linea in lineas]
    
    # Separar encuestados de preguntas
    encuestados = []
    lineas_preguntas = []
    
    i = 0
    # Leer encuestados hasta línea vacía
    while i < len(lineas) and lineas[i] != '':
        linea = lineas[i]
        # Parsear: "Nombre, Experticia: X, Opinión: Y"
        partes = linea.split(', ')
        nombre = partes[0]
        experticia = int(partes[1].split(': ')[1])
        opinion = int(partes[2].split(': ')[1])
        
        encuestado = Encuestado(len(encuestados) + 1, nombre, experticia, opinion)
        encuestados.append(encuestado)
        i += 1
    
    # Saltar líneas vacías
    while i < len(lineas) and lineas[i] == '':
        i += 1
    
    # Leer estructura de preguntas
    temas = []
    tema_actual = -1  # Empezar en -1 para que el primer tema sea 0
    pregunta_actual = 1
    
    while i < len(lineas):
        if lineas[i] == '':
            # Saltar líneas vacías que separan temas
            if i < len(lineas) - 1 and i + 1 < len(lineas) and lineas[i + 1].startswith('{'):
                # Es una separación de tema
                tema_actual += 1
                pregunta_actual = 1
            i += 1
            continue
        
        if lineas[i].startswith('{') and lineas[i].endswith('}'):
            # Es una pregunta
            ids_str = lineas[i][1:-1]  # Quitar { }
            ids = [int(x.strip()) for x in ids_str.split(',')]
            
            # Si es la primera pregunta de todo, crear el primer tema
            if tema_actual == -1:
                tema_actual = 0
            
            # Crear tema si no existe
            while len(temas) <= tema_actual:
                temas.append(Tema(len(temas) + 1))
            
            # Crear pregunta
            pregunta = Pregunta(tema_actual + 1, pregunta_actual)
            
            # Agregar encuestados a la pregunta
            for id_encuestado in ids:
                pregunta.agregar_encuestado(encuestados[id_encuestado - 1])
            
            temas[tema_actual].agregar_pregunta(pregunta)
            pregunta_actual += 1
        
        i += 1
    
    return encuestados, temas


# ----------------- Funciones de búsqueda -----------------
def encontrar_pregunta_extrema(temas, criterio, es_maximo=True):
    """Encuentra pregunta con valor extremo según criterio"""
    mejor_pregunta = None
    mejor_valor = None
    mejor_tema_id = 0
    mejor_pregunta_id = 0
    
    for tema in temas:
        for pregunta in tema.preguntas:
            if criterio == "promedio_opinion":
                valor = pregunta.calcular_promedio_opinion()
            elif criterio == "promedio_experticia":
                valor = pregunta.calcular_promedio_experticia()
            elif criterio == "mediana":
                valor = pregunta.calcular_mediana_opinion()
            elif criterio == "moda":
                valor = pregunta.calcular_moda_opinion()
            elif criterio == "extremismo":
                valor = pregunta.calcular_extremismo()
            elif criterio == "consenso":
                valor = pregunta.calcular_consenso()
            
            if (mejor_valor is None or 
                (es_maximo and valor > mejor_valor) or 
                (not es_maximo and valor < mejor_valor) or
                (valor == mejor_valor and pregunta.tema_id < mejor_tema_id) or
                (valor == mejor_valor and pregunta.tema_id == mejor_tema_id and pregunta.pregunta_id < mejor_pregunta_id)):
                mejor_valor = valor
                mejor_tema_id = pregunta.tema_id
                mejor_pregunta_id = pregunta.pregunta_id
    
    return mejor_valor, mejor_tema_id, mejor_pregunta_id

def procesar_encuesta(ruta_archivo):
    """Función principal que procesa la encuesta"""
    # Leer datos
    encuestados, temas = leer_archivo_entrada(ruta_archivo)
    
    # Ordenar encuestados dentro de cada pregunta
    for tema in temas:
        for pregunta in tema.preguntas:
            pregunta.encuestados = merge_sort_encuestados_pregunta(pregunta.encuestados)
    
    # Ordenar preguntas dentro de cada tema
    for tema in temas:
        tema.preguntas = merge_sort_preguntas(tema.preguntas)
    
    # Ordenar temas
    temas = merge_sort_temas(temas)
    
    # Ordenar lista general de encuestados
    todos_encuestados = merge_sort_todos_encuestados(encuestados)
    
    # Generar salida
    resultado = []
    resultado.append("Resultados de la encuesta:")
    resultado.append("")
    
    # Mostrar temas y preguntas
    for tema in temas:
        promedio_tema = tema.calcular_promedio_total_opinion()
        resultado.append(f"[{promedio_tema:.2f}] Tema {tema.id}:")
        
        for pregunta in tema.preguntas:
            promedio_pregunta = pregunta.calcular_promedio_opinion()
            ids_encuestados = [str(enc.id) for enc in pregunta.encuestados]
            resultado.append(f" [{promedio_pregunta:.2f}] Pregunta {pregunta.tema_id}.{pregunta.pregunta_id}: ({', '.join(ids_encuestados)})")
        
        resultado.append("")
    
    # Lista de encuestados
    resultado.append("Lista de encuestados:")
    for encuestado in todos_encuestados:
        resultado.append(f" ({encuestado.id}, Nombre:'{encuestado.nombre}', Experticia:{encuestado.experticia}, Opinión:{encuestado.opinion})")
    
    resultado.append("")
    
    # Análisis estadístico
    resultado.append("Resultados:")
    
    # Mayor y menor promedio de opinión
    max_prom_op, max_tema, max_preg = encontrar_pregunta_extrema(temas, "promedio_opinion", True)
    min_prom_op, min_tema, min_preg = encontrar_pregunta_extrema(temas, "promedio_opinion", False)
    resultado.append(f"  Pregunta con mayor promedio de opinion: [{max_prom_op:.2f}] Pregunta: {max_tema}.{max_preg}")
    resultado.append(f"  Pregunta con menor promedio de opinion: [{min_prom_op:.2f}] Pregunta: {min_tema}.{min_preg}")
    
    # Mayor y menor promedio de experticia
    max_prom_exp, max_tema_exp, max_preg_exp = encontrar_pregunta_extrema(temas, "promedio_experticia", True)
    min_prom_exp, min_tema_exp, min_preg_exp = encontrar_pregunta_extrema(temas, "promedio_experticia", False)
    resultado.append(f"  Pregunta con mayor promedio de experticia: [{max_prom_exp:.2f}] Pregunta: {max_tema_exp}.{max_preg_exp}")
    resultado.append(f"  Pregunta con menor promedio de experticia: [{min_prom_exp:.2f}] Pregunta: {min_tema_exp}.{min_preg_exp}")
    
    # Mayor y menor mediana
    max_med, max_tema_med, max_preg_med = encontrar_pregunta_extrema(temas, "mediana", True)
    min_med, min_tema_med, min_preg_med = encontrar_pregunta_extrema(temas, "mediana", False)
    resultado.append(f"  Pregunta con Mayor mediana de opinion: [{max_med:.8g}] Pregunta: {max_tema_med}.{max_preg_med}")
    resultado.append(f"  Pregunta con menor mediana de opinion: [{min_med:.8g}] Pregunta: {min_tema_med}.{min_preg_med}")
    
    # Mayor y menor moda
    max_moda, max_tema_moda, max_preg_moda = encontrar_pregunta_extrema(temas, "moda", True)
    min_moda, min_tema_moda, min_preg_moda = encontrar_pregunta_extrema(temas, "moda", False)
    resultado.append(f"  Pregunta con mayor moda de opinion: [{max_moda:.8g}] Pregunta: {max_tema_moda}.{max_preg_moda}")
    resultado.append(f"  Pregunta con menor moda de opinion: [{min_moda:.8g}] Pregunta: {min_tema_moda}.{min_preg_moda}")
    
    # Mayor extremismo
    max_ext, max_tema_ext, max_preg_ext = encontrar_pregunta_extrema(temas, "extremismo", True)
    resultado.append(f"  Pregunta con mayor extremismo: [{max_ext:.2g}] Pregunta: {max_tema_ext}.{max_preg_ext}")
    
    # Mayor consenso
    max_cons, max_tema_cons, max_preg_cons = encontrar_pregunta_extrema(temas, "consenso", True)
    resultado.append(f"  Pregunta con mayor consenso: [{max_cons:.2g}] Pregunta: {max_tema_cons}.{max_preg_cons}")
    
    resultado.append("")
    
    return '\n'.join(resultado)


# ----------------- Función principal para ejecutar -----------------
def main():
    if len(sys.argv) != 2:
        print("Uso: python solucion1.py <archivo_entrada>")
        return
    
    ruta_archivo = sys.argv[1]
    
    if not os.path.exists(ruta_archivo):
        print(f"Error: El archivo {ruta_archivo} no existe")
        return
    
    try:
        resultado = procesar_encuesta(ruta_archivo)
        print(resultado)
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")

if __name__ == "__main__":
    main()
