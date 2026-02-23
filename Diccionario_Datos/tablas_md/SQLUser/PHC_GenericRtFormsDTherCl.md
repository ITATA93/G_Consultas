# SQLUser.PHC_GenericRtFormsDTherCl

**Schema:** SQLUser
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DTC_ParRef | varchar | PK |  | NO | PHC_GenericRtForms Parent Reference |
| DTC_Childsub | double |  |  | NO | Childsub |
| DTC_CreatedDate | date |  |  | SI | Created Date |
| DTC_CreatedTime | time |  |  | SI | Created Time |
| DTC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DTC_DuplTherClass_DR | bigint |  | FK | SI | Des Ref DuplTherClass |
| DTC_RowId | varchar |  |  | NO | - |
| DTC_UpdatedDate | date |  |  | SI | Updated Date |
| DTC_UpdatedTime | time |  |  | SI | Updated Time |
| DTC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*