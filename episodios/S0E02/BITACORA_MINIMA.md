# 📔 Plantilla: Bitácora Mínima de Cultivo

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
