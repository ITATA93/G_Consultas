# SQLUser.PA_CustomExtractReport

**Schema:** SQLUser
**Columnas:** 129
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Extensión de datos adicionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REP_ParRef | bigint | PK |  | NO | PA_CustomExtract Parent Reference |
| Q01 | - |  |  | SI | Build / Weight for Height |
| Q02 | - |  |  | SI | Skin Type Visual Risk Areas |
| Q03 | - |  |  | SI | Continence |
| Q04 | - |  |  | SI | Age |
| Q05 | - |  |  | SI | Mobility |
| Q07 | - |  |  | SI | Tissue malnutrition |
| Q08 | - |  |  | SI | Neurological deficit |
| Q09 | - |  |  | SI | Major Surgery or Trauma |
| Q10 | - |  |  | SI | Medication |
| Q11 | - |  |  | SI | 10+ At risk |
| Q12 | - |  |  | SI | 15+ High risk |
| Q13 | - |  |  | SI | 20+ Very high risk |
| Q14 | - |  |  | SI | The Waterlow score gives an estimated risk for the... |
| Q15 | - |  |  | SI | Sex |
| Q16 | - |  |  | SI | Neurological deficit (score) |
| Q17 | - |  |  | SI | Date |
| Q18 | - |  |  | SI | Malnutrition Screening Tool (MST) |
| Q18a | - |  |  | SI | Medication (score) |
| Q19 | - |  |  | SI | Has patient lost weight recently? |
| Q20 | - |  |  | SI | Weight loss score |
| Q21 | - |  |  | SI | Patient eating poorly or lack of appetite |
| Q22 | - |  |  | SI | Nutrition score (calculated) |
| Q22b | - |  |  | SI | Nutrition score (calculated) |
| Q23 | - |  |  | SI | If Nutrition score >2 refer for nutrition assessme... |
| Q24 | - |  |  | SI | Total score |
| Q24b | - |  |  | SI | Total score |
| Q24c | - |  |  | SI | Total score |
| Q28 | - |  |  | SI | Special risks |
| Q29 | - |  |  | SI | < 10 No risk |
| Q2a | - |  |  | SI | Skin Type Visual Risk Areas |
| Q30 | - |  |  | SI | Medication - Cytotoxics, long term/high dose stero... |
| Q31 | - |  |  | SI | Neurological deficit - Diabetes, MS, CVA, Motor/Se... |
| Q33 | - |  |  | SI | The Waterlow Scale should be used in conjunction w... |
| Q34 | - |  |  | SI | As a result of the assessment, patients will be ei... |
| Q35 | - |  |  | SI | More than one option can be selected against the f... |
| Q36 | - |  |  | SI | This questionnaire incorporates the Australian Mal... |
| Q37 | - |  |  | SI | Please, note that the MST Nutrition Score will not... |
| Q38 | - |  |  | SI | Guidance |
| Q39 | - |  |  | SI | Waterlow score |
| Q40 | - |  |  | SI | MST score |
| Q43 | - |  |  | SI | <=2 Nutrition assessment/intervention not required |
| Q44 | - |  |  | SI | >2 Refer for nutrition assessment/intervention |
| Q45 | - |  |  | SI | The neurological deficit score can vary between 4 ... |
| Q46 | - |  |  | SI | The Medication section is at the care provider's d... |
| Q47 | - |  |  | SI | Nutrition is an extremely important contributory f... |
| Q48 | - |  |  | SI | Guidelines |
| Q49 | - |  |  | SI | Date |
| Q50 | - |  |  | SI | Time |
| Q51 | - |  |  | SI | Score |
| Q52 | - |  |  | SI | Classification |
| Q53 | - |  |  | SI | Score |
| Q54 | - |  |  | SI | < 10 |
| Q55 | - |  |  | SI | No risk |
| Q56 | - |  |  | SI | 10+ |
| Q57 | - |  |  | SI | At risk |
| Q58 | - |  |  | SI | 15+ |
| Q59 | - |  |  | SI | High risk |
| Q5a | - |  |  | SI | Mobility |
| Q60 | - |  |  | SI | 20+ |
| Q61 | - |  |  | SI | Very high risk |
| Q62 | - |  |  | SI | < 10: No risk |
| Q63 | - |  |  | SI | 10+: At risk |
| Q64 | - |  |  | SI | 15+: High risk |
| Q65 | - |  |  | SI | 20+: Very high risk |
| Q66 | - |  |  | SI | ≤ 2 |
| Q67 | - |  |  | SI | Nutrition assessment/intervention not required |
| Q68 | - |  |  | SI | > 2 |
| Q69 | - |  |  | SI | Refer for nutrition assessment / intervention |
| Q70 | - |  |  | SI | ≤ 2: Nutrition assessment / intervention not requi... |
| Q71 | - |  |  | SI | > 2: Refer for nutrition assessment / intervention |
| Q72 | - |  |  | SI | Waterlow score |
| Q73 | - |  |  | SI | MST score |
| Q9a | - |  |  | SI | Major Surgery or Trauma |
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
| REP_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| REP_Childsub | double |  |  | NO | Childsub |
| REP_CustomExtractRep_DR | varchar |  | FK | SI | Des Ref PAC CustomExtractRep |
| REP_DateFrom | date |  |  | SI | Date From |
| REP_DateRun | date |  |  | SI | Date Run |
| REP_DateTo | date |  |  | SI | Date To |
| REP_Errors | varchar |  |  | SI | Errors |
| REP_HCA_DR | bigint |  | FK | SI | Des Ref HCA |
| REP_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| REP_RowId | varchar |  |  | NO | - |
| REP_SpecialtyExclude | varchar |  |  | SI | Specialty Exclude |
| REP_SpecialtyString | varchar |  |  | SI | Specialty String |
| REP_Status | varchar |  |  | SI | Status |
| REP_Trust_DR | bigint |  | FK | SI | Des Ref Trust |
| REP_User_DR | bigint |  | FK | SI | Des Ref User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*