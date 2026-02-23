# SQLUser.MRC_ClinPathWaysEpDaysOS

**Schema:** SQLUser
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OS_ParRef | varchar | PK |  | NO | MRC_ClinPathwEpDays Parent Reference |
| OS_ARCIM_DR | varchar |  | FK | SI | Des Ref ARCIM |
| OS_Childsub | double |  |  | NO | Childsub |
| OS_CreatedDate | date |  |  | SI | Created Date |
| OS_CreatedTime | time |  |  | SI | Created Time |
| OS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| OS_OrdSet_DR | varchar |  | FK | SI | Des Ref OrdSet |
| OS_RowId | varchar |  |  | NO | - |
| OS_UpdatedDate | date |  |  | SI | Updated Date |
| OS_UpdatedTime | time |  |  | SI | Updated Time |
| OS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q160Q1 | - |  |  | SI | Bebé Número |
| Q160Q2 | - |  |  | SI | Lactancia |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*