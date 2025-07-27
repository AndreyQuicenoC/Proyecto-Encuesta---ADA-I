"""
SOLUCIÓN 2: PROCESAMIENTO DE ENCUESTA CON DICCIONARIOS Y ÁRBOLES
Algoritmo de ordenamiento: Árbol Binario de Búsqueda (BST)
Estructuras de datos: Diccionarios y Árboles Binarios exclusivamente

Autor: Proyecto ADA I - Universidad del Valle
"""

import sys
import os

# Aumentar límite de recursión para manejar archivos grandes
sys.setrecursionlimit(15000)

# ----------------- CLASES PARA EL ÁRBOL BINARIO DE BÚSQUEDA -----------------
class NodoArbol:
    """Nodo para Árbol Binario de Búsqueda"""
    def __init__(self, clave, valor, comparador=None):
        self.clave = clave
        self.valor = valor
        self.izquierdo = None
        self.derecho = None
        self.comparador = comparador  # Función para comparar valores
    
    def insertar(self, clave, valor):
        """Inserta un nuevo nodo en el árbol"""
        if self.comparador:
            # Usar comparador personalizado
            if self.comparador(valor, self.valor):
                if self.izquierdo is None:
                    self.izquierdo = NodoArbol(clave, valor, self.comparador)
                else:
                    self.izquierdo.insertar(clave, valor)
            else:
                if self.derecho is None:
                    self.derecho = NodoArbol(clave, valor, self.comparador)
                else:
                    self.derecho.insertar(clave, valor)
        else:
            # Comparación por clave por defecto
            if clave < self.clave:
                if self.izquierdo is None:
                    self.izquierdo = NodoArbol(clave, valor, self.comparador)
                else:
                    self.izquierdo.insertar(clave, valor)
            else:
                if self.derecho is None:
                    self.derecho = NodoArbol(clave, valor, self.comparador)
                else:
                    self.derecho.insertar(clave, valor)
    
    def recorrido_inorden(self, resultado):
        """Recorrido en orden del árbol (retorna elementos ordenados)"""
        if self.izquierdo:
            self.izquierdo.recorrido_inorden(resultado)
        resultado[self.clave] = self.valor
        if self.derecho:
            self.derecho.recorrido_inorden(resultado)

class ArbolBST:
    """Árbol Binario de Búsqueda para ordenamiento"""
    def __init__(self, comparador=None):
        self.raiz = None
        self.comparador = comparador
    
    def insertar(self, clave, valor):
        """Inserta un elemento en el árbol"""
        if self.raiz is None:
            self.raiz = NodoArbol(clave, valor, self.comparador)
        else:
            self.raiz.insertar(clave, valor)
    
    def obtener_ordenado(self):
        """Retorna diccionario con elementos ordenados"""
        if self.raiz is None:
            return {}
        
        resultado = {}
        self.raiz.recorrido_inorden(resultado)
        
        return resultado


# ----------------- FUNCIONES PARA CREAR ESTRUCTURAS DE DATOS -----------------
def crear_encuestado(id, nombre, experticia, opinion):
    """Crea un diccionario que representa un encuestado"""
    return {
        'id': id,
        'nombre': nombre,
        'experticia': experticia,
        'opinion': opinion
    }

def crear_pregunta(tema_id, pregunta_id):
    """Crea un diccionario que representa una pregunta"""
    return {
        'tema_id': tema_id,
        'pregunta_id': pregunta_id,
        'encuestados': {},  # Diccionario con id como clave
        'estadisticas': {}
    }

def crear_tema(id):
    """Crea un diccionario que representa un tema"""
    return {
        'id': id,
        'preguntas': {},  # Diccionario con pregunta_id como clave
        'estadisticas': {}
    }


