# SQLUser.PHC_GenericRtFormsSubs

**Schema:** SQLUser
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SUBS_ParRef | varchar | PK |  | NO | PHC_GenericRtForms Parent Reference |
| SUBS_Childsub | double |  |  | NO | Childsub |
| SUBS_CreatedDate | date |  |  | SI | Created Date |
| SUBS_CreatedTime | time |  |  | SI | Created Time |
| SUBS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SUBS_GenRtForm_DR | varchar |  | FK | SI | Des Ref GenRtForm |
| SUBS_RowId | varchar |  |  | NO | - |
| SUBS_UpdatedDate | date |  |  | SI | Updated Date |
| SUBS_UpdatedTime | time |  |  | SI | Updated Time |
| SUBS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*