# SQLUser.ORC_MinorAgreemAuthoriser

**Schema:** SQLUser
**Columnas:** 23
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MIAGAU_RowId | bigint | PK |  | NO | - |
| MIAGAU_Code | varchar |  |  | NO | Code |
| MIAGAU_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| MIAGAU_CreatedDate | date |  |  | SI | Created Date |
| MIAGAU_CreatedTime | time |  |  | SI | Created Time |
| MIAGAU_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MIAGAU_DateFrom | date |  |  | SI | Date From |
| MIAGAU_DateTo | date |  |  | SI | Date To |
| MIAGAU_Desc | varchar |  |  | NO | Description |
| MIAGAU_Owner | varchar |  |  | SI | Owner |
| MIAGAU_UpdatedDate | date |  |  | SI | Updated Date |
| MIAGAU_UpdatedTime | time |  |  | SI | Updated Time |
| MIAGAU_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q82Q1 | - |  |  | SI | Date |
| Q82Q2 | - |  |  | SI | Time |
| Q82Q3 | - |  |  | SI | Screening timeframe |
| Q82Q4 | - |  |  | SI | Pre-ductal saturation - hand (%) |
| Q82Q5 | - |  |  | SI | Hand laterality |
| Q82Q6 | - |  |  | SI | Post-ductal saturation - foot (%) |
| Q82Q7 | - |  |  | SI | Foot laterality |
| Q82Q8 | - |  |  | SI | Result |
| Q82Q9 | - |  |  | SI | Other result |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*