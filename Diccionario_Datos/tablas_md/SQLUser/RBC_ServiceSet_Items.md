# SQLUser.RBC_ServiceSet_Items

**Schema:** SQLUser
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ITM_ParRef | bigint | PK |  | NO | RBC_ServiceSet Parent Reference |
| ITM_ARCIM_DR | varchar |  | FK | SI | Des Ref ARCIM |
| ITM_ARCOS_DR | varchar |  | FK | SI | Des Ref ARCOS |
| ITM_Childsub | double |  |  | NO | Childsub |
| ITM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ITM_CreatedDate | date |  |  | SI | Created Date |
| ITM_CreatedTime | time |  |  | SI | Created Time |
| ITM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ITM_Days | double |  |  | SI | Days |
| ITM_Main | varchar |  |  | SI | Main Service |
| ITM_RowId | varchar |  |  | NO | - |
| ITM_Sequence | varchar |  |  | SI | Sequence |
| ITM_Service_DR | bigint |  | FK | SI | Des Ref RBC_Service |
| ITM_UpdatedDate | date |  |  | SI | Updated Date |
| ITM_UpdatedTime | time |  |  | SI | Updated Time |
| ITM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*