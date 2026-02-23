# SQLUser.PA_TumorClinDiagReason

**Schema:** SQLUser
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CDR_ParRef | bigint | PK |  | NO | PA_Tumor Parent Reference |
| CDR_Childsub | double |  |  | NO | Childsub |
| CDR_ClinDiagReason_DR | bigint |  | FK | SI | Des Ref ClinDiagReason |
| CDR_Comment | varchar |  |  | SI | Comment |
| CDR_RowId | varchar |  |  | NO | - |
| CDR_UpdateDate | date |  |  | SI | UpdateDate |
| CDR_UpdateTime | time |  |  | SI | UpdateTime |
| CDR_UpdateUserHospital_DR | bigint |  | FK | SI | Des Ref UpdateUserHospital |
| CDR_UpdateUser_DR | bigint |  | FK | SI | Des REf UpdateUser |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*