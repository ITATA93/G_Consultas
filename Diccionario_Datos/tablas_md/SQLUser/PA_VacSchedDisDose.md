# SQLUser.PA_VacSchedDisDose

**Schema:** SQLUser
**Columnas:** 34
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DOSE_ParRef | varchar | PK |  | NO | PA_VacSchedDis Parent Reference |
| DOSE_ARCIM_DR | varchar |  | FK | SI | Des Ref ARCItmMast |
| DOSE_AdminLocation | varchar |  |  | SI | AdminLocation |
| DOSE_AdminRoute_DR | bigint |  | FK | SI | Des Ref PHCAdministrationRoute |
| DOSE_BodySite_DR | bigint |  | FK | SI | Des Ref OECBodySite |
| DOSE_Childsub | double |  |  | NO | Childsub |
| DOSE_DateOfAdmin | date |  |  | SI | DateOfAdmin |
| DOSE_DoseNumber | varchar |  |  | SI | DoseNumber |
| DOSE_Doseage | varchar |  |  | SI | Doseage |
| DOSE_ErrorReason_DR | bigint |  | FK | SI | Des Ref PACEnteredInErrorReason |
| DOSE_ExtBatchNumber | varchar |  |  | SI | ExtBatchNumber |
| DOSE_GivenBy | varchar |  |  | SI | GivenBy |
| DOSE_ICDDx_DR | bigint |  | FK | SI | Des Ref MRCICDDx |
| DOSE_ImmunisationNotes | varchar |  |  | SI | ImmunisationNotes |
| DOSE_IsDateOfAdminApprox | varchar |  |  | SI | IsDateOfAdminApprox |
| DOSE_OptOut | varchar |  |  | SI | OptOut |
| DOSE_OrdItem_DR | varchar |  | FK | SI | Des Ref OEOrdItem |
| DOSE_OrderItemFreeText | varchar |  |  | SI | OrderItemFreeText |
| DOSE_ReasonForChange | varchar |  |  | SI | ReasonForChange |
| DOSE_RowId | varchar |  |  | NO | - |
| DOSE_Text1 | varchar |  |  | SI | Text1 |
| DOSE_Text2 | varchar |  |  | SI | Text2 |
| DOSE_Text3 | varchar |  |  | SI | Text3 |
| DOSE_Text4 | varchar |  |  | SI | Text4 |
| DOSE_Text5 | varchar |  |  | SI | Text5 |
| DOSE_UpdateDate | date |  |  | SI | UpdateDate |
| DOSE_UpdateTime | time |  |  | SI | UpdateTime |
| DOSE_UpdateUser_DR | bigint |  | FK | SI | Des Ref SSUser |
| DOSE_VacSchedDisDose_DR | varchar |  | FK | SI | Des Ref PAVacSchedDisDose |
| DOSE_YesNo1 | varchar |  |  | SI | YesNo1 |
| DOSE_YesNo2 | varchar |  |  | SI | YesNo2 |
| DOSE_YesNo3 | varchar |  |  | SI | YesNo3 |
| DOSE_YesNo4 | varchar |  |  | SI | YesNo4 |
| DOSE_YesNo5 | varchar |  |  | SI | YesNo5 |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*