# SQLUser.PAC_SNAPCareTypeADLType

**Schema:** SQLUser
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ADL_ParRef | bigint | PK |  | NO | PAC_SNAPCareType Parent Reference |
| ADL_ADLCareType_DR | bigint |  | FK | SI | Des Ref ADLCareType |
| ADL_Childsub | double |  |  | NO | Childsub |
| ADL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ADL_CreatedDate | date |  |  | SI | Created Date |
| ADL_CreatedTime | time |  |  | SI | Created Time |
| ADL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ADL_RowId | varchar |  |  | NO | - |
| ADL_UpdatedDate | date |  |  | SI | Updated Date |
| ADL_UpdatedTime | time |  |  | SI | Updated Time |
| ADL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ5DR | - |  |  | SI | Child Reference: Clinical stability and secondary ... |
| Q19Q1 | - |  |  | SI | Micro goal |
| Q19Q2 | - |  |  | SI | Timing |
| Q19Q3 | - |  |  | SI | Outcome |
| Q19Q4 | - |  |  | SI | Notes |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*