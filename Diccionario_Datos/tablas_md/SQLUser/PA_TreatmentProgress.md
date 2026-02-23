# SQLUser.PA_TreatmentProgress

**Schema:** SQLUser
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TRPR_ParRef | bigint | PK |  | NO | PA_PatMas Parent Reference |
| TRPR_Childsub | double |  |  | NO | Childsub |
| TRPR_RefDate | date |  |  | SI | RefDate |
| TRPR_RowId | varchar |  |  | NO | - |
| TRPR_Text1 | varchar |  |  | SI | Text1 |
| TRPR_Text2 | varchar |  |  | SI | Text2 |
| TRPR_TreatReason_DR | bigint |  | FK | SI | Des Ref TreatReason |
| TRPR_TreatmentDate | date |  |  | SI | TreatmentDate |
| TRPR_UpdateDate | date |  |  | SI | UpdateDate |
| TRPR_UpdateHospital_DR | bigint |  | FK | SI | Des Ref UpdateHospital |
| TRPR_UpdateTime | time |  |  | SI | UpdateTime |
| TRPR_UpdateUser_DR | bigint |  | FK | SI | Des Ref UpdateUser |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*