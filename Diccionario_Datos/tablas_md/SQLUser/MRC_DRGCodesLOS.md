# SQLUser.MRC_DRGCodesLOS

**Schema:** SQLUser
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LOS_ParRef | bigint | PK |  | NO | MRC_DRGCodes Parent Reference |
| ChildQ34DR | - |  |  | SI | Child Reference: Ojos |
| LOS_Average | double |  |  | SI | LOS Average |
| LOS_Childsub | double |  |  | NO | Childsub |
| LOS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LOS_CreatedDate | date |  |  | SI | Created Date |
| LOS_CreatedTime | time |  |  | SI | Created Time |
| LOS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LOS_DateFrom | date |  |  | SI | Date From |
| LOS_DateTo | date |  |  | SI | Date To |
| LOS_HighTrim | double |  |  | SI | LOS High Trim |
| LOS_Hospital_DR | bigint |  | FK | SI | Des Ref CTHospital |
| LOS_LowTrim | double |  |  | SI | LOS Low Trim |
| LOS_PostOffice_DR | bigint |  | FK | SI | Des Ref ARCPostOffice |
| LOS_RowId | varchar |  |  | NO | - |
| LOS_UpdatedDate | date |  |  | SI | Updated Date |
| LOS_UpdatedTime | time |  |  | SI | Updated Time |
| LOS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q14Q1 | - |  |  | SI | Área |
| Q14Q2 | - |  |  | SI | Resultado |
| Q14Q3 | - |  |  | SI | Observaciones |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*