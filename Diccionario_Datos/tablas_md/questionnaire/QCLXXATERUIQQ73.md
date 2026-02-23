# questionnaire.QCLXXATERUIQQ73

> REGISTRO ATENCIÓN RUI : Programa de Salud

**Schema:** questionnaire
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* REGISTRO ATENCIÓN RUI : Programa de Salud

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q73Q1 | varchar |  |  | SI | Programa / Actividad |
| Q73Q2 | varchar |  |  | SI | Tipo Consulta |
| Q73Q3 | varchar |  |  | SI | ID Consultation |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*