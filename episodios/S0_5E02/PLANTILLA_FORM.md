# 🛡️ Guía: Validaciones de Datos

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
