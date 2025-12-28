import os

# Estructura de carpetas y archivos para el BLOQUE A
structure = {
    "episodios/S0E02": [
        ("guion.md", """# S0E02 — Una nota NO es trazabilidad

**Personajes:**
- **[PEDRO]**: Indignado con el desorden.
- **[JAVIER]**: Metódico, "Excel lover".

---

## 🎬 Guion de Rodaje

**Escena:** Pedro sostiene un móvil mostrando una nota de texto caótica. Javier tiene un portátil abierto.

**(00:00) EL PROBLEMA**
**[PEDRO]** *(Muestra el móvil a cámara)*
Una nota en el móvil que dice "regué ayer" **no** es trazabilidad. Y cuando venga la auditoría y te pregunten "¿cuánto y a qué hora?", esa nota no te salva.

**(00:10) LA SOLUCIÓN TÉCNICA**
**[JAVIER]** *(Teclea rápido)*
Trazabilidad mínima requiere estructura, Pedro. Necesitas: ID único, fecha/hora exacta, quién lo hizo (Operador) y en qué fase.
*(Muestra pantalla: Nota vs Tabla)*
Esto es una nota libre... basura. Y esto es una tabla estructurada.

**(00:25) EL VALOR AGRO**
**[PEDRO]** *(Mira la pantalla, asintiendo)*
La clave no es tener más datos, es que sean consistentes. Si registras así, luego puedo comparar cosechas.

**(00:35) DEMO Y CIERRE**
**[JAVIER]**
Ahora el registro cae en una base de datos limpia. Es tu base para crecer a sensores.
Descarga la **plantilla de bitácora mínima** en el repo.

**[PEDRO]**
Tu misión hoy: crea un registro correcto. Deja las notas adhesivas.

**[JAVIER]**
Comenta "N0" y te paso el siguiente episodio.
"""),
        ("BITACORA_MINIMA.md", """# 📔 Plantilla: Bitácora Mínima de Cultivo

Para graduarte de "notas sueltas" a "datos reales", tus registros deben tener esta estructura.
Puedes copiar esta cabecera en Excel o Google Sheets.

| ID_Registro | Fecha_Hora (ISO) | Operador | Lote_ID | Fase | Tipo_Evento | Variable | Valor | Unidad | Notas |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 001 | 2026-01-20 09:00 | Pedro | A-01 | Veg | Riego | Cantidad | 5 | Litros | Riego manual |
| 002 | 2026-01-20 09:05 | Javier | A-01 | Veg | Clima | Temp | 24.5 | C | Sensor check |

## Glosario de Columnas
* **ID_Registro:** Número único ascendente.
* **Fecha_Hora:** Formato YYYY-MM-DD HH:MM (Crucial para ordenar).
* **Operador:** ¿Quién hizo la acción?
* **Lote_ID:** ¿Sobre qué planta/zona actuamos?
* **Fase:** En qué etapa está el cultivo (Veg, Flor, Secado).
"""),
        ("metadata_social.txt", """TITULO YOUTUBE: Una nota NO es trazabilidad: diferencia en 60s 📝❌
DESCRIPCION: Una nota en el móvil no te salva en una auditoría. Aprende a estructurar tu bitácora mínima. Descarga la plantilla en: [REPO_LINK]

IG CAPTION:
Una nota en el móvil no es trazabilidad. ❌📱
Si necesitas reconstruir qué pasó hace 3 meses, "regué ayer" no sirve.
Pedro y Javier te enseñan la estructura mínima de un registro profesional.
👇 Comenta "N0" si quieres la ruta corta.
#Trazabilidad #CultivoLegal #DataScience #ExcelTips
""")
    ],
    "episodios/S0_5E01": [
        ("guion.md", """# S0_5E01 — Antes de sensores: modelo de datos

**Personajes:**
- **[PEDRO]**: Quiere comparar cultivos pasados.
- **[JAVIER]**: Obsesionado con la nomenclatura.

---

## 🎬 Guion de Rodaje

**Escena:** Pizarra blanca con palabras escritas de forma distinta (Temp, Tº, Temperature).

**(00:00) EL CAOS**
**[PEDRO]** *(Señala la pizarra)*
Si en enero lo llamas "Temperatura" y en febrero "T_amb", tus datos no se pueden comparar. Y sin comparación, no hay control.

**(00:10) EL DICCIONARIO**
**[JAVIER]** *(Borra la pizarra y escribe una lista limpia)*
Hoy creamos el **Diccionario de Datos**. Definimos un idioma único: Lote, Fase, Evento, Variable y Unidad.
Ejemplo: La variable SIEMPRE se llamará `temp_air`.

**(00:25) POR QUÉ IMPORTA**
**[PEDRO]**
Esto no es burocracia. Es lo que te permite saber qué ocurrió, cuándo, y quién lo registró sin volverte loco leyendo jeroglíficos.

**(00:35) CIERRE**
**[JAVIER]**
Lo dejamos listo para que el formulario use listas cerradas. Descarga la plantilla de diccionario en el repo.

**[PEDRO]**
Consistencia desde el día 1.

**[JAVIER]**
Comenta "DICCIONARIO" y te enseño a validarlo.
"""),
        ("DICCIONARIO_DATOS.md", """# 📖 Diccionario de Datos (Modelo de Datos)

Define esto ANTES de crear tu Excel o configurar Home Assistant.

## 1. Fases del Cultivo (Lista Cerrada)
* `PLANTULAS`
* `VEGETATIVO`
* `FLORACION_TEMPRANA`
* `FLORACION_TARDIA`
* `SECADO`
* `CURADO`

## 2. Variables Standard (IDs)
| Nombre Humano | ID Sistema (Variable) | Unidad | Fuente Típica |
| :--- | :--- | :--- | :--- |
| Temperatura Aire | `temp_air` | ºC | Sensor / Manual |
| Humedad Relativa | `hum_rel` | % | Sensor / Manual |
| pH Riego | `ph_water` | pH | Manual (Pen) |
| Electrocond. | `ec_water` | mS/cm | Manual (Pen) |
"""),
        ("metadata_social.txt", """TITULO YOUTUBE: Tu Excel no sirve si no haces esto (Diccionario de Datos) 📖🔐
DESCRIPCION: Si no defines fases e IDs, tus datos no sirven. Crea tu diccionario de datos hoy. Plantilla: [REPO_LINK]

IG CAPTION:
¿"Temp", "Temperatura" o "T"? 🤔
Si cambias el nombre, rompes la gráfica.
Javier te explica cómo crear un DICCIONARIO DE DATOS para que Manual (N0) y Sensores (N1) hablen el mismo idioma.
👇 Descarga la plantilla en el link de la bio.
#DataGovernance #CultivoIndoor #SOPs #AgroData
""")
    ],
    "episodios/S0_5E02": [
        ("guion.md", """# S0_5E02 — Formularios que evitan errores

**Personajes:**
- **[JAVIER]**: Muestra cómo bloquear errores en Excel/Google Sheets.
- **[PEDRO]**: Feliz porque "sus chicos" ya no se equivocan al escribir.

---

## 🎬 Guion de Rodaje

**(00:00) EL ERROR #1**
**[JAVIER]**
El error número 1 en Nivel 0: escribir datos a mano.
**[PEDRO]**
Eso rompe la trazabilidad. Alguien escribe "25 grados" con letra, otro pone solo "25"... luego eso no se puede sumar.

**(00:15) LA SOLUCIÓN**
**[JAVIER]**
Solución: Formularios con **listas cerradas**.
*(Muestra pantalla móvil)*
Mira: Aquí elijo la fase de una lista. La variable también. Si intento escribir algo raro...
*(Suena sonido de error)*
...no me deja.

**(00:30) BENEFICIO**
**[PEDRO]**
Esto reduce el error humano a casi cero. Y prepara el terreno para cuando pongamos sensores.

**(00:40) CIERRE**
**[JAVIER]**
Paso práctico: activa una validación de datos hoy. Tienes la plantilla en el repo. Comenta "FORM" y te digo cómo estructurarla.
"""),
        ("PLANTILLA_FORM.md", """# 🛡️ Guía: Validaciones de Datos

Cómo evitar que entren datos "sucios" en tu sistema.

## Reglas de Validación (Google Sheets / Excel)

### 1. Listas Desplegables (Dropdowns)
* **Dónde usar:** Columna `Fase`, `Variable`, `Lote`.
* **Cómo:** Datos > Validación de datos > Criterio: "Lista de elementos".
* **Valor:** Copia los IDs de tu Diccionario de Datos.

### 2. Restricción Numérica
* **Dónde usar:** Columna `Valor`.
* **Cómo:** Datos > Validación de datos > "Es un número" > "Entre X e Y".
* **Ejemplo pH:** Entre 0 y 14.
"""),
        ("metadata_social.txt", """TITULO YOUTUBE: El truco para no equivocarte al registrar datos 🚫✍️
DESCRIPCION: El error #1 son los datos mal escritos ("typos"). Arréglalo con validaciones de datos y listas cerradas. Plantilla: [REPO_LINK]

IG CAPTION:
¿Tus hojas de cálculo son un caos? 📉
El secreto no es ser ordenado, es usar FORMULARIOS QUE NO TE DEJAN EQUIVOCARTE.
Javier te enseña a poner "candados" a tus celdas.
👇 Comenta "FORM" y te paso el tutorial.
#GoogleSheets #ExcelHacks #CultivoEficiente #AgroTech
""")
    ],
    "episodios/S0_5E04": [
        ("guion.md", """# S0_5E04 — Dashboard mínimo: ver tendencias

**Personajes:**
- **[PEDRO]**: Busca "visibilidad".
- **[JAVIER]**: Construye gráficas simples.

---

## 🎬 Guion de Rodaje

**(00:00) LA CEGUERA**
**[PEDRO]**
Si no ves tendencias, reaccionas tarde. Si ves que la humedad sube solo cuando ya hay hongos, has perdido.

**(00:10) DASHBOARD N0**
**[JAVIER]**
Hoy hacemos un dashboard mínimo con lo que ya tienes: tu hoja de cálculo.
*(Muestra pantalla)*
Gráfico 1: Evolución de temperatura en los últimos 7 días.
Gráfico 2: Conteo de incidencias por semana.
KPI: % de registros completados.

**(00:25) LA VISIBILIDAD**
**[PEDRO]**
No buscamos gráficos bonitos, buscamos ver el problema antes de que ocurra.
**[JAVIER]**
Paso práctico: crea un gráfico de línea desde tu columna `valor` y `fecha`.

**(00:35) CIERRE**
**[PEDRO]**
Así detectas huecos de datos y rutinas que fallan.
**[JAVIER]**
Tienes la plantilla en el repo. ¿Qué variable es la más crítica para ti? Déjalo en comentarios.
"""),
        ("GUIA_DASHBOARD.md", """# 📊 Guía: Tu Primer Dashboard

Objetivo: Visualizar los datos que capturaste en el Nivel 0.

## Gráfico 1: La Línea de Vida (Tendencia)
* **Eje X:** Columna `Fecha_Hora`
* **Eje Y:** Columna `Valor`
* **Filtro:** Filtrar por Variable = `temp_air`.
* **Uso:** Detectar picos o caídas bruscas.

## Gráfico 2: El Semáforo (Incidencias)
* **Tipo:** Gráfico de Barras.
* **Eje X:** Semana.
* **Eje Y:** Conteo de registros donde `Notas` no está vacío.
* **Uso:** Saber si una semana fue problemática.
"""),
        ("metadata_social.txt", """TITULO YOUTUBE: Cómo ver el futuro de tu cultivo con 2 gráficas 📈👀
DESCRIPCION: Si no ves tendencias, reaccionas tarde. Crea un dashboard mínimo en tu hoja de cálculo hoy mismo. Guía: [REPO_LINK]

IG CAPTION:
Ver el dato de hoy está bien. Ver la tendencia de la semana te salva la cosecha. 🚀
Javier te enseña a montar un Dashboard Mínimo con los datos que ya tienes.
👇 ¿Qué variable miras más? ¿Temp o Humedad?
#DataViz #Dashboard #CultivoIndoor #BusinessIntelligence
""")
    ]
}

def create_files():
    base_path = os.getcwd()
    print(f"📂 Generando Bloque A en: {base_path}")
    
    for folder, files in structure.items():
        # Crear carpeta si no existe
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        print(f"  + Carpeta: {folder}")
        
        # Crear archivos
        for filename, content in files:
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"    - Archivo creado: {filename}")

    print("\n✅ ¡Todo listo! Ahora ejecuta los comandos de git.")

if __name__ == "__main__":
    create_files()
