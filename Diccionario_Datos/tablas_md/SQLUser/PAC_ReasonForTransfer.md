# SQLUser.PAC_ReasonForTransfer

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RETRA_RowId | bigint | PK |  | NO | - |
| Q40Q1 | - |  |  | SI | Suture location |
| Q40Q2 | - |  |  | SI | Suture material |
| Q40Q3 | - |  |  | SI | Suturing method |
| Q40Q4 | - |  |  | SI | Notes |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| RETRA_Code | varchar |  |  | NO | Code |
| RETRA_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| RETRA_CreatedDate | date |  |  | SI | Created Date |
| RETRA_CreatedTime | time |  |  | SI | Created Time |
| RETRA_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RETRA_DateFrom | date |  |  | SI | Date From |
| RETRA_DateTo | date |  |  | SI | Date To |
| RETRA_Desc | varchar |  |  | NO | Description |
| RETRA_NationalCode | varchar |  |  | SI | National Code |
| RETRA_Owner | varchar |  |  | SI | Owner |
| RETRA_UpdatedDate | date |  |  | SI | Updated Date |
| RETRA_UpdatedTime | time |  |  | SI | Updated Time |
| RETRA_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*