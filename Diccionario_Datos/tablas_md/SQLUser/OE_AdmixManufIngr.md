# SQLUser.OE_AdmixManufIngr

**Schema:** SQLUser
**Columnas:** 75
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INGR_ParRef | varchar | PK |  | NO | OE_AdmixManuf Parent Reference |
| INGR_AdjustedAmount | double |  |  | SI | Adjusted Amount |
| INGR_AdmixAdditive_DR | varchar |  | FK | SI | Des Ref OEAdmixAdditive |
| INGR_Admix_DR | bigint |  | FK | SI | Des Ref OEAdmix |
| INGR_Childsub | double |  |  | NO | Childsub |
| INGR_ExtDispenseID | varchar |  |  | SI | External DispenseID |
| INGR_ExtStkBatchID | varchar |  |  | SI | External Stock BatchID |
| INGR_ExtStkDetails | varchar |  |  | SI | External Stock Details |
| INGR_INCIRN_DR | varchar |  | FK | SI | Des Ref INCItmRegNo |
| INGR_INCLB_DR | varchar |  | FK | SI | Des Ref INCItmLcBt |
| INGR_Quantity | double |  |  | SI | Quantity |
| INGR_ReqQuantity | double |  |  | SI | Required Quantity |
| INGR_RowId | varchar |  |  | NO | - |
| INGR_WardDispense | varchar |  |  | SI | Ward Dispense |
| Q01 | - |  |  | SI | 3 - Clinical signs and symptoms of deep vein throm... |
| Q02 | - |  |  | SI | 3 - PE is number 1 Diagnosis, or equally likely |
| Q03 | - |  |  | SI | 1.5 - Heart rate > 100 |
| Q04 | - |  |  | SI | 1.5 - Immobilisation for at least 3 days, or surge... |
| Q05 | - |  |  | SI | 1.5 - Previous, objectively diagnosed pulmonary em... |
| Q06 | - |  |  | SI | 1 - Hemoptysis |
| Q07 | - |  |  | SI | 1 - Malignancy on treatment, treated in the last 6... |
| Q08 | - |  |  | SI | 1 - 1.5: Low risk |
| Q09 | - |  |  | SI | 2 - 6: Moderate risk |
| Q10 | - |  |  | SI | 6.5 - 12.5: High risk |
| Q11 | - |  |  | SI | The Wells' Criteria for Pulmonary Embolism estimat... |
| Q12 | - |  |  | SI | Date |
| Q13 | - |  |  | SI | Time |
| Q14 | - |  |  | SI | Score |
| Q15 | - |  |  | SI | Classification |
| Q16 | - |  |  | SI | 1 - 1.5 |
| Q17 | - |  |  | SI | 2 - 6 |
| Q18 | - |  |  | SI | 6.5 - 12.5 |
| Q19 | - |  |  | SI | Low risk |
| Q20 | - |  |  | SI | Moderate risk |
| Q21 | - |  |  | SI | High risk |
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

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*