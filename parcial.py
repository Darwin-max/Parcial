maxLecturas = 8
lecturas = 0
sumTemp = 0.0
sumHum = 0.0
minTemp = float('inf')
maxTemp = float('-inf')
minHum = float('inf')
maxHum = float('-inf')
seqTemp = []
seqHum = []
resultado = ""

def fNum(val):
    """Formatea números quitando .0 si es entero y cambiando punto por coma"""
    numStr = str(val) if val % 1 != 0 else str(int(val))
    return numStr.replace('.', ',')

while resultado == "":
    # 1. Entrada y validación
    while True:
        try:
            temp = float(input("Ingrese temperatura [°C]: "))
            hum = float(input("Ingrese humedad [%]: "))
            if (-10 <= temp <= 60) and (0 <= hum <= 100):
                break
            else:
                print("Dato inválido. Ingrese nuevamente la lectura (no se cuenta).")
        except ValueError:
            print("Dato inválido. Debe ingresar números.")
    
    lecturas += 1
    
    # 2. Conteo, acumulación y registro de extremos
    sumTemp += temp
    sumHum += hum
    if temp < minTemp: minTemp = temp
    if temp > maxTemp: maxTemp = temp
    if hum < minHum: minHum = hum
    if hum > maxHum: maxHum = hum
    
    seqTemp.append(fNum(temp))
    seqHum.append(fNum(hum))
    
    # 3. Evaluaciones lógicas
    esCritico = (temp < 12 or temp > 32) or (hum < 40 or hum > 90)
    esOptimo = (18 <= temp <= 26) and (60 <= hum <= 80)
    
    if esCritico:
        estado = "Crítico"
        resultado = "Alerta crítica"
    elif esOptimo:
        estado = "Óptimo"
        if lecturas == 1:
            resultado = "Condiciones óptimas"
        else:
            resultado = "Cultivo estabilizado"
    else:
        estado = "Observación"
        acciones = []
        if temp < 18: acciones.append("Encender calefacción")
        if temp > 26: acciones.append("Ventilar")
        if hum < 60: acciones.append("Nebulizar")
        if hum > 80: acciones.append("deshumidificar")
        
        accion = " y ".join(acciones) if len(acciones) > 1 else acciones[0]
        # Ajuste minúsculas/mayúsculas para emparejar tabla original
        accion = accion.replace("y deshumidificar", "y deshumidificar")

    # Límite de revisión técnica
    if resultado == "" and lecturas == maxLecturas:
        resultado = "Revisión técnica"

# 4. Reporte y Salidas formadas
promTemp = sumTemp / lecturas
promHum = sumHum / lecturas

print("\n--- SALIDA ESPERADA ---")
print(f"Resultado: {resultado}. Lecturas tomadas: {lecturas}.")
print(f"Temperatura: mínima {fNum(minTemp)} – máxima {fNum(maxTemp)} – promedio {promTemp:.2f}".replace('.', ','))
print(f"Humedad: mínima {fNum(minHum)} – máxima {fNum(maxHum)} – promedio {promHum:.2f}".replace('.', ','))
print(f"Secuencia de temperaturas: {'; '.join(seqTemp)}. Secuencia de humedades: {'; '.join(seqHum)}.")