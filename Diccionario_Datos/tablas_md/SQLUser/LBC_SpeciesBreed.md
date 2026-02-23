# SQLUser.LBC_SpeciesBreed

**Schema:** SQLUser
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCSPCSB_ParRef | bigint | PK |  | NO | Parent Container DR |
| LBCSPCSB_Code | varchar |  |  | NO | Code |
| LBCSPCSB_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCSPCSB_CreatedDate | date |  |  | SI | Created Date |
| LBCSPCSB_CreatedTime | time |  |  | SI | Created Time |
| LBCSPCSB_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCSPCSB_DateFrom | date |  |  | SI | From Date |
| LBCSPCSB_DateTo | date |  |  | SI | To Date |
| LBCSPCSB_Desc | varchar |  |  | NO | Description |
| LBCSPCSB_RowID | varchar |  |  | NO | - |
| LBCSPCSB_UpdatedDate | date |  |  | SI | Updated Date |
| LBCSPCSB_UpdatedTime | time |  |  | SI | Updated Time |
| LBCSPCSB_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*