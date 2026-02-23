# questionnaire.QTCPDPHEBPR

> Post Dural Puncture Headache and Epidural Blood Patch Record

**Schema:** questionnaire
**Columnas:** 104
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Post Dural Puncture Headache and Epidural Blood Patch Record

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Post dural puncture headache can be diagnosed with... |
| Q04 | varchar |  |  | SI | Please refer to online help for list of possible d... |
| Q05 | varchar |  |  | SI | •&nbsp;Tension headache |
| Q06 | varchar |  |  | SI | •&nbsp;Migraine |
| Q07 | varchar |  |  | SI | •&nbsp;Sinus headache |
| Q08 | varchar |  |  | SI | •&nbsp;Pneumocephalus |
| Q09 | varchar |  |  | SI | •&nbsp;Drug induced or withdrawal |
| Q10 | varchar |  |  | SI | •&nbsp;Pre-eclampsia/ eclampsia |
| Q11 | varchar |  |  | SI | •&nbsp;Meningitis |
| Q12 | varchar |  |  | SI | •&nbsp;Subarachnoid haemorrhage |
| Q13 | varchar |  |  | SI | •&nbsp;Subdural haematoma |
| Q14 | varchar |  |  | SI | •&nbsp;Pituitary apoplexy |
| Q15 | varchar |  |  | SI | •&nbsp;Neoplasm |
| Q16 | varchar |  |  | SI | •&nbsp;Posterior leukoencephaly |
| Q17 | varchar |  |  | SI | •&nbsp;Stroke |
| Q18 | varchar |  |  | SI | Post dural puncture headache diagnosis confirmed |
| Q19 | varchar |  |  | SI | Time since onset of headache |
| Q20 | varchar |  |  | SI | Probable cause of dural puncture |
| Q21 | varchar |  |  | SI | Specify other probable cause |
| Q22 | varchar |  |  | SI | Obstetric related |
| Q23 | varchar |  |  | SI | Post dural puncture headache severity |
| Q24 | varchar |  |  | SI | Diagnosis, cause and symptom review notes |
| Q25 | varchar |  |  | SI | Please confirm that the diagnosis has been added t... |
| Q26 | date |  |  | SI | Injection date |
| Q27 | time |  |  | SI | Time |
| Q28 | varchar |  |  | SI | Indication for epidural blood patch |
| Q29 | varchar |  |  | SI | Specify other indications |
| Q30 | varchar |  |  | SI | Risks explained |
| Q31 | varchar |  |  | SI | Specify other risks explained |
| Q32 | varchar |  |  | SI | Patient positioning during procedure |
| Q33 | varchar |  |  | SI | Ultrasound used |
| Q34 | varchar |  |  | SI | Standard aseptic procedure |
| Q35 | varchar |  |  | SI | Specify other aseptic procedures |
| Q36 | varchar |  |  | SI | Needle type |
| Q37 | varchar |  |  | SI | Specify other needle type |
| Q38 | varchar |  |  | SI | Needle gauge |
| Q39 | varchar |  |  | SI | Other needle gauge |
| Q40 | varchar |  |  | SI | Loss of resistance (LOR) |
| Q41 | varchar |  |  | SI | Injection level |
| Q42 | varchar |  |  | SI | Specify other injection levels |
| Q43 | numeric |  |  | SI | Number of passes |
| Q44 | numeric |  |  | SI | Depth of space (cm) |
| Q45 | numeric |  |  | SI | Blood volume injected (ml) |
| Q46 | varchar |  |  | SI | Issues on injection |
| Q47 | varchar |  |  | SI | EBP notes |
| Q48 | varchar |  |  | SI | Care provider 1 |
| Q49 | varchar |  |  | SI | Care provider 2 |
| Q50 | varchar |  |  | SI | Standard aseptic procedure |
| Q51 | varchar |  |  | SI | Specify other precautions |
| Q52 | varchar |  |  | SI | Blood collected from |
| Q53 | varchar |  |  | SI | Blood collection notes |
| Q54 | varchar |  |  | SI | Care provider 1 |
| Q55 | varchar |  |  | SI | Care provider 2 |
| Q56 | varchar |  |  | SI | Recommended post procedure destination |
| Q57 | varchar |  |  | SI | Alternative destination |
| Q58 | varchar |  |  | SI | Post procedure checklist |
| Q59 | varchar |  |  | SI | Other additional post procedure needs |
| Q60 | varchar |  |  | SI | Symptom resolution |
| Q61 | varchar |  |  | SI | Estimated date of discharge recorded |
| Q62 | varchar |  |  | SI | Post procedure care and planned discharged date co... |
| Q63 | varchar |  |  | SI | Please refer to online help for follow-up guidance |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*