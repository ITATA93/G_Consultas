# SQLUser.INC_CommercialItem

**Schema:** SQLUser
**Columnas:** 23
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| COMM_RowId | bigint | PK |  | NO | - |
| COMM_Code | varchar |  |  | NO | Code |
| COMM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| COMM_CreatedDate | date |  |  | SI | Created Date |
| COMM_CreatedTime | time |  |  | SI | Created Time |
| COMM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| COMM_Desc | varchar |  |  | NO | Description |
| COMM_Owner | varchar |  |  | SI | Owner |
| COMM_UpdatedDate | date |  |  | SI | Updated Date |
| COMM_UpdatedTime | time |  |  | SI | Updated Time |
| COMM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ52DR | - |  |  | SI | Child Reference: Performing care bundle |
| Q51Q1 | - |  |  | SI | Daily review of line necessity |
| Q51Q10 | - |  |  | SI | Increased white blood count |
| Q51Q2 | - |  |  | SI | Dressing intact and labelled with date and time st... |
| Q51Q3 | - |  |  | SI | Scrub the access port hub with chlorhexidine prior... |
| Q51Q4 | - |  |  | SI | Comply with hand hygiene |
| Q51Q5 | - |  |  | SI | Regular monitoring of insertion site |
| Q51Q6 | - |  |  | SI | Change dressing at least every 7 days or when wet ... |
| Q51Q7 | - |  |  | SI | Fever |
| Q51Q8 | - |  |  | SI | Chills |
| Q51Q9 | - |  |  | SI | Hypotension |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*