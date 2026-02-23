# SQLUser.PAC_IncapacityType

**Schema:** SQLUser
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INCT_RowId | bigint | PK |  | NO | - |
| ChildQ25DR | - |  |  | SI | Child Reference: Psychotherapist psychologist goal... |
| INCT_Code | varchar |  |  | NO | Code |
| INCT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| INCT_CreatedDate | date |  |  | SI | Created Date |
| INCT_CreatedTime | time |  |  | SI | Created Time |
| INCT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| INCT_DateFrom | date |  |  | SI | Date From |
| INCT_DateTo | date |  |  | SI | Date To |
| INCT_Desc | varchar |  |  | NO | Description |
| INCT_Owner | varchar |  |  | SI | Owner |
| INCT_UpdatedDate | date |  |  | SI | Updated Date |
| INCT_UpdatedTime | time |  |  | SI | Updated Time |
| INCT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q23Q1 | - |  |  | SI | Goal |
| Q23Q2 | - |  |  | SI | Timing |
| Q23Q3 | - |  |  | SI | Notes |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*