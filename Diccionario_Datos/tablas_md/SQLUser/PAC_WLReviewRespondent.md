# SQLUser.PAC_WLReviewRespondent

**Schema:** SQLUser
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| WLRES_RowId | bigint | PK |  | NO | - |
| Q26Q1 | - |  |  | SI | Date of positive blood culture |
| Q26Q2 | - |  |  | SI | Date of clearance blood culture |
| Q26Q3 | - |  |  | SI | Surveillance blood cultures at 72-96 hours results |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| WLRES_Code | varchar |  |  | NO | Code |
| WLRES_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| WLRES_CreatedDate | date |  |  | SI | Created Date |
| WLRES_CreatedTime | time |  |  | SI | Created Time |
| WLRES_CreatedUser_DR | bigint |  | FK | SI | Created User |
| WLRES_DateFrom | date |  |  | SI | Date From |
| WLRES_DateTo | date |  |  | SI | Date To |
| WLRES_Desc | varchar |  |  | NO | Description |
| WLRES_Owner | varchar |  |  | SI | Owner |
| WLRES_UpdatedDate | date |  |  | SI | Updated Date |
| WLRES_UpdatedTime | time |  |  | SI | Updated Time |
| WLRES_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*