# ----------------- FUNCIONES PARA CALCULAR ESTADÍSTICAS -----------------
def calcular_estadisticas_pregunta(pregunta):
    """Calcula todas las estadísticas de una pregunta"""
    encuestados = pregunta['encuestados']
    
    if len(encuestados) == 0:
        pregunta['estadisticas'] = {
            'promedio_opinion': 0.0,
            'promedio_experticia': 0.0,
            'mediana_opinion': 0,
            'moda_opinion': 0,
            'extremismo': 0.0,
            'consenso': 0.0,
            'num_encuestados': 0
        }
        return
    
    # Extraer opiniones y experticías
    opiniones = {}
    experticías = {}
    for id_enc, encuestado in encuestados.items():
        opiniones[id_enc] = encuestado['opinion']
        experticías[id_enc] = encuestado['experticia']
    
    # Promedio de opinión
    suma_opinion = sum(opiniones.values())
    promedio_opinion = suma_opinion / len(opiniones)
    
    # Promedio de experticia
    suma_experticia = sum(experticías.values())
    promedio_experticia = suma_experticia / len(experticías)
    
    # Mediana de opinión
    mediana = calcular_mediana_con_bst(opiniones)
    
    # Moda de opinión
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
            if moda is None or valor < moda:  # En caso de empate, tomar el menor
                moda = valor
    
    # Extremismo
    extremos = 0
    for op in opiniones.values():
        if op == 0 or op == 10:
            extremos += 1
    extremismo = extremos / len(opiniones)
    
    # Consenso
    consenso = max_frecuencia / len(opiniones)
    
    pregunta['estadisticas'] = {
        'promedio_opinion': promedio_opinion,
        'promedio_experticia': promedio_experticia,
        'mediana_opinion': mediana,
        'moda_opinion': moda,
        'extremismo': extremismo,
        'consenso': consenso,
        'num_encuestados': len(encuestados)
    }

def calcular_estadisticas_tema(tema):
    """Calcula estadísticas de un tema"""
    preguntas = tema['preguntas']
    
    if len(preguntas) == 0:
        tema['estadisticas'] = {
            'promedio_total_opinion': 0.0,
            'promedio_total_experticia': 0.0,
            'total_encuestados': 0
        }
        return
    
    suma_prom_opinion = 0
    suma_prom_experticia = 0
    total_encuestados = 0
    
    for pregunta in preguntas.values():
        suma_prom_opinion += pregunta['estadisticas']['promedio_opinion']
        suma_prom_experticia += pregunta['estadisticas']['promedio_experticia']
        total_encuestados += pregunta['estadisticas']['num_encuestados']
    
    tema['estadisticas'] = {
        'promedio_total_opinion': suma_prom_opinion / len(preguntas),
        'promedio_total_experticia': suma_prom_experticia / len(preguntas),
        'total_encuestados': total_encuestados
    }


# ----------------- FUNCIONES PARA ORDENAMIENTO CON ÁRBOL BINARIO DE BÚSQUEDA -----------------
def calcular_mediana_con_bst(opiniones_dict):
    """Calcula mediana usando BST"""
    if len(opiniones_dict) == 0:
        return 0
    
    # Crear BST para ordenar opiniones
    arbol = ArbolBST()
    frecuencias = {}
    
    # Contar frecuencias y construir BST
    for opinion in opiniones_dict.values():
        if opinion in frecuencias:
            frecuencias[opinion] += 1
        else:
            frecuencias[opinion] = 1
            arbol.insertar(opinion, opinion)
    
    # Obtener valores ordenados
    valores_ordenados = arbol.obtener_ordenado()
    
    # Expandir según frecuencias para encontrar mediana
    total_elementos = len(opiniones_dict)
    if total_elementos % 2 == 1:  # Impar - posición central
        posicion_mediana = total_elementos // 2
    else:  # Par - posición del menor de los dos centrales  
        posicion_mediana = total_elementos // 2 - 1
    
    contador = 0
    for valor in valores_ordenados.keys():
        contador += frecuencias[valor]
        if total_elementos % 2 == 1:  # Impar
            if contador > posicion_mediana:
                return valor
        else:  # Par
            if contador > posicion_mediana:
                return valor
    
    # Fallback usando next() para obtener primera clave sin list()
    # Caso por defecto
    return next(iter(valores_ordenados.keys())) if valores_ordenados else 0

