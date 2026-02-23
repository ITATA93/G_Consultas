# SQLUser.LBC_ContainerManufacturer

**Schema:** SQLUser
**Columnas:** 23
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCCONM_RowID | bigint | PK |  | NO | - |
| LBCCONM_128_Code | varchar |  |  | SI | 128 Code |
| LBCCONM_Code | varchar |  |  | NO | Code |
| LBCCONM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCCONM_CreatedDate | date |  |  | SI | Created Date |
| LBCCONM_CreatedTime | time |  |  | SI | Created Time |
| LBCCONM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCCONM_DateFrom | date |  |  | SI | Effective date for the record |
| LBCCONM_DateTo | date |  |  | SI | Last day the record is active  |
| LBCCONM_Desc | varchar |  |  | NO | Description |
| LBCCONM_Owner | varchar |  |  | SI | Owner |
| LBCCONM_UpdatedDate | date |  |  | SI | Updated Date |
| LBCCONM_UpdatedTime | time |  |  | SI | Updated Time |
| LBCCONM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q20Q1 | - |  |  | SI | Embryos frozen number |
| Q20Q2 | - |  |  | SI | Cells / Grade |
| Q20Q3 | - |  |  | SI | Post-thaw day 2 |
| Q20Q4 | - |  |  | SI | Post-thaw day 3 |
| Q20Q5 | - |  |  | SI | Post-thaw day 4 |
| Q20Q6 | - |  |  | SI | Post-thaw day 5 |
| Q20Q7 | - |  |  | SI | Transferred |
| Q20Q8 | - |  |  | SI | Refrozen |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*