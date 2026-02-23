# SQLUser.PAC_CitizenshipStatusSource

**Schema:** SQLUser
**Columnas:** 24
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CITSRC_RowId | bigint | PK |  | NO | - |
| CITSRC_Code | varchar |  |  | NO | Code |
| CITSRC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CITSRC_CreatedDate | date |  |  | SI | Created Date |
| CITSRC_CreatedTime | time |  |  | SI | Created Time |
| CITSRC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CITSRC_DateFrom | date |  |  | SI | DateFrom |
| CITSRC_DateTo | date |  |  | SI | DateTo |
| CITSRC_Desc | varchar |  |  | NO | Description |
| CITSRC_Owner | varchar |  |  | SI | Owner |
| CITSRC_UpdatedDate | date |  |  | SI | Updated Date |
| CITSRC_UpdatedTime | time |  |  | SI | Updated Time |
| CITSRC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ22DR | - |  |  | SI | Child Reference: Drainage Assessment |
| Q21Q1 | - |  |  | SI | Need daily assessment |
| Q21Q2 | - |  |  | SI | Care |
| Q21Q3 | - |  |  | SI | Site details |
| Q21Q4 | - |  |  | SI | Dressing type / appearance |
| Q21Q5 | - |  |  | SI | Line patency |
| Q21Q6 | - |  |  | SI | Assessment date / time |
| Q21Q7 | - |  |  | SI | Assessment time |
| Q21Q8 | - |  |  | SI | Assessing care provider |
| Q21Q9 | - |  |  | SI | Equipment used |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*