def bst_encuestados_pregunta(encuestados_dict):
    """BST para encuestados en una pregunta (descendente por opinión, luego experticia)"""
    if len(encuestados_dict) <= 1:
        return encuestados_dict
    
    def comparar_encuestados(enc_a, enc_b):
        """Retorna True si enc_a debe ir antes que enc_b (orden descendente)"""
        if enc_a['opinion'] > enc_b['opinion']:
            return True
        elif enc_a['opinion'] == enc_b['opinion']:
            if enc_a['experticia'] > enc_b['experticia']:
                return True
            elif enc_a['experticia'] == enc_b['experticia']:
                return enc_a['id'] < enc_b['id']  # Desempate por ID ascendente
        return False
    
    arbol = ArbolBST(comparar_encuestados)
    
    # Insertar encuestados en el árbol
    for id_enc, encuestado in encuestados_dict.items():
        arbol.insertar(id_enc, encuestado)
    
    return arbol.obtener_ordenado()

def bst_preguntas(preguntas_dict):
    """BST para preguntas en un tema"""
    if len(preguntas_dict) <= 1:
        return preguntas_dict
    
    def comparar_preguntas(preg_a, preg_b):
        """Retorna True si preg_a debe ir antes que preg_b"""
        stats_a = preg_a['estadisticas']
        stats_b = preg_b['estadisticas']
        
        if stats_a['promedio_opinion'] > stats_b['promedio_opinion']:
            return True
        elif stats_a['promedio_opinion'] == stats_b['promedio_opinion']:
            if stats_a['promedio_experticia'] > stats_b['promedio_experticia']:
                return True
            elif stats_a['promedio_experticia'] == stats_b['promedio_experticia']:
                return stats_a['num_encuestados'] > stats_b['num_encuestados']
        return False
    
    arbol = ArbolBST(comparar_preguntas)
    
    # Insertar preguntas en el árbol
    for pregunta_id, pregunta in preguntas_dict.items():
        arbol.insertar(pregunta_id, pregunta)
    
    return arbol.obtener_ordenado()

def bst_temas(temas_dict):
    """BST para temas"""
    if len(temas_dict) <= 1:
        return temas_dict
    
    def comparar_temas(tema_a, tema_b):
        """Retorna True si tema_a debe ir antes que tema_b"""
        stats_a = tema_a['estadisticas']
        stats_b = tema_b['estadisticas']
        
        if stats_a['promedio_total_opinion'] > stats_b['promedio_total_opinion']:
            return True
        elif stats_a['promedio_total_opinion'] == stats_b['promedio_total_opinion']:
            if stats_a['promedio_total_experticia'] > stats_b['promedio_total_experticia']:
                return True
            elif stats_a['promedio_total_experticia'] == stats_b['promedio_total_experticia']:
                return stats_a['total_encuestados'] > stats_b['total_encuestados']
        return False
    
    arbol = ArbolBST(comparar_temas)
    
    # Insertar temas en el árbol
    for tema_id, tema in temas_dict.items():
        arbol.insertar(tema_id, tema)
    
    return arbol.obtener_ordenado()

def bst_todos_encuestados(encuestados_dict):
    """BST para lista general de encuestados"""
    if len(encuestados_dict) <= 1:
        return encuestados_dict
    
    def comparar_todos_encuestados(enc_a, enc_b):
        """Retorna True si enc_a debe ir antes que enc_b"""
        if enc_a['experticia'] > enc_b['experticia']:
            return True
        elif enc_a['experticia'] == enc_b['experticia']:
            return enc_a['id'] > enc_b['id']
        return False
    
    arbol = ArbolBST(comparar_todos_encuestados)
    
    # Insertar encuestados en el árbol
    for id_enc, encuestado in encuestados_dict.items():
        arbol.insertar(id_enc, encuestado)
    
    return arbol.obtener_ordenado()


