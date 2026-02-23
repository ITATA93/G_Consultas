# SQLUser.PAC_InPatAdmTypePayor

**Schema:** SQLUser
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INS_ParRef | bigint | PK |  | NO | PAC_InPatAdmissionType Parent Reference |
| ChildQ19DR | - |  |  | SI | Child Reference: Physiotherapist goals |
| INS_AuxInsType_DR | bigint |  | FK | SI | Des Ref AuxInsType |
| INS_Childsub | double |  |  | NO | Childsub |
| INS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| INS_CreatedDate | date |  |  | SI | Created Date |
| INS_CreatedTime | time |  |  | SI | Created Time |
| INS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| INS_InsType_DR | bigint |  | FK | SI | Des Ref InsType |
| INS_RowId | varchar |  |  | NO | - |
| INS_UpdatedDate | date |  |  | SI | Updated Date |
| INS_UpdatedTime | time |  |  | SI | Updated Time |
| INS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q17Q1 | - |  |  | SI | Goal |
| Q17Q2 | - |  |  | SI | Timing |
| Q17Q3 | - |  |  | SI | Notes |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*