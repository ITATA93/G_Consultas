# SQLUser.OE_AdmixAdditiveAllocation

**Schema:** SQLUser
**Columnas:** 85
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| AAA_ParRef | varchar | PK |  | NO | OEAdmixAdditive Parent Reference |
| AAA_Childsub | double |  |  | NO | Childsub |
| AAA_Form_DR | bigint |  | FK | SI | Des Ref to PHCForm |
| AAA_ItmMast_DR | varchar |  | FK | SI | Des Ref to ARCIM |
| AAA_Quantity | double |  |  | SI | Quantity |
| AAA_RowId | varchar |  |  | NO | - |
| AAA_Strength_DR | bigint |  | FK | SI | Des Ref to PHCStrength |
| Q01 | - |  |  | SI | Build / Weight for Height |
| Q02 | - |  |  | SI | Skin Type Visual Risk Areas |
| Q03 | - |  |  | SI | Continence |
| Q04 | - |  |  | SI | Age |
| Q05 | - |  |  | SI | Mobility |
| Q06 | - |  |  | SI | Appetite |
| Q07 | - |  |  | SI | Tissue malnutrition |
| Q08 | - |  |  | SI | Neurological deficit |
| Q09 | - |  |  | SI | Major Surgery / Trauma |
| Q10 | - |  |  | SI | Medication |
| Q11 | - |  |  | SI | 10+ At risk |
| Q12 | - |  |  | SI | 15+ High risk |
| Q13 | - |  |  | SI | 20+ Very high risk |
| Q14 | - |  |  | SI | The Waterlow scale gives an estimated risk for the... |
| Q15 | - |  |  | SI | Sex |
| Q16 | - |  |  | SI | Neurological deficit (score) |
| Q17 | - |  |  | SI | Date |
| Q18 | - |  |  | SI | Medication Score |
| Q18a | - |  |  | SI | Medication Score |
| Q21 | - |  |  | SI | Skin type visual risk areas |
| Q22 | - |  |  | SI | Time |
| Q23 | - |  |  | SI | Score |
| Q24 | - |  |  | SI | Classification |
| Q25 | - |  |  | SI | 0 - 9 |
| Q26 | - |  |  | SI | No risk |
| Q27 | - |  |  | SI | 10 - 14 |
| Q28 | - |  |  | SI | At risk |
| Q29 | - |  |  | SI | 15 - 19 |
| Q30 | - |  |  | SI | High risk |
| Q31 | - |  |  | SI | > 20 |
| Q32 | - |  |  | SI | Very high risk |
| Q33 | - |  |  | SI | 0 - 9: No risk |
| Q34 | - |  |  | SI | 10 - 14: At risk |
| Q35 | - |  |  | SI | 15 - 19: High Risk |
| Q36 | - |  |  | SI | > 20: Very high risk |
| Q37 | - |  |  | SI | Neurological deficit - Diabetes/ MS/ CVA/ motor/ s... |
| Q38 | - |  |  | SI | Medication - Cytotoxic, anti-inflammatory, long te... |
| Q9a | - |  |  | SI | Major Surgery / Trauma |
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