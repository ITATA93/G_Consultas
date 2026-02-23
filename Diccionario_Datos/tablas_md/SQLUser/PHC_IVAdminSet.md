# SQLUser.PHC_IVAdminSet

**Schema:** SQLUser
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| IVADM_RowId | bigint | PK |  | NO | - |
| IVADM_Code | varchar |  |  | NO | Code |
| IVADM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| IVADM_CreatedDate | date |  |  | SI | Created Date |
| IVADM_CreatedTime | time |  |  | SI | Created Time |
| IVADM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| IVADM_DateFrom | date |  |  | SI | Date From |
| IVADM_DateTo | date |  |  | SI | Date To |
| IVADM_Desc | varchar |  |  | NO | Description |
| IVADM_DropsPerMl | double |  |  | SI | DropsPerMl |
| IVADM_Owner | varchar |  |  | SI | Owner |
| IVADM_UpdatedDate | date |  |  | SI | Updated Date |
| IVADM_UpdatedTime | time |  |  | SI | Updated Time |
| IVADM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*