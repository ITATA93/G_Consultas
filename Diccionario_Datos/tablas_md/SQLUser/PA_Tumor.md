# SQLUser.PA_Tumor

**Schema:** SQLUser
**Columnas:** 52
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TUM_RowId | bigint | PK |  | NO | - |
| TUM_Active | varchar |  |  | SI | Active |
| TUM_AdmissRoute_DR | bigint |  | FK | SI | Des Ref AdmissRoute |
| TUM_CTZIP_DR | bigint |  | FK | SI | Des Ref to CTZIP |
| TUM_CancerReg_DR | bigint |  | FK | SI | Des Ref CancerReg |
| TUM_CancerStageSystem_DR | bigint |  | FK | SI | Des Ref MRCCancerClassification  |
| TUM_CityAtFirstDiag_DR | bigint |  | FK | SI | Des Ref CityAtFirstDiag |
| TUM_Comments | varchar |  |  | SI | Comments |
| TUM_CurrTreatmentCancer_DR | bigint |  | FK | SI | Des Ref CurrTreatment of Cancer |
| TUM_DateDeath | date |  |  | SI | Date of Death |
| TUM_DateFirstDiagEstimated | varchar |  |  | SI | Date of First Diag is Estimated |
| TUM_DateMetastatSpread | date |  |  | SI | Date of Metastatic Spread |
| TUM_DateRecurrence | date |  |  | SI | Date of Recurrence |
| TUM_DegreeDifferent_DR | bigint |  | FK | SI | Des Ref DegreeDifferent |
| TUM_DegreeProgress_DR | bigint |  | FK | SI | Des Ref DegreeProgress |
| TUM_DiagnMethodCancer_DR | bigint |  | FK | SI | Des Ref Diagn Method of Cancer |
| TUM_DiagnosedPrior | varchar |  |  | SI | Diagnosed Prior |
| TUM_DiagnosedWhere | varchar |  |  | SI | Diagnosed Where |
| TUM_FirstAdmDate | date |  |  | SI | FirstAdmDate |
| TUM_FirstDiagnosisDate | date |  |  | SI | First Diagnosis Date |
| TUM_FirstDiagnosisPlace_DR | bigint |  | FK | SI | Des REf to FirstDiagnosisPlace |
| TUM_FreeText1 | varchar |  |  | SI | Free Text 1 |
| TUM_FreeText2 | varchar |  |  | SI | Free Text 2 |
| TUM_FreeText3 | varchar |  |  | SI | Free Text 3 |
| TUM_HistDeliv_DR | bigint |  | FK | SI | Des Ref HistDeliv |
| TUM_HistologicalSite | varchar |  |  | SI | Histological Site |
| TUM_HistoryTreatment_DR | bigint |  | FK | SI | Des Ref HistoryTreatment |
| TUM_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| TUM_LastUpdateDate | date |  |  | SI | LastUpdateDate |
| TUM_LastUpdateTime | time |  |  | SI | LastUpdateTime |
| TUM_LastUpdateUser_DR | bigint |  | FK | SI | Des Ref LastUpdateUser |
| TUM_Laterality_DR | bigint |  | FK | SI | Des Ref Laterality |
| TUM_LocalDoctor_DR | varchar |  | FK | SI | Des Ref LocalDoctor |
| TUM_MetastaticSite | varchar |  |  | SI | Metastatic Site |
| TUM_MorphologyText | varchar |  |  | SI | Morphology Text |
| TUM_Morphology_DR | bigint |  | FK | SI | Des Ref Morphology |
| TUM_PathologicDiagnosis_DR | bigint |  | FK | SI | Des MRCIDx Pathologic Diagnosis |
| TUM_PrimarySiteCancer | varchar |  |  | SI | Primary Site of Cancer |
| TUM_Province_DR | bigint |  | FK | SI | Des Ref CTProvince  |
| TUM_RegistrationAtScreening | varchar |  |  | SI | Registration At Screening |
| TUM_Speciality_DR | bigint |  | FK | SI | Des Ref CTLOC |
| TUM_Specify | varchar |  |  | SI | Specify |
| TUM_StageCancerAtDiag_DR | bigint |  | FK | SI | Des Ref MRCDiagCancerStage  |
| TUM_SurvivalPeriods | varchar |  |  | SI | Survival Periods |
| TUM_TreatingDoctor_DR | varchar |  | FK | SI | Des Ref TreatingDoctor |
| TUM_TumorType_DR | bigint |  | FK | SI | Des Ref TumorType |
| TUM_TumourSize | varchar |  |  | SI | Tumour Size |
| TUM_UpdateDate | date |  |  | SI | UpdateDate |
| TUM_UpdateTime | time |  |  | SI | UpdateTime |
| TUM_UpdateUserHospital_DR | bigint |  | FK | SI | Des Ref UpdateUserHospital |
| TUM_UpdateUser_DR | bigint |  | FK | SI | Des Ref UpdateUser |
| TUM_ZipAtFirstDiag_DR | bigint |  | FK | SI | Des Ref ZipAtFirstDiag |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*