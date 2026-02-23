# SQLUser.ARC_HICResponseMessages

**Schema:** SQLUser
**Columnas:** 23
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HICRM_RowId | bigint | PK |  | NO | - |
| HICRM_Code | varchar |  |  | NO | Code |
| HICRM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| HICRM_CreatedDate | date |  |  | SI | Created Date |
| HICRM_CreatedTime | time |  |  | SI | Created Time |
| HICRM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| HICRM_DateFrom | date |  |  | SI | Date From |
| HICRM_DateTo | date |  |  | SI | Date To |
| HICRM_Desc | varchar |  |  | NO | Description |
| HICRM_InternalType | varchar |  |  | SI | InternalType |
| HICRM_MessageResponse | varchar |  |  | SI | Message Response |
| HICRM_Owner | varchar |  |  | SI | Owner |
| HICRM_Text | varchar |  |  | SI | Text |
| HICRM_UpdatedDate | date |  |  | SI | Updated Date |
| HICRM_UpdatedTime | time |  |  | SI | Updated Time |
| HICRM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| HICRM_ValidResponseA | varchar |  |  | SI | Valid Response A |
| HICRM_ValidResponseB | varchar |  |  | SI | Valid Response B |
| Q21Q1 | - |  |  | SI | Ojo |
| Q21Q2 | - |  |  | SI | Cuadrante |
| Q21Q3 | - |  |  | SI | Comentarios |
| Q21Q4 | - |  |  | SI | Hemorragia Subconjuntival |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*