# ----------------- FUNCIONES PARA LEER Y PROCESAR ARCHIVOS DE ENTRADA -----------------
def leer_archivo_entrada(ruta_archivo):
    """Lee el archivo de entrada y retorna diccionarios de encuestados y temas"""
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()
    
    lineas = [linea.strip() for linea in lineas]
    
    # Diccionario de todos los encuestados
    encuestados = {}
    # Diccionario de temas
    temas = {}
    
    i = 0
    # Leer encuestados
    while i < len(lineas) and lineas[i] != '':
        linea = lineas[i]
        partes = linea.split(', ')
        nombre = partes[0]
        experticia = int(partes[1].split(': ')[1])
        opinion = int(partes[2].split(': ')[1])
        
        id_encuestado = len(encuestados) + 1
        encuestados[id_encuestado] = crear_encuestado(id_encuestado, nombre, experticia, opinion)
        i += 1
    
    # Saltar líneas vacías
    while i < len(lineas) and lineas[i] == '':
        i += 1
    
    # Leer estructura de preguntas
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
            ids_str = lineas[i][1:-1]
            ids = [int(x.strip()) for x in ids_str.split(',')]
            
            # Si es la primera pregunta de todo, crear el primer tema
            if tema_actual == -1:
                tema_actual = 0
            
            # Crear tema si no existe
            tema_id = tema_actual + 1
            if tema_id not in temas:
                temas[tema_id] = crear_tema(tema_id)
            
            # Crear pregunta
            pregunta = crear_pregunta(tema_id, pregunta_actual)
            
            # Agregar encuestados a la pregunta
            for id_encuestado in ids:
                pregunta['encuestados'][id_encuestado] = encuestados[id_encuestado]
            
            temas[tema_id]['preguntas'][pregunta_actual] = pregunta
            pregunta_actual += 1
        
        i += 1
    
    return encuestados, temas


# ----------------- FUNCIONES PARA ENCONTRAR PREGUNTAS EXTREMAS -----------------
def encontrar_pregunta_extrema(temas, criterio, es_maximo=True):
    """Encuentra pregunta con valor extremo según criterio"""
    mejor_valor = None
    mejor_tema_id = 0
    mejor_pregunta_id = 0
    
    for tema_id, tema in temas.items():
        for pregunta_id, pregunta in tema['preguntas'].items():
            stats = pregunta['estadisticas']
            
            if criterio == "promedio_opinion":
                valor = stats['promedio_opinion']
            elif criterio == "promedio_experticia":
                valor = stats['promedio_experticia']
            elif criterio == "mediana":
                valor = stats['mediana_opinion']
            elif criterio == "moda":
                valor = stats['moda_opinion']
            elif criterio == "extremismo":
                valor = stats['extremismo']
            elif criterio == "consenso":
                valor = stats['consenso']
            
            if (mejor_valor is None or 
                (es_maximo and valor > mejor_valor) or 
                (not es_maximo and valor < mejor_valor) or
                (valor == mejor_valor and tema_id < mejor_tema_id) or
                (valor == mejor_valor and tema_id == mejor_tema_id and pregunta_id < mejor_pregunta_id)):
                mejor_valor = valor
                mejor_tema_id = tema_id
                mejor_pregunta_id = pregunta_id
    
    return mejor_valor, mejor_tema_id, mejor_pregunta_id

def procesar_encuesta(ruta_archivo):
    """Función principal que procesa la encuesta"""
    # Leer datos
    encuestados, temas = leer_archivo_entrada(ruta_archivo)
    
    # Calcular estadísticas de preguntas
    for tema in temas.values():
        for pregunta in tema['preguntas'].values():
            calcular_estadisticas_pregunta(pregunta)
    
    # Calcular estadísticas de temas
    for tema in temas.values():
        calcular_estadisticas_tema(tema)
    
    # Ordenar encuestados dentro de cada pregunta
    for tema in temas.values():
        for pregunta_id, pregunta in tema['preguntas'].items():
            pregunta['encuestados'] = bst_encuestados_pregunta(pregunta['encuestados'])
    
    # Ordenar preguntas dentro de cada tema
    for tema_id, tema in temas.items():
        tema['preguntas'] = bst_preguntas(tema['preguntas'])
    
    # Ordenar temas
    temas = bst_temas(temas)
    
    # Ordenar lista general de encuestados
    encuestados_ordenados = bst_todos_encuestados(encuestados)
    
    # Generar salida
    resultado = "Resultados de la encuesta:\n\n"
    
    # Mostrar temas y preguntas
    for tema_id, tema in temas.items():
        promedio_tema = tema['estadisticas']['promedio_total_opinion']
        resultado += f"[{promedio_tema:.2f}] Tema {tema_id}:\n"
        
        for pregunta_id, pregunta in tema['preguntas'].items():
            promedio_pregunta = pregunta['estadisticas']['promedio_opinion']
            # Usar diccionario para construir string de IDs
            ids_str = ""
            for i, id_enc in enumerate(pregunta['encuestados'].keys()):
                if i > 0:
                    ids_str += ", "
                ids_str += str(id_enc)
            resultado += f" [{promedio_pregunta:.2f}] Pregunta {tema_id}.{pregunta_id}: ({ids_str})\n"
        
        resultado += "\n"
    
    # Lista de encuestados
    resultado += "Lista de encuestados:\n"
    for id_enc, encuestado in encuestados_ordenados.items():
        resultado += f" ({id_enc}, Nombre:'{encuestado['nombre']}', Experticia:{encuestado['experticia']}, Opinión:{encuestado['opinion']})\n"
    
    resultado += "\n"
    
    # Análisis estadístico
    resultado += "Resultados:\n"
    
    # Mayor y menor promedio de opinión
    max_prom_op, max_tema, max_preg = encontrar_pregunta_extrema(temas, "promedio_opinion", True)
    min_prom_op, min_tema, min_preg = encontrar_pregunta_extrema(temas, "promedio_opinion", False)
    resultado += f"  Pregunta con mayor promedio de opinion: [{max_prom_op:.2f}] Pregunta: {max_tema}.{max_preg}\n"
    resultado += f"  Pregunta con menor promedio de opinion: [{min_prom_op:.2f}] Pregunta: {min_tema}.{min_preg}\n"
    
    # Mayor y menor promedio de experticia
    max_prom_exp, max_tema_exp, max_preg_exp = encontrar_pregunta_extrema(temas, "promedio_experticia", True)
    min_prom_exp, min_tema_exp, min_preg_exp = encontrar_pregunta_extrema(temas, "promedio_experticia", False)
    resultado += f"  Pregunta con mayor promedio de experticia: [{max_prom_exp:.2f}] Pregunta: {max_tema_exp}.{max_preg_exp}\n"
    resultado += f"  Pregunta con menor promedio de experticia: [{min_prom_exp:.2f}] Pregunta: {min_tema_exp}.{min_preg_exp}\n"
    
    # Mayor y menor mediana
    max_med, max_tema_med, max_preg_med = encontrar_pregunta_extrema(temas, "mediana", True)
    min_med, min_tema_med, min_preg_med = encontrar_pregunta_extrema(temas, "mediana", False)
    resultado += f"  Pregunta con Mayor mediana de opinion: [{max_med:.8g}] Pregunta: {max_tema_med}.{max_preg_med}\n"
    resultado += f"  Pregunta con menor mediana de opinion: [{min_med:.8g}] Pregunta: {min_tema_med}.{min_preg_med}\n"
    
    # Mayor y menor moda
    max_moda, max_tema_moda, max_preg_moda = encontrar_pregunta_extrema(temas, "moda", True)
    min_moda, min_tema_moda, min_preg_moda = encontrar_pregunta_extrema(temas, "moda", False)
    resultado += f"  Pregunta con mayor moda de opinion: [{max_moda:.8g}] Pregunta: {max_tema_moda}.{max_preg_moda}\n"
    resultado += f"  Pregunta con menor moda de opinion: [{min_moda:.8g}] Pregunta: {min_tema_moda}.{min_preg_moda}\n"
    
    # Mayor extremismo
    max_ext, max_tema_ext, max_preg_ext = encontrar_pregunta_extrema(temas, "extremismo", True)
    resultado += f"  Pregunta con mayor extremismo: [{max_ext:.2g}] Pregunta: {max_tema_ext}.{max_preg_ext}\n"
    
    # Mayor consenso
    max_cons, max_tema_cons, max_preg_cons = encontrar_pregunta_extrema(temas, "consenso", True)
    resultado += f"  Pregunta con mayor consenso: [{max_cons:.2g}] Pregunta: {max_tema_cons}.{max_preg_cons}\n"
    
    resultado += "\n"
    
    return resultado


# ----------------- FUNCIONES PRINCIPALES -----------------
def main():
    if len(sys.argv) != 2:
        print("Uso: python solucion2.py <archivo_entrada>")
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
