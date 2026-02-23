# SQLUser.NRC_Goal

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Enfermería**. Parámetros de enfermería.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| NRCG_RowID | bigint | PK |  | NO | - |
| ChildQ122DR | - |  |  | SI | Child Reference: Shift Assessment |
| NRCG_ARCIM_DR | varchar |  | FK | SI | Order Item |
| NRCG_AdditionalDescription | varchar |  |  | SI | Order Item Additional Description. Stores the long... |
| NRCG_Code | varchar |  |  | NO | Code  |
| NRCG_CodeTableTags | varchar |  |  | SI | List of code table tags |
| NRCG_DateFrom | date |  |  | NO | Effective date for the record |
| NRCG_DateTo | date |  |  | SI | Last day the record is active |
| NRCG_DefaultAutoOrderValid | bit |  |  | SI | Order Item Valid Automatic Order |
| NRCG_Desc | varchar |  |  | NO | Description |
| NRCG_Owner | varchar |  |  | SI | Owner |
| NRCG_PrefParams_DR | bigint |  | FK | SI | Order Item Default Parameters |
| Q85Q3 | - |  |  | SI | Comments |
| Q85Q4 | - |  |  | SI | Staff |
| Q85Q5 | - |  |  | SI | Date |
| Q85Q6 | - |  |  | SI | Time |
| Q86Q1 | - |  |  | SI | Checklist |
| Q86Q2 | - |  |  | SI | Helium level in cylinder |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*