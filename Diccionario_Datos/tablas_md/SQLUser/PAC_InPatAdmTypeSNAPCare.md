# SQLUser.PAC_InPatAdmTypeSNAPCare

**Schema:** SQLUser
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SNAP_ParRef | bigint | PK |  | NO | PAC_InPatAdmissionType Parent Reference |
| ChildQ21DR | - |  |  | SI | Child Reference: Logopedist goals |
| Q19Q1 | - |  |  | SI | Goal |
| Q19Q2 | - |  |  | SI | Timing |
| Q19Q3 | - |  |  | SI | Notes |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| SNAP_Childsub | double |  |  | NO | Childsub |
| SNAP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SNAP_CreatedDate | date |  |  | SI | Created Date |
| SNAP_CreatedTime | time |  |  | SI | Created Time |
| SNAP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SNAP_RowId | varchar |  |  | NO | - |
| SNAP_SNAPCareType_DR | bigint |  | FK | SI | Des Ref SNAPCareType |
| SNAP_UpdatedDate | date |  |  | SI | Updated Date |
| SNAP_UpdatedTime | time |  |  | SI | Updated Time |
| SNAP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*