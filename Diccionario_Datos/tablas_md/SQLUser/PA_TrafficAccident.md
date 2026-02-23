# SQLUser.PA_TrafficAccident

**Schema:** SQLUser
**Columnas:** 97
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TRF_RowId | bigint | PK |  | NO | - |
| TRF_ACCContProv | varchar |  |  | SI | [DEPRECATED]<br>
Deprecated in release: <Deprecat... |
| TRF_AccidentCause | varchar |  |  | SI | Cause of Accident |
| TRF_AccidentCode_DR | bigint |  | FK | SI | Des REf TRF_AccidentCode_DR |
| TRF_AccidentDate | date |  |  | SI | Accident Date |
| TRF_AccidentLocCode_DR | bigint |  | FK | SI | Accident Location Code |
| TRF_AccidentTime | time |  |  | SI | Accident Time |
| TRF_AdmitHospital | varchar |  |  | SI | Admitted To Hospital |
| TRF_AltWorkTypeCode_DR | bigint |  | FK | SI | [DEPRECATED]<br>
Deprecated in release: <Deprecat... |
| TRF_AssistCentre | varchar |  |  | SI | Assist Centre |
| TRF_AssistReq | varchar |  |  | SI | [DEPRECATED]<br>
Deprecated in release: <Deprecat... |
| TRF_AssistType_DR | bigint |  | FK | SI | [DEPRECATED]<br>
Deprecated in release: <Deprecat... |
| TRF_CareProvider_DR | varchar |  | FK | SI | Care Provider |
| TRF_CourtCity | varchar |  |  | SI | Court City |
| TRF_CourtNumber | varchar |  |  | SI | Court Number |
| TRF_DiagAction_DR | bigint |  | FK | SI | Diagnosis Action |
| TRF_DiagCodes | varchar |  |  | SI | Diagnosis Codes |
| TRF_DiagCodingSys_DR | bigint |  | FK | SI | Diagnosis Coding System |
| TRF_DiagComments | varchar |  |  | SI | Diagnosis Comments |
| TRF_DiagDesc | varchar |  |  | SI | Diagnosis Description |
| TRF_DiagSide | varchar |  |  | SI | Diagnosis Side |
| TRF_Employer | varchar |  |  | SI | Employer |
| TRF_Episodes | varchar |  |  | SI | List of Episodes |
| TRF_GradProcInjury | varchar |  |  | SI | Gradual Process Injury |
| TRF_ICD1_DR | bigint |  | FK | SI | Des Ref ICD1 |
| TRF_ICD2_DR | bigint |  | FK | SI | Des Ref ICD2 |
| TRF_ID | varchar |  |  | SI | ID |
| TRF_IncapComments | varchar |  |  | SI | [DEPRECATED]<br>
Deprecated in release: <Deprecat... |
| TRF_IncapDateFrom | date |  |  | SI | [DEPRECATED]<br>
Deprecated in release: <Deprecat... |
| TRF_IncapDateTo | date |  |  | SI | [DEPRECATED]<br>
Deprecated in release: <Deprecat... |
| TRF_IncapacityType_DR | bigint |  | FK | SI | [DEPRECATED]<br>
Deprecated in release: <Deprecat... |
| TRF_InformedEmployer | varchar |  |  | SI | Informed Employer |
| TRF_Injury | varchar |  |  | SI | Injury |
| TRF_InsType_DR | bigint |  | FK | SI | Des Ref InsType |
| TRF_InvolvesVehicle | varchar |  |  | SI | Involves Vehicle |
| TRF_IssueDetails | varchar |  |  | SI | [DEPRECATED]<br>
Deprecated in release: <Deprecat... |
| TRF_LastUpdateDate | date |  |  | SI | LastUpdateDate |
| TRF_LastUpdateHospital_DR | bigint |  | FK | SI | Des Ref LastUpdateHospital |
| TRF_LastUpdateTime | time |  |  | SI | LastUpdateTime |
| TRF_LastUpdateUser_DR | bigint |  | FK | SI | Des Ref LastUpdateUser |
| TRF_LocationInj_DR | bigint |  | FK | SI | Des Ref LocationInj |
| TRF_MedTreatInjury | varchar |  |  | SI | Medical Treatment Injury |
| TRF_Notes | varchar |  |  | SI | Notes |
| TRF_OwnerAddress | varchar |  |  | SI | Owner Address |
| TRF_OwnerCity | varchar |  |  | SI | Owner City |
| TRF_OwnerFaxNo | varchar |  |  | SI | OwnerFaxNo |
| TRF_OwnerID | varchar |  |  | SI | Owner Id |
| TRF_OwnerName1 | varchar |  |  | SI | Owner Name1 |
| TRF_OwnerPhone1 | varchar |  |  | SI | Owner Phone1 |
| TRF_OwnerProvince_DR | bigint |  | FK | SI | Des REf Province |
| TRF_OwnerZipCode | varchar |  |  | SI | OwnerZipCode |
| TRF_PatientRole_DR | bigint |  | FK | SI | Des Ref PatientRole |
| TRF_PayorBill_DR | bigint |  | FK | SI | Payor Bill - Des Ref ARPatientBill |
| TRF_Person_DR | bigint |  | FK | SI | Des Ref Person |
| TRF_PhysicalRest | varchar |  |  | SI | [DEPRECATED]<br>
Deprecated in release: <Deprecat... |
| TRF_Place | varchar |  |  | SI | Place |
| TRF_PoliceBadge | varchar |  |  | SI | Police Badge |
| TRF_PoliceStation | varchar |  |  | SI | Police Station |
| TRF_PrimaryDiagInd | varchar |  |  | SI | Primary Diagnosis Indicator |
| TRF_PurchaseOrderNum | varchar |  |  | SI | Purchase Order Number |
| TRF_ReferralReason | varchar |  |  | SI | Referral Reason |
| TRF_RestDayWeek | double |  |  | SI | [DEPRECATED]<br>
Deprecated in release: <Deprecat... |
| TRF_RestHrDay | double |  |  | SI | [DEPRECATED]<br>
Deprecated in release: <Deprecat... |
| TRF_Restrictions | varchar |  |  | SI | [DEPRECATED]<br>
Deprecated in release: <Deprecat... |
| TRF_ResumeWork | varchar |  |  | SI | [DEPRECATED]<br>
Deprecated in release: <Deprecat... |
| TRF_ReturnToWork | date |  |  | SI | [DEPRECATED]<br>
Deprecated in release: <Deprecat... |
| TRF_RevIncapDate | date |  |  | SI | [DEPRECATED]<br>
Deprecated in release: <Deprecat... |
| TRF_ServiceRank | varchar |  |  | SI | Service Rank |
| TRF_ShipName | varchar |  |  | SI | Ship Name |
| TRF_SnomedTerms | varchar |  |  | SI | SNOMED Codes |
| TRF_SportInjury | varchar |  |  | SI | Sport Injury |
| TRF_SportNameCode_DR | bigint |  | FK | SI | Sport Name Code - Des Ref PACSportNameCode |
| TRF_Veh2Model | varchar |  |  | SI | Veh2 Model |
| TRF_Veh3Model | varchar |  |  | SI | Veh 3 Model |
| TRF_VehDriverAddress2 | varchar |  |  | SI | Veh Driver Address 2 |
| TRF_VehDriverAddress3 | varchar |  |  | SI | Veh Driver Address 2 |
| TRF_VehDriverCity | varchar |  |  | SI | Driver City |
| TRF_VehDriverID | varchar |  |  | SI | VehDriverID |
| TRF_VehDriverName | varchar |  |  | SI | VehDriverName |
| TRF_VehDriverName2 | varchar |  |  | SI | Veh Driver Name 2 |
| TRF_VehDriverName3 | varchar |  |  | SI | Veh Driver Name 3 |
| TRF_VehDriverPh2 | varchar |  |  | SI | Veh Driver Ph 2 |
| TRF_VehDriverPh3 | varchar |  |  | SI | Veh Driver Ph 3 |
| TRF_VehDriverPhone | varchar |  |  | SI | VehDriverPhone |
| TRF_VehDriverProvince_DR | bigint |  | FK | SI | Des REf VehDriverProvince |
| TRF_VehInsComp2 | varchar |  |  | SI | Veh Ins Comp2 |
| TRF_VehInsComp3 | varchar |  |  | SI | Veh Ins Company 3 |
| TRF_VehInsCompany | varchar |  |  | SI | Veh Ins Company |
| TRF_VehInsPolicy | varchar |  |  | SI | Veh Ins Policy |
| TRF_VehMake | varchar |  |  | SI | VehMake |
| TRF_VehModel | varchar |  |  | SI | Veh  Model |
| TRF_VehReg4 | varchar |  |  | SI | Vehicle Rego 4 |
| TRF_VehReq | varchar |  |  | SI | Veh Req |
| TRF_VehReq2 | varchar |  |  | SI | Veh Req 2 |
| TRF_VehReq3 | varchar |  |  | SI | Veh Req 3 |
| TRF_WorkInjury | varchar |  |  | SI | Work Injury |
| TRF_WorkTypeCode_DR | bigint |  | FK | SI | Work Type Code - Des Ref PACWorkTypeCode |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*