# SQLUser.PAC_InductionIndicators

**Schema:** SQLUser
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INDINDCTR_RowId | bigint | PK |  | NO | - |
| ChildQ29DR | - |  |  | SI | Child Reference: Psychiatric rehabilitation therap... |
| INDINDCTR_Active | varchar |  |  | SI | Active flag |
| INDINDCTR_Code | varchar |  |  | NO | Code |
| INDINDCTR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| INDINDCTR_CreatedDate | date |  |  | SI | Created Date |
| INDINDCTR_CreatedTime | time |  |  | SI | Created Time |
| INDINDCTR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| INDINDCTR_DateFrom | date |  |  | SI | Date From |
| INDINDCTR_DateTo | date |  |  | SI | Date To |
| INDINDCTR_Desc | varchar |  |  | NO | Description |
| INDINDCTR_NationalCode | varchar |  |  | SI | National code |
| INDINDCTR_Owner | varchar |  |  | SI | Owner |
| INDINDCTR_UpdatedDate | date |  |  | SI | Updated Date |
| INDINDCTR_UpdatedTime | time |  |  | SI | Updated Time |
| INDINDCTR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q27Q1 | - |  |  | SI | Goal |
| Q27Q2 | - |  |  | SI | Timing |
| Q27Q3 | - |  |  | SI | Notes |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*