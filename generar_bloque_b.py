import os

# Estructura de carpetas para el BLOQUE B (Final)
structure = {
    "episodios/S0E09": [
        ("guion.md", """# S0E09 — Backup y Restore en 60s

**Personajes:**
- **[JAVIER]**: Paranoico de la seguridad (pero con calma).
- **[PEDRO]**: Preocupado por perder años de trabajo.

---

## 🎬 Guion de Rodaje

**Escena:** Pedro mirando el ordenador con cara de terror. Javier tranquilo tomando café.

**(00:00) EL MIEDO**
**[JAVIER]**
Pregunta rápida, Pedro: si mañana se quema este ordenador... ¿pierdes 3 años de genética y registros?
**[PEDRO]** *(Traga saliva)*
Si pierdo la hoja maestra, pierdo la trazabilidad. No sabría qué madre es cual.

**(00:10) EL SIMULACRO**
**[JAVIER]**
Sin backup probado, tus datos no existen. Hoy hacemos un simulacro de incendio digital.
*(Muestra pantalla)*
Paso 1: Exporto la base de datos (o copio el Excel).
Paso 2: Lo borro todo.
**[PEDRO]** *(Grita)* ¡No!

**(00:25) LA RESURRECCIÓN**
**[JAVIER]**
Tranquilo. Paso 3: Restore desde la nube/USB.
*(Click, barra de carga, todo vuelve)*
Verificado.

**(00:35) CIERRE**
**[PEDRO]** *(Resopla aliviado)*
Lo importante no es guardar, es saber restaurar. Backup que no se prueba, es fe, no tecnología.

**[JAVIER]**
Descarga la **Checklist de Backup** en el repo. Comenta "BACKUP" y te digo dónde guardar las copias.
"""),
        ("CHECKLIST_BACKUP.md", """# 💾 Checklist: Estrategia de Copias de Seguridad (3-2-1)

No esperes al desastre. Sigue la regla 3-2-1.

1.  [ ] **3 Copias:** Ten tus datos en 3 lugares (Original + Copia A + Copia B).
2.  [ ] **2 Soportes:** Usa distintos medios (Ej: Tu PC y un Disco Duro USB).
3.  [ ] **1 Nube:** Una copia debe estar fuera de tu edificio (Google Drive, GitHub, AWS).

## Rutina de Simulacro (Mensual)
* [ ] Borrar un archivo de prueba.
* [ ] Intentar recuperarlo desde la copia.
* [ ] ¿Ha funcionado? Si la respuesta es NO, tu backup no sirve.
"""),
        ("metadata_social.txt", """TITULO YOUTUBE: El día que borré mi cultivo (Simulacro Backup) 😱💾
DESCRIPCION: Si mañana pierdes tu ordenador, ¿pierdes tu empresa? Hoy hacemos un simulacro de desastre y recuperación. Checklist: [REPO_LINK]

IG CAPTION:
El sudor frío cuando no encuentras un archivo... 😰
Pedro casi le da un infarto, pero Javier le enseña la regla 3-2-1 de los backups.
⚠️ Un backup que no has probado a restaurar, NO EXISTE.
👇 Comenta "BACKUP" y asegura tu trabajo.
#Ciberseguridad #CultivoSeguro #DataBackup #TechTips
""")
    ],
    "episodios/S0_5E08": [
        ("guion.md", """# S0_5E08 — Piloto 0→1: Elige 1 variable

**Personajes:**
- **[PEDRO]**: Frena el entusiasmo desmedido.
- **[JAVIER]**: Quiere poner sensores hasta en el baño.

---

## 🎬 Guion de Rodaje

**Escena:** Javier llega con una caja llena de cables y sensores. Pedro le para la mano.

**(00:00) EL EXCESO**
**[PEDRO]**
¡Quieto ahí! Si empiezas poniendo 10 sensores a la vez, te vas a frustrar. No vas a saber qué falla.

**(00:10) EL PLAN PILOTO**
**[JAVIER]**
Vale, vale. Hacemos el **Piloto 0→1**.
Elegimos SOLA UNA variable. Por ejemplo: Temperatura.
Un solo punto de medida. Y lo comparamos con tu termómetro manual durante una semana.

**(00:25) LA VALIDACIÓN**
**[PEDRO]**
El objetivo no es automatizar ya. Es confiar en el dato. Si el sensor dice 25ºC y mi termómetro 30ºC, tenemos un problema.

**(00:35) CIERRE**
**[JAVIER]**
Paso práctico: define tu "variable piloto" en la plantilla del repo.
**[PEDRO]**
Así el salto es seguro.

**[JAVIER]**
Comenta tu variable favorita (Temp, Humedad, EC) y te digo qué sensor barato comprar.
"""),
        ("PLAN_PILOTO.md", """# 🛫 Plan Piloto 0→1 (Tu primer sensor)

No automatices todo el cultivo de golpe. Empieza aquí.

## Definición del Experimento
* **Variable elegida:** (Ej: Temperatura Aire)
* **Sensor candidato:** (Ej: Xiaomi Mijia / Sonoff / ESP32)
* **Duración de prueba:** 7 días.

## Tabla de Validación (Sensor vs Manual)
| Día | Hora | Valor Manual (Nivel 0) | Valor Sensor (Nivel 1) | Diferencia | ¿Aceptable? (<10%) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Lunes | 09:00 | 24.0 ºC | 24.2 ºC | +0.2 | ✅ SÍ |
| Martes| 09:00 | 23.5 ºC | 28.0 ºC | +4.5 | ❌ NO (Revisar ubicación) |

> **Nota:** Nunca confíes en un sensor nuevo hasta que pase esta prueba.
"""),
        ("metadata_social.txt", """TITULO YOUTUBE: No compres 10 sensores, compra 1 (Plan Piloto) 🛑📟
DESCRIPCION: El error de novato es llenarlo todo de cables. Empieza con UNA variable y valídala. Plantilla de Plan Piloto: [REPO_LINK]

IG CAPTION:
¿Quieres montar un sistema IoT? 🤖
Pedro le prohíbe a Javier poner 10 sensores de golpe. 🛑
La estrategia correcta es el "Piloto 0→1": Una variable, un sensor, una semana de pruebas.
👇 ¿Por cuál vas a empezar? ¿Temperatura o Humedad? Te leo.
#IoT #SmartGrow #Sensores #IngenieriaAgricola
""")
    ],
    "episodios/S0E10": [
        ("guion.md", """# S0E10 — Subir de Nivel: Mejoras y Retos

**Personajes:**
- **[PEDRO]**: Orgulloso de la evolución.
- **[JAVIER]**: Mirando al futuro (IA).

---

## 🎬 Guion de Rodaje

**Escena:** Plano partido. Izquierda: Pedro con su libreta ordenada. Derecha: Javier con un dashboard en tablet.

**(00:00) EL VIAJE**
**[PEDRO]**
Empezamos con papeles sucios y miedo a la tecnología. Hoy tenemos datos limpios.
**[JAVIER]**
Hemos visto que subir de nivel te da superpoderes... pero también trae problemas nuevos.

**(00:10) RESUMEN DE NIVELES**
**[JAVIER]**
Nivel 0 fue disciplina. Nivel 1 será calibración de hardware. Nivel 2 será gestionar servidores. Y el Nivel 3... enseñar a la IA a pensar como Pedro.

**(00:25) LA ADVERTENCIA**
**[PEDRO]**
Recuerda: la tecnología amplifica lo que ya eres. Si eres ordenado, serás eficiente. Si eres un caos, serás un caos automatizado.

**(00:35) CIERRE DE TEMPORADA**
**[JAVIER]**
Tienes la tabla de **Mejoras y Retos** en el repo.
**[AMBOS]**
Gracias por seguir la ruta 0→3.
**[JAVIER]**
Comenta "N1" si quieres que la próxima temporada empecemos a conectar cables de verdad.
"""),
        ("MEJORAS_RETOS.md", """# 📈 Tabla: Mejoras y Retos por Nivel

Lo que ganas (y lo que sufres) al subir cada escalón.

| Nivel | Lo que ganas (Ventaja) | El nuevo problema (Reto) |
| :--- | :--- | :--- |
| **N0 (Manual)** | Bajo coste, flexibilidad total. | Error humano, datos lentos, no escalable. |
| **N1 (Sensores)** | Datos 24/7, alertas al móvil. | Calibración, pilas agotadas, desconexiones WiFi. |
| **N2 (Plataforma)** | Soberanía, dashboards unificados. | Mantenimiento del servidor (updates, backups). |
| **N3 (IA)** | Predicciones, "segundo cerebro". | Coste computacional, "alucinaciones" de la IA. |

## ¿Estás listo para el Nivel 1?
Si has completado todos los entregables de esta temporada, estás listo para comprar tu primer sensor. ¡Nos vemos en la siguiente fase!
"""),
        ("metadata_social.txt", """TITULO YOUTUBE: El fin del principio (Resumen Nivel 0 a 3) 🚀🏁
DESCRIPCION: Hemos terminado la fase de fundamentos. ¿Qué ganas y qué pierdes al automatizar? Tabla de Retos: [REPO_LINK]

IG CAPTION:
¡Final de temporada! 🎬
Pedro y Javier resumen el viaje.
La tecnología no es magia ✨, es una herramienta con ventajas y retos.
¿Estás listo para dejar el papel y pasar al hardware?
👇 Comenta "N1" si quieres que la próxima serie sea 100% montaje de sensores.
#FinDeTemporada #Agritech #Roadmap #CultivoIndoor
""")
    ]
}

def create_files():
    base_path = os.getcwd()
    print(f"📂 Generando Bloque B (Final) en: {base_path}")
    
    for folder, files in structure.items():
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        print(f"  + Carpeta: {folder}")
        
        for filename, content in files:
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"    - Archivo creado: {filename}")

    print("\n✅ Bloque B generado. Ejecuta 'git add .' y 'git push' de nuevo.")

if __name__ == "__main__":
    create_files()
