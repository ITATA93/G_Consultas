# questionnaire.QCLXXATERUIQQ81

> REGISTRO ATENCIÓN RUI : Programa de Salud MEUI

**Schema:** questionnaire
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* REGISTRO ATENCIÓN RUI : Programa de Salud MEUI

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q81Q1 | varchar |  |  | SI | Programa de Salud  |
| Q81Q2 | varchar |  |  | SI | Tipo de Atención |
| Q81Q3 | varchar |  |  | SI | ID MRC_EncEntryType |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*