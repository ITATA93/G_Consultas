# SQLUser.PA_PersonAdmInsBGLimits

**Schema:** SQLUser
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LIM_ParRef | varchar | PK |  | NO | PA_Person Parent Reference |
| LIM_ARCIM_DR | varchar |  | FK | SI | Des Ref ARCIM |
| LIM_BillGroup_DR | bigint |  | FK | SI | Des Ref BillGroup |
| LIM_BillSub_DR | varchar |  | FK | SI | Des Ref BillSub |
| LIM_Childsub | double |  |  | NO | Childsub |
| LIM_CoPaymentPercentage | double |  |  | SI | Co-Payment Percentage |
| LIM_DateFrom | date |  |  | SI | DateFrom |
| LIM_DateTo | date |  |  | SI | DateTo |
| LIM_EpisSubType_DR | bigint |  | FK | SI | Des Ref EpisSubType |
| LIM_EpisodeType | varchar |  |  | SI | EpisodeType |
| LIM_MaxCoPayAmountBeforeTax | double |  |  | SI | Maximum Co-Payment Amount Before Tax |
| LIM_MaxCoPaymentAmount | double |  |  | SI | Maximum Co-Payment Amount |
| LIM_MinCoPaymentAmount | double |  |  | SI | Minimum Co-Payment Amount |
| LIM_PatientAmount | double |  |  | SI | Patient Amount |
| LIM_PayorMaximumLimit | double |  |  | SI | Payor Maximum Limit |
| LIM_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*