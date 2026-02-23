# SQLUser.ARC_ServCat

**Schema:** SQLUser
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ARCSC_RowId | bigint | PK |  | NO | - |
| ARCSC_Abbrev | varchar |  |  | SI | Abbreviation |
| ARCSC_AccruedAccount_DR | bigint |  | FK | SI | Des Ref AccruedAccount |
| ARCSC_ActiveFlag | varchar |  |  | NO | Active Flag |
| ARCSC_Code | varchar |  |  | NO | Service Category |
| ARCSC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ARCSC_CreatedDate | date |  |  | SI | Created Date |
| ARCSC_CreatedTime | time |  |  | SI | Created Time |
| ARCSC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ARCSC_Desc | varchar |  |  | NO | Description |
| ARCSC_IPAcc_DR | bigint |  | FK | SI | Des Ref to GLCAC |
| ARCSC_OPAcc_DR | bigint |  | FK | SI | Des Ref to GLCAC |
| ARCSC_Owner | varchar |  |  | SI | Owner |
| ARCSC_UpdatedDate | date |  |  | SI | Updated Date |
| ARCSC_UpdatedTime | time |  |  | SI | Updated Time |
| ARCSC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| QDataField | - |  |  | SI | Campo |
| QDataValueNew | - |  |  | SI | Valor Nuevo |
| QDataValueOld | - |  |  | SI | Valor Anterior |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*