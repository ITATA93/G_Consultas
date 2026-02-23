# SQLUser.LBC_Container

**Schema:** SQLUser
**Columnas:** 23
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCCON_RowID | bigint | PK |  | NO | - |
| ChildQ19DR | - |  |  | SI | Child Reference: Straw Details |
| LBCCON_Code | varchar |  |  | NO | Code |
| LBCCON_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCCON_CodeTranslated | varchar |  |  | SI | - |
| LBCCON_Comments | varchar |  |  | SI | Comments |
| LBCCON_CreatedDate | date |  |  | SI | Created Date |
| LBCCON_CreatedTime | time |  |  | SI | Created Time |
| LBCCON_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCCON_DateFrom | date |  |  | SI | Effective date for the record |
| LBCCON_DateTo | date |  |  | SI | Last day the record is active  |
| LBCCON_Desc | varchar |  |  | NO | Description |
| LBCCON_DescTranslated | varchar |  |  | SI | - |
| LBCCON_Manufacturer_DR | bigint |  | FK | SI | Manufacturer |
| LBCCON_MaxVolume | double |  |  | SI | Max Volume |
| LBCCON_Owner | varchar |  |  | SI | Owner |
| LBCCON_Thumbnail | bigint |  |  | SI | Thumbnail |
| LBCCON_UpdatedDate | date |  |  | SI | Updated Date |
| LBCCON_UpdatedTime | time |  |  | SI | Updated Time |
| LBCCON_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q03Q1 | - |  |  | SI | Number of embryos |
| Q03Q2 | - |  |  | SI | Stage |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*