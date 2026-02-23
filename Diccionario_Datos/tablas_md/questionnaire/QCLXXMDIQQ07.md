# questionnaire.QCLXXMDIQQ07

> Mantención Dispositivos Invasivos : Dispositivos Vías Aéreas

**Schema:** questionnaire
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Mantención Dispositivos Invasivos : Dispositivos Vías Aéreas

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q07Q1 | varchar |  |  | SI | Tipo Dispositivo |
| Q07Q2 | varchar |  |  | SI | Subtipo |
| Q07Q3 | varchar |  |  | SI | Actividad |
| Q07Q4 | varchar |  |  | SI | Tamaño |
| Q07Q5 | varchar |  |  | SI | Ubicación |
| Q07Q6 | varchar |  |  | SI | N° Días Dispositivo Vía Aérea |
| Q07Q7 | varchar |  |  | SI | ¿Es necesario el DI? |
| Q07Q8 | varchar |  |  | SI | Comentarios |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*