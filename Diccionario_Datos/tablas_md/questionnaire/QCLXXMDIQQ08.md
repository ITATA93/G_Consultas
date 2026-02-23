# questionnaire.QCLXXMDIQQ08

> Mantención Dispositivos Invasivos : Dispositivos Gastrointestinales

**Schema:** questionnaire
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Mantención Dispositivos Invasivos : Dispositivos Gastrointestinales

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q08Q1 | varchar |  |  | SI | Tipo Dispositivo |
| Q08Q10 | varchar |  |  | SI | ¿Es Necesario el DI? |
| Q08Q2 | varchar |  |  | SI | Actividad |
| Q08Q3 | varchar |  |  | SI | Tamaño |
| Q08Q4 | varchar |  |  | SI | Acceso |
| Q08Q5 | varchar |  |  | SI | Ubicación |
| Q08Q6 | varchar |  |  | SI | Confirmación Ubicación |
| Q08Q7 | varchar |  |  | SI | Estado |
| Q08Q8 | varchar |  |  | SI | Descripción Contenido |
| Q08Q9 | varchar |  |  | SI | N° Días Dispositivo GI |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*