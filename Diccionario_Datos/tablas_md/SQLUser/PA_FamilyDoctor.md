# SQLUser.PA_FamilyDoctor

**Schema:** SQLUser
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| FAMD_ParRef | bigint | PK |  | NO | PA_PatMas Parent Reference |
| FAMD_Childsub | double |  |  | NO | Childsub |
| FAMD_DateFrom | date |  |  | SI | DateFrom |
| FAMD_DateTo | date |  |  | SI | DateTo |
| FAMD_FamDoc_DR | bigint |  | FK | SI | Des Ref FamDoc |
| FAMD_Involvement | varchar |  |  | SI | Involvement |
| FAMD_RefDocClinc_DR | varchar |  | FK | SI | Des Ref RefDocClinc |
| FAMD_RowId | varchar |  |  | NO | - |
| FAMD_UpdateDate | date |  |  | SI | Update Date |
| FAMD_UpdateHospital_DR | bigint |  | FK | SI | Des Ref UpdateHospital |
| FAMD_UpdateTime | time |  |  | SI | Update Time |
| FAMD_UpdateUser_DR | bigint |  | FK | SI | Des Ref UpdateUser |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*