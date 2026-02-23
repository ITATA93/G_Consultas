# SQLUser.PA_TrafficAccidentDiagnosis

**Schema:** SQLUser
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TADG_ParRef | bigint | PK |  | NO | PA_TrafficAccident Parent Reference |
| TADG_Childsub | double |  |  | NO | Childsub |
| TADG_DiagAction_DR | bigint |  | FK | SI | Diagnosis Action |
| TADG_DiagCodingSys_DR | bigint |  | FK | SI | Diagnosis Coding System |
| TADG_DiagComments | varchar |  |  | SI | Diagnosis Comments |
| TADG_DiagDesc | varchar |  |  | SI | Diagnosis Description |
| TADG_DiagSide | varchar |  |  | SI | Diagnosis Side |
| TADG_Diagnosis_DR | bigint |  | FK | SI | Diagnosis Codes |
| TADG_LastUpdateDate | date |  |  | SI | LastUpdateDate |
| TADG_LastUpdateHospital_DR | bigint |  | FK | SI | Des Ref LastUpdateHospital |
| TADG_LastUpdateTime | time |  |  | SI | LastUpdateTime |
| TADG_LastUpdateUser_DR | bigint |  | FK | SI | Des Ref LastUpdateUser |
| TADG_PrimaryDiagInd | varchar |  |  | SI | Primary Diagnosis Indicator |
| TADG_RowId | varchar |  |  | NO | - |
| TADG_Snomed_DR | bigint |  | FK | SI | SNOMED Codes |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*