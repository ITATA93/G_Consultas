# SQLUser.PHC_GenericRtFormsPBSRule

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PBSRULE_ParRef | varchar | PK |  | NO | PHC_GenericRtForms Parent Reference |
| PBSRULE_Childsub | double |  |  | NO | Childsub |
| PBSRULE_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PBSRULE_CreatedDate | date |  |  | SI | Created Date |
| PBSRULE_CreatedTime | time |  |  | SI | Created Time |
| PBSRULE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PBSRULE_DateFrom | date |  |  | SI | Date From |
| PBSRULE_DateTo | date |  |  | SI | Date To |
| PBSRULE_PrescribingRule_DR | bigint |  | FK | SI | PBS Prescribing Rule |
| PBSRULE_RowId | varchar |  |  | NO | - |
| PBSRULE_UpdatedDate | date |  |  | SI | Updated Date |
| PBSRULE_UpdatedTime | time |  |  | SI | Updated Time |
| PBSRULE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*