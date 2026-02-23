# SQLUser.PAC_ContInterpreterType

**Schema:** SQLUser
**Columnas:** 24
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INTERP_RowId | bigint | PK |  | NO | - |
| INTERP_Code | varchar |  |  | NO | Code |
| INTERP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| INTERP_CreatedDate | date |  |  | SI | Created Date |
| INTERP_CreatedTime | time |  |  | SI | Created Time |
| INTERP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| INTERP_DateFrom | date |  |  | SI | Date From |
| INTERP_DateTo | date |  |  | SI | Date To |
| INTERP_Desc | varchar |  |  | NO | Description |
| INTERP_Owner | varchar |  |  | SI | Owner |
| INTERP_UpdatedDate | date |  |  | SI | Updated Date |
| INTERP_UpdatedTime | time |  |  | SI | Updated Time |
| INTERP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q07Q1 | - |  |  | SI | Date |
| Q07Q10 | - |  |  | SI | Performed  by: |
| Q07Q2 | - |  |  | SI | Time |
| Q07Q3 | - |  |  | SI | Duration of taught (Minutes) |
| Q07Q4 | - |  |  | SI | Participant(s) |
| Q07Q5 | - |  |  | SI | Education method used |
| Q07Q6 | - |  |  | SI | Learning barrier |
| Q07Q7 | - |  |  | SI | Education needs and information taught  (* is mand... |
| Q07Q8 | - |  |  | SI | Learning Response |
| Q07Q9 | - |  |  | SI | Comment |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*