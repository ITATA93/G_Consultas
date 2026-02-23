# SQLUser.AR_HICBulkBillVouchHisSer

**Schema:** SQLUser
**Columnas:** 71
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuentas por Cobrar (AR)**. Facturación y cobranza de pacientes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SH_ParRef | varchar | PK |  | NO | AR_HICBulkBillVouchHis Parent Reference |
| Q01 | - |  |  | SI | Fecha de Ingreso Programa |
| Q02 | - |  |  | SI | Fecha de Egreso Programa |
| Q03 | - |  |  | SI | Tipo de Egreso |
| Q04 | - |  |  | SI | Profesional |
| Q05 | - |  |  | SI | Tipo de Plan de Tratamiento |
| Q06 | - |  |  | SI | Grupos Síndromes Diagnósticos |
| QUESAnaDR | - |  |  | SI | Anaesthesia |
| QUESAnaOperationDR | - |  |  | SI | Operation |
| QUESConsultDR | - |  |  | SI | Consult |
| QUESCopiedComments | - |  |  | SI | Copied Comments |
| QUESCopiedDate | - |  |  | SI | Copied Date |
| QUESCopiedEpDR | - |  |  | SI | Copied Episode |
| QUESCopiedSourceDR | - |  |  | SI | Copied Source DR |
| QUESCopiedTime | - |  |  | SI | Copied Time |
| QUESCopiedUserDR | - |  |  | SI | Copied User |
| QUESCreateDate | - |  |  | SI | Creation Date |
| QUESCreateTime | - |  |  | SI | Creation Time |
| QUESCreateUserDR | - |  |  | SI | Creation User |
| QUESDate | - |  |  | SI | Last Update Date |
| QUESErrorReasonDR | - |  |  | SI | Error Reason |
| QUESFHResidentDR | - |  |  | SI | Resident |
| QUESMRClinicalPathWaysDR | - |  |  | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | - |  |  | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | - |  |  | SI | Order Execution |
| QUESORPreanaestheticConsultDR | - |  |  | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | - |  |  | SI | Observation Entry |
| QUESOperRoomDR | - |  |  | SI | Operating Room |
| QUESPAAdmDR | - |  |  | SI | Admission |
| QUESPAAdverseEventDR | - |  |  | SI | Adverse Event |
| QUESPAPatMasDR | - |  |  | SI | Patient |
| QUESPAPregnancyDR | - |  |  | SI | Pregnancy |
| QUESPAWaitingListDR | - |  |  | SI | Waiting List |
| QUESPathwayItemDR | - |  |  | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | - |  |  | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | - |  |  | SI | Appointments |
| QUESRBApptOutcomeDR | - |  |  | SI | Appointment Outcome |
| QUESRBApptSlotDR | - |  |  | SI | Appointment Slot |
| QUESReasonForCorrectionDR | - |  |  | SI | Reason for Correction |
| QUESSSUserDefWindowDR | - |  |  | SI | Questionnaire |
| QUESScore | - |  |  | SI | Score |
| QUESSecondUserDR | - |  |  | SI | Second Signature |
| QUESStatusDR | - |  |  | SI | Status |
| QUESTextResultDR | - |  |  | SI | Text Result |
| QUESTime | - |  |  | SI | Last Update Time |
| QUESTransactionDR | - |  |  | SI | Transaction |
| QUESUserDR | - |  |  | SI | Last Update User |
| SH_AccessionDateTime | varchar |  |  | SI | AccessionDateTime |
| SH_AccountReferenceNum | varchar |  |  | SI | Account Reference Number |
| SH_AfterCareOverrideInd | varchar |  |  | SI | AfterCareOverrideInd    |
| SH_ChargeAmount | double |  |  | SI | Charge Amount |
| SH_Childsub | double |  |  | NO | Childsub |
| SH_CollectionDateTime | varchar |  |  | SI | CollectionDateTime |
| SH_DistanceKms | double |  |  | SI | Distance Kms |
| SH_DuplicateServiceOverrideInd | varchar |  |  | SI | DuplicateServiceOverrideInd   |
| SH_EquipmentId | varchar |  |  | SI | Equipment Id |
| SH_FieldQuantity | double |  |  | SI | Field Quantity |
| SH_HospitalInd | varchar |  |  | SI | Hospital Indicator |
| SH_ItemNum | varchar |  |  | SI | Item Num |
| SH_LSPNum | varchar |  |  | SI | LSP Number |
| SH_MultipleProcedureOverrideInd | varchar |  |  | SI | MultipleProcedureOverrideInd  |
| SH_NoOfPatientsSeen | varchar |  |  | SI | No Of Patients Seen |
| SH_OEOrdItem_DR | varchar |  | FK | SI | Des Ref OEOrdItem |
| SH_RestrictiveOverrideCde | varchar |  |  | SI | RestrictiveOverrideCde |
| SH_RowId | varchar |  |  | NO | - |
| SH_Rule3ExemptInd | varchar |  |  | SI | Rule3ExemptInd |
| SH_S4b3ExemptInd | varchar |  |  | SI | S4b3ExemptInd |
| SH_SelfDeemedCde | varchar |  |  | SI | Self Deemed Code |
| SH_ServiceId | varchar |  |  | SI | ServiceId |
| SH_ServiceText | varchar |  |  | SI | ServiceText |
| SH_TimeDuration | varchar |  |  | SI | TimeDuration |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*