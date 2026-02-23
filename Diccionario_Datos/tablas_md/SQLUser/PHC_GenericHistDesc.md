# SQLUser.PHC_GenericHistDesc

**Schema:** SQLUser
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HISTDESC_ParRef | bigint | PK |  | NO | PHC_Generic Parent Reference |
| HISTDESC_Childsub | double |  |  | NO | Childsub |
| HISTDESC_CreatedDate | date |  |  | SI | Created Date |
| HISTDESC_CreatedTime | time |  |  | SI | Created Time |
| HISTDESC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| HISTDESC_DateFrom | date |  |  | SI | Date From |
| HISTDESC_DateTo | date |  |  | SI | Date To |
| HISTDESC_Description | varchar |  |  | SI | Description |
| HISTDESC_OrgDescription | varchar |  |  | SI | Is Original Description |
| HISTDESC_RowId | varchar |  |  | NO | - |
| HISTDESC_TimeFrom | time |  |  | SI | Time From |
| HISTDESC_TimeTo | time |  |  | SI | Time From |
| HISTDESC_UpdatedDate | date |  |  | SI | Updated Date |
| HISTDESC_UpdatedTime | time |  |  | SI | Updated Time |
| HISTDESC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*