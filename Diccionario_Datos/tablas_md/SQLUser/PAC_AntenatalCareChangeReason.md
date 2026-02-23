# SQLUser.PAC_AntenatalCareChangeReason

**Schema:** SQLUser
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ACCR_RowId | bigint | PK |  | NO | - |
| ACCR_Code | varchar |  |  | NO | Code |
| ACCR_CodeTableTags | varchar |  |  | SI | Code Table Tags |
| ACCR_CreatedDate | date |  |  | SI | Created Date |
| ACCR_CreatedTime | time |  |  | SI | Created Time |
| ACCR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ACCR_DateFrom | date |  |  | SI | Date From |
| ACCR_DateTo | date |  |  | SI | Date To |
| ACCR_Desc | varchar |  |  | NO | Description |
| ACCR_Owner | varchar |  |  | SI | Code Table Owner |
| ACCR_UpdatedDate | date |  |  | SI | Updated Date |
| ACCR_UpdatedTime | time |  |  | SI | Updated Time |
| ACCR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ111DR | - |  |  | SI | Child Reference: Needed supplies |
| Q109Q1 | - |  |  | SI | Items |
| Q109Q2 | - |  |  | SI | Action |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*