# SQLUser.PA_TrafficAccidentWorkCapacity

**Schema:** SQLUser
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| WAC_ParRef | bigint | PK |  | NO | PA_TrafficAccident Parent Reference |
| WAC_ACCContProv | varchar |  |  | SI | ACC Contact Provider |
| WAC_AltWorkTypeCode_DR | bigint |  | FK | SI | Alternative Work Type Code |
| WAC_AssistReq | varchar |  |  | SI | Assistance Required |
| WAC_AssistType_DR | bigint |  | FK | SI | Assistance Type |
| WAC_Childsub | double |  |  | NO | Childsub |
| WAC_IncapComments | varchar |  |  | SI | Incapacity Comments |
| WAC_IncapDateFrom | date |  |  | SI | Incapacity Date From |
| WAC_IncapDateTo | date |  |  | SI | Incapacity Date To |
| WAC_IncapacityType_DR | bigint |  | FK | SI | Incapacity Type |
| WAC_IssueDetails | varchar |  |  | SI | Issue Details |
| WAC_MedCertIdentifier | varchar |  |  | SI | Medical Certificate Identifier |
| WAC_PhysicalRest | varchar |  |  | SI | Physical Restrictions  |
| WAC_RestDayWeek | double |  |  | SI | Restricted Days per Week |
| WAC_RestHrDay | double |  |  | SI | Restricted Hours Per Day |
| WAC_Restrictions | varchar |  |  | SI | Restriction Comments |
| WAC_ResumeWork | varchar |  |  | SI | Can Resume Normal Work |
| WAC_ReturnToWork | date |  |  | SI | Return to Normal Work Date |
| WAC_RevIncapDate | date |  |  | SI | Review Incapacity Date |
| WAC_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*