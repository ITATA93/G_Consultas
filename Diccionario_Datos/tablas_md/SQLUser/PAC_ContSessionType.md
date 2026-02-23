# SQLUser.PAC_ContSessionType

**Schema:** SQLUser
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CONTSESSTYPE_RowId | bigint | PK |  | NO | - |
| CONTSESSTYPE_Code | varchar |  |  | NO | Code |
| CONTSESSTYPE_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CONTSESSTYPE_CreatedDate | date |  |  | SI | Created Date |
| CONTSESSTYPE_CreatedTime | time |  |  | SI | Created Time |
| CONTSESSTYPE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CONTSESSTYPE_DateFrom | date |  |  | SI | Date From |
| CONTSESSTYPE_DateTo | date |  |  | SI | Date To |
| CONTSESSTYPE_Desc | varchar |  |  | NO | Description |
| CONTSESSTYPE_Owner | varchar |  |  | SI | Owner |
| CONTSESSTYPE_UpdatedDate | date |  |  | SI | Updated Date |
| CONTSESSTYPE_UpdatedTime | time |  |  | SI | Updated Time |
| CONTSESSTYPE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q22Q1 | - |  |  | SI | Drainage present |
| Q22Q2 | - |  |  | SI | Drainage description |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*