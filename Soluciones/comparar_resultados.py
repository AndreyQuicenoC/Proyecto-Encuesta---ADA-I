#!/usr/bin/env python3
"""
Para comparar los resultados de ambas soluciones
Verifica que las salidas sean idénticas y analiza diferencias si las hay
"""

import os
import sys
import subprocess
import difflib

# Configurar encoding para Windows
if sys.platform.startswith('win'):
    import locale
    locale.setlocale(locale.LC_ALL, '')
    os.environ['PYTHONIOENCODING'] = 'utf-8'

def ejecutar_solucion(script_path, archivo_entrada):
    """Ejecuta una solución y retorna la salida"""
    try:
        # Para Windows, usar una configuración más robusta
        if sys.platform.startswith('win'):
            resultado = subprocess.run(
                [sys.executable, script_path, archivo_entrada],
                capture_output=True,
                text=True,
                encoding='utf-8',
                errors='replace',
                creationflags=subprocess.CREATE_NO_WINDOW
            )
        else:
            resultado = subprocess.run(
                [sys.executable, script_path, archivo_entrada],
                capture_output=True,
                text=True,
                encoding='utf-8',
                errors='replace'
            )
        
        if resultado.returncode != 0:
            return None, f"Error: {resultado.stderr}"
        
        return resultado.stdout.strip(), None
    except Exception as e:
        return None, f"Excepción: {str(e)}"

def comparar_salidas(salida1, salida2, nombre_archivo):
    """Compara dos salidas y muestra diferencias detalladas"""
    lineas1 = salida1.split('\\n')
    lineas2 = salida2.split('\\n')
    
    print(f"\\nCOMPARACIÓN PARA {nombre_archivo}")
    print("-" * 60)
    
    if salida1 == salida2:
        print("Las salidas son IDÉNTICAS")
        return True
    
    print("Las salidas son DIFERENTES")
    
    # Mostrar estadísticas básicas
    print(f"  Longitud Solución 1: {len(lineas1)} líneas")
    print(f"  Longitud Solución 2: {len(lineas2)} líneas")
    
    # Usar difflib para mostrar diferencias detalladas
    print("\\nDIFERENCIAS DETALLADAS:")
    print("-" * 40)
    
    differ = difflib.unified_diff(
        lineas1, 
        lineas2, 
        fromfile='Solución 1 (Arreglos + Merge Sort)',
        tofile='Solución 2 (Diccionarios + Quick Sort)',
        lineterm=''
    )
    
    diferencias = list(differ)
    if diferencias:
        for linea in diferencias[:50]:  # Mostrar máximo 50 líneas de diferencias
            print(linea)
        
        if len(diferencias) > 50:
            print(f"\\n... ({len(diferencias) - 50} líneas más de diferencias)")
    
    # Análisis línea por línea para las primeras diferencias
    print("\\nANÁLISIS LÍNEA POR LÍNEA (primeras 5 diferencias):")
    print("-" * 50)
    
    diferencias_encontradas = 0
    for i, (l1, l2) in enumerate(zip(lineas1, lineas2)):
        if l1 != l2:
            diferencias_encontradas += 1
            if diferencias_encontradas <= 5:
                print(f"\\nLínea {i+1}:")
                print(f"  Sol1: '{l1}'")
                print(f"  Sol2: '{l2}'")
                
                # Mostrar diferencias a nivel de carácter
                if len(l1) != len(l2):
                    print(f"  Longitudes diferentes: {len(l1)} vs {len(l2)}")
                
                # Encontrar primer carácter diferente
                for j, (c1, c2) in enumerate(zip(l1, l2)):
                    if c1 != c2:
                        print(f"  Primera diferencia en posición {j}: '{c1}' vs '{c2}'")
                        break
    
    if diferencias_encontradas > 5:
        print(f"\\n... ({diferencias_encontradas - 5} diferencias más encontradas)")
    
    return False

def guardar_salidas(salida1, salida2, nombre_archivo):
    """Guarda las salidas en archivos para comparación manual"""
    base_name = os.path.splitext(nombre_archivo)[0]
    
    with open(f"salida_sol1_{base_name}.txt", 'w', encoding='utf-8') as f:
        f.write(salida1)
    
    with open(f"salida_sol2_{base_name}.txt", 'w', encoding='utf-8') as f:
        f.write(salida2)
    
    print(f"\\nSalidas guardadas en:")
    print(f"  - salida_sol1_{base_name}.txt")
    print(f"  - salida_sol2_{base_name}.txt")

def main():
    # Rutas de las soluciones
    solucion1_path = os.path.join("Solucion1_Arreglos", "solucion1.py")
    solucion2_path = os.path.join("Solucion2_Diccionarios", "solucion2.py")
    
    # Archivos de prueba
    archivos_prueba = [
        os.path.join("..", "Contexto", "Datos de entrada", "Test1.txt"),
        os.path.join("..", "Contexto", "Datos de entrada", "Test2.txt"),
        os.path.join("..", "Contexto", "Datos de entrada", "Test3.txt")
    ]
    
    print("=" * 80)
    print("COMPARACIÓN DE RESULTADOS - SOLUCIONES DE ENCUESTA")
    print("=" * 80)
    
    # Verificar que existan las soluciones
    if not os.path.exists(solucion1_path):
        print(f"Error: No se encontró {solucion1_path}")
        return
    
    if not os.path.exists(solucion2_path):
        print(f"Error: No se encontró {solucion2_path}")
        return
    
    todas_identicas = True
    
    for archivo in archivos_prueba:
        if not os.path.exists(archivo):
            print(f"Archivo {archivo} no encontrado, saltando...")
            continue
        
        nombre_archivo = os.path.basename(archivo)
        print(f"\\nPROCESANDO: {nombre_archivo}")
        print("=" * 60)
        
        # Ejecutar ambas soluciones
        print("Ejecutando Solución 1...")
        salida1, error1 = ejecutar_solucion(solucion1_path, archivo)
        
        if error1:
            print(f"Error en Solución 1: {error1}")
            continue
        
        print("Ejecutando Solución 2...")
        salida2, error2 = ejecutar_solucion(solucion2_path, archivo)
        
        if error2:
            print(f"Error en Solución 2: {error2}")
            continue
        
        # Comparar resultados
        son_identicas = comparar_salidas(salida1, salida2, nombre_archivo)
        
        if not son_identicas:
            todas_identicas = False
            guardar_salidas(salida1, salida2, nombre_archivo)
        
        print("\\n" + "=" * 80)
    
    # Resumen final
    print("\\nRESUMEN FINAL:")
    print("-" * 30)
    
    if todas_identicas:
        print("¡ÉXITO! Todas las salidas son idénticas")
        print("Ambas soluciones producen resultados correctos")
    else:
        print("Se encontraron diferencias entre las soluciones")
        print("Revisa los archivos de salida generados para más detalles")
    
    print("\\n💡 Tip: Para comparar manualmente, usa:")
    print("   diff salida_sol1_TestX.txt salida_sol2_TestX.txt")

if __name__ == "__main__":
    main()
