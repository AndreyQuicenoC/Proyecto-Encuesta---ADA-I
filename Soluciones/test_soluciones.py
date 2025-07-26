#!/usr/bin/env python3
"""
Script para probar ambas soluciones del problema de procesamiento de encuesta
Ejecuta las dos soluciones con todos los archivos de prueba disponibles
"""

import os
import sys
import subprocess
import time

def ejecutar_solucion(script_path, archivo_entrada):
    """Ejecuta una solución y retorna la salida y el tiempo de ejecución"""
    try:
        inicio = time.time()
        resultado = subprocess.run(
            [sys.executable, script_path, archivo_entrada],
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='replace'  # Manejo de errores de codificación
        )
        fin = time.time()
        
        if resultado.returncode != 0:
            return None, 0, f"Error: {resultado.stderr}"
        
        return resultado.stdout, fin - inicio, None
    except Exception as e:
        return None, 0, f"Excepción: {str(e)}"

def main():
    # Rutas de las soluciones
    solucion1_path = os.path.join("Solucion1_Arreglos", "solucion1.py")
    solucion2_path = os.path.join("Solucion2_Diccionarios", "solucion2.py")
    
    # Archivos de prueba
    archivos_prueba = [
        os.path.join("..", "Contexto", "Datos de entrada", "Test1.txt"),
        os.path.join("..", "Contexto", "Datos de entrada", "Test2.txt"),
        os.path.join("..", "Contexto", "Datos de entrada", "Test3.txt"),
        os.path.join("..", "Contexto", "Datos de entrada", "Test4.txt"),
        os.path.join("..", "Contexto", "Datos de entrada", "Test5.txt"),
        os.path.join("..", "Contexto", "Datos de entrada", "Test6.txt")

    ]
    
    # Variables para recopilar tiempos
    tiempos_solucion1 = []
    tiempos_solucion2 = []
    nombres_archivos = []
    
    print("=" * 80)
    print("PRUEBA DE SOLUCIONES - PROBLEMA DE PROCESAMIENTO DE ENCUESTA")
    print("=" * 80)
    print()
    
    # Verificar que existan las soluciones
    if not os.path.exists(solucion1_path):
        print(f"Error: No se encontró {solucion1_path}")
        return
    
    if not os.path.exists(solucion2_path):
        print(f"Error: No se encontró {solucion2_path}")
        return
    
    # Ejecutar pruebas
    for i, archivo in enumerate(archivos_prueba, 1):
        if not os.path.exists(archivo):
            print(f"Archivo de prueba {archivo} no encontrado, saltando...")
            continue
        
        print(f"PRUEBA {i}: {os.path.basename(archivo)}")
        print("-" * 60)
        
        # Ejecutar Solución 1
        print("Ejecutando Solución 1 (Arreglos + Merge Sort)...")
        salida1, tiempo1, error1 = ejecutar_solucion(solucion1_path, archivo)
        
        if error1:
            print(f"Error en Solución 1: {error1}")
            tiempo1 = None
        else:
            print(f"Solución 1 completada en {tiempo1:.4f} segundos")
        
        # Ejecutar Solución 2
        print("Ejecutando Solución 2 (Diccionarios + BST)...")
        salida2, tiempo2, error2 = ejecutar_solucion(solucion2_path, archivo)
        
        if error2:
            print(f"Error en Solución 2: {error2}")
            tiempo2 = None
        else:
            print(f"Solución 2 completada en {tiempo2:.4f} segundos")
        
        # Guardar datos para el resumen final
        nombres_archivos.append(os.path.basename(archivo))
        tiempos_solucion1.append(tiempo1)
        tiempos_solucion2.append(tiempo2)
        
        # Comparar resultados
        if salida1 and salida2:
            if salida1.strip() == salida2.strip():
                print("✅ Las salidas de ambas soluciones son idénticas")
                
                # Mostrar comparación de tiempos
                if tiempo1 and tiempo2:
                    if tiempo1 < tiempo2:
                        diferencia = ((tiempo2 - tiempo1) / tiempo1) * 100
                        print(f"⚡ Solución 1 es {diferencia:.1f}% más rápida")
                    elif tiempo2 < tiempo1:
                        diferencia = ((tiempo1 - tiempo2) / tiempo2) * 100
                        print(f"⚡ Solución 2 es {diferencia:.1f}% más rápida")
                    else:
                        print("⚡ Ambas soluciones tienen tiempos similares")
            else:
                print("Las salidas de las soluciones son diferentes")
                print("\nPrimeras diferencias encontradas:")
                lineas1 = salida1.strip().split('\\n')
                lineas2 = salida2.strip().split('\\n')
                
                for j, (l1, l2) in enumerate(zip(lineas1, lineas2)):
                    if l1 != l2:
                        print(f"  Línea {j+1}:")
                        print(f"    Sol1: {l1}")
                        print(f"    Sol2: {l2}")
                        break
        
        # Mostrar una muestra de la salida
        if salida1:
            print("\\nMuestra de salida (primeras 10 líneas):")
            lineas = salida1.strip().split('\\n')
            for j, linea in enumerate(lineas[:10]):
                print(f"  {j+1:2}: {linea}")
            if len(lineas) > 10:
                print(f"  ... ({len(lineas) - 10} líneas más)")
        
        print("\\n" + "=" * 80 + "\\n")
    
    # RESUMEN FINAL DE RENDIMIENTO
    print("RESUMEN FINAL DE RENDIMIENTO")
    print("=" * 80)
    
    # Filtrar tiempos válidos
    tiempos_validos_sol1 = [t for t in tiempos_solucion1 if t is not None]
    tiempos_validos_sol2 = [t for t in tiempos_solucion2 if t is not None]
    
    if tiempos_validos_sol1 and tiempos_validos_sol2:
        print("\\n📈 Comparación de tiempos por archivo:")
        print("-" * 50)
        
        for i, nombre in enumerate(nombres_archivos):
            if tiempos_solucion1[i] is not None and tiempos_solucion2[i] is not None:
                t1 = tiempos_solucion1[i]
                t2 = tiempos_solucion2[i]
                print(f"  {nombre:12}: Sol1={t1:.4f}s  Sol2={t2:.4f}s", end="")
                
                if t1 < t2:
                    diferencia = ((t2 - t1) / t1) * 100
                    print(f"  Sol1 +{diferencia:.1f}%")
                elif t2 < t1:
                    diferencia = ((t1 - t2) / t2) * 100
                    print(f"  Sol2 +{diferencia:.1f}%")
                else:
                    print("  Empate")
        
        # Estadísticas generales
        tiempo_total_sol1 = sum(tiempos_validos_sol1)
        tiempo_total_sol2 = sum(tiempos_validos_sol2)
        tiempo_promedio_sol1 = tiempo_total_sol1 / len(tiempos_validos_sol1)
        tiempo_promedio_sol2 = tiempo_total_sol2 / len(tiempos_validos_sol2)
        
        print("\\nEstadísticas generales:")
        print("-" * 50)
        print(f"  Solución 1 (Arreglos + Merge Sort):")
        print(f"    • Tiempo total:    {tiempo_total_sol1:.4f}s")
        print(f"    • Tiempo promedio: {tiempo_promedio_sol1:.4f}s")
        print(f"    • Tiempo mínimo:   {min(tiempos_validos_sol1):.4f}s")
        print(f"    • Tiempo máximo:   {max(tiempos_validos_sol1):.4f}s")
        
        print(f"\\n  Solución 2 (Diccionarios + BST):")
        print(f"    • Tiempo total:    {tiempo_total_sol2:.4f}s")
        print(f"    • Tiempo promedio: {tiempo_promedio_sol2:.4f}s")
        print(f"    • Tiempo mínimo:   {min(tiempos_validos_sol2):.4f}s")
        print(f"    • Tiempo máximo:   {max(tiempos_validos_sol2):.4f}s")
        
        # Ganador general
        print("\\nVEREDICTO FINAL:")
        print("-" * 50)
        if tiempo_promedio_sol1 < tiempo_promedio_sol2:
            mejora = ((tiempo_promedio_sol2 - tiempo_promedio_sol1) / tiempo_promedio_sol1) * 100
            print(f"Solución 1 (Arreglos + Merge Sort) es {mejora:.1f}% más rápida en promedio")
            print("   Merge Sort muestra mejor rendimiento general")
        elif tiempo_promedio_sol2 < tiempo_promedio_sol1:
            mejora = ((tiempo_promedio_sol1 - tiempo_promedio_sol2) / tiempo_promedio_sol2) * 100
            print(f"Solución 2 (Diccionarios + BST) es {mejora:.1f}% más rápida en promedio")
            print("   BST muestra mejor rendimiento general")
        else:
            print("Ambas soluciones tienen rendimiento similar")
            print("   Ambos algoritmos son eficientes para este problema")
        
        # Análisis técnico
        print("\\nANÁLISIS TÉCNICO:")
        print("-" * 50)
        print("  • Merge Sort:     O(n log n) garantizado, estable")
        print("  • BST:           O(n log n) promedio, O(n²) peor caso")
    else:
        print("\\n  No se pudieron recopilar suficientes datos de tiempo para el resumen")
    
    print("\\n" + "=" * 80)
    print("Pruebas completadas!")
    print("\\nPara ver la salida completa de una solución específica, ejecuta:")
    print(f"   python {solucion1_path} <archivo_entrada>")
    print(f"   python {solucion2_path} <archivo_entrada>")

if __name__ == "__main__":
    main()
