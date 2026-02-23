# SQLUser.OE_OrdRefDoctor

**Schema:** SQLUser
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Órdenes Médicas**. Solicitudes de exámenes, procedimientos, etc.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REFD_ParRef | varchar | PK |  | NO | OE_OrdItem Parent Reference |
| Q62Q1 | - |  |  | SI | Pretest Symptoms Standing |
| Q62Q2 | - |  |  | SI | Pretest Symptoms Lying |
| Q62Q3 | - |  |  | SI | If required Pretest Symptoms |
| Q62Q4 | - |  |  | SI | Symptoms During Testing |
| Q62Q5 | - |  |  | SI | Symptoms After Testing |
| Q62Q6 | - |  |  | SI | Mechanical Response |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| REFD_Childsub | double |  |  | NO | Childsub |
| REFD_RefDoc_DR | bigint |  | FK | SI | Des Ref RefDoc |
| REFD_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*