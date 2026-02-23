# questionnaire.QTCVAPA

> Visual Acuity Physician Assessment

**Schema:** questionnaire
**Columnas:** 124
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Visual Acuity Physician Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Visual Acuity (VA) |
| Q04 | varchar |  |  | SI | Right eye |
| Q05 | varchar |  |  | SI | Left eye |
| Q06 | varchar |  |  | SI | Visual Acuity |
| Q07 | varchar |  |  | SI | Visual acuity notes |
| Q08 | varchar |  |  | SI | Visual acuity correction |
| Q09 | varchar |  |  | SI | Visual acuity, right eye (imperial) |
| Q09ObsDR | varchar |  | FK | SI | Visual acuity, right eye (imperial) DR |
| Q10 | varchar |  |  | SI | Visual acuity, right eye (metric) |
| Q10ObsDR | varchar |  | FK | SI | Visual acuity, right eye (metric) DR |
| Q11 | varchar |  |  | SI | Visual acuity, right eye (decimal) |
| Q11ObsDR | varchar |  | FK | SI | Visual acuity, right eye (decimal) DR |
| Q12 | varchar |  |  | SI | Visual acuity, right eye (logMAR) |
| Q12ObsDR | varchar |  | FK | SI | Visual acuity, right eye (logMAR) DR |
| Q13 | varchar |  |  | SI | Visual acuity notes, right eye |
| Q14 | varchar |  |  | SI | Correction, right eye |
| Q15 | varchar |  |  | SI | Visual acuity, left eye (imperial) |
| Q15ObsDR | varchar |  | FK | SI | Visual acuity, left eye (imperial) DR |
| Q16 | varchar |  |  | SI | Visual acuity, left eye (metric) |
| Q16ObsDR | varchar |  | FK | SI | Visual acuity, left eye (metric) DR |
| Q17 | varchar |  |  | SI | Visual acuity, left eye (decimal) |
| Q17ObsDR | varchar |  | FK | SI | Visual acuity, left eye (decimal) DR |
| Q18 | varchar |  |  | SI | Visual acuity, left eye (logMAR) |
| Q18ObsDR | varchar |  | FK | SI | Visual acuity, left eye (logMAR) DR |
| Q19 | varchar |  |  | SI | Visual acuity notes, left eye |
| Q20 | varchar |  |  | SI | Correction, left eye |
| Q21 | varchar |  |  | SI | Visual acuity notes |
| Q22 | varchar |  |  | SI | Visual acuity, both eyes (imperial) |
| Q22ObsDR | varchar |  | FK | SI | Visual acuity, both eyes (imperial) DR |
| Q23 | varchar |  |  | SI | Visual acuity, both eyes (metric) |
| Q23ObsDR | varchar |  | FK | SI | Visual acuity, both eyes (metric) DR |
| Q24 | varchar |  |  | SI | Visual acuity, both eyes (decimal) |
| Q24ObsDR | varchar |  | FK | SI | Visual acuity, both eyes (decimal) DR |
| Q25 | varchar |  |  | SI | Visual acuity, both eyes (logMAR) |
| Q25ObsDR | varchar |  | FK | SI | Visual acuity, both eyes (logMAR) DR |
| Q26 | varchar |  |  | SI | Visual acuity notes, both eyes |
| Q27 | varchar |  |  | SI | Visual acuity correction, both eyes |
| Q28 | numeric |  |  | SI | Distance between the subject and vision chart |
| Q29 | varchar |  |  | SI | Unit |
| Q30 | varchar |  |  | SI | Method |
| Q31 | varchar |  |  | SI | Other method notes |
| Q32 | varchar |  |  | SI | Subjective change (subject's perception of visual ... |
| Q33 | varchar |  |  | SI | Visual acuity both eyes |
| Q34 | varchar |  |  | SI | Right eye |
| Q35 | varchar |  |  | SI | Left eye |
| Q36 | varchar |  |  | SI | Measurement |
| Q37 | varchar |  |  | SI | Add dioptres |
| Q38 | varchar |  |  | SI | Working distance (cm) |
| Q39 | varchar |  |  | SI | Measurement, right eye |
| Q40 | varchar |  |  | SI | Add dioptres, right eye |
| Q41 | numeric |  |  | SI | Working distance (cm), right eye |
| Q42 | varchar |  |  | SI | Measurement, left eye |
| Q43 | varchar |  |  | SI | Add dioptres, left eye |
| Q44 | numeric |  |  | SI | Working distance (cm), left eye |
| Q45 | varchar |  |  | SI | Near vision notes |
| Q46 | varchar |  |  | SI | Measurement, both eyes |
| Q47 | varchar |  |  | SI | Add dioptres, both eyes |
| Q48 | numeric |  |  | SI | Working distance (cm), both eyes |
| Q49 | varchar |  |  | SI | Near vision notes, both eyes |
| Q50 | varchar |  |  | SI | Right eye |
| Q51 | varchar |  |  | SI | Right eye |
| Q52 | varchar |  |  | SI | Right eye |
| Q53 | varchar |  |  | SI | Right eye |
| Q54 | varchar |  |  | SI | Right eye |
| Q55 | varchar |  |  | SI | Right eye |
| Q56 | varchar |  |  | SI | Right eye |
| Q57 | varchar |  |  | SI | Right eye |
| Q58 | varchar |  |  | SI | Right eye |
| Q59 | varchar |  |  | SI | Left eye |
| Q60 | varchar |  |  | SI | Left eye |
| Q61 | varchar |  |  | SI | Left eye |
| Q62 | varchar |  |  | SI | Left eye |
| Q63 | varchar |  |  | SI | Left eye |
| Q64 | varchar |  |  | SI | Left eye |
| Q65 | varchar |  |  | SI | Left eye |
| Q66 | varchar |  |  | SI | Left eye |
| Q67 | varchar |  |  | SI | Left eye |
| Q68 | varchar |  |  | SI | Visual acuity (imperial) |
| Q69 | varchar |  |  | SI | Visual acuity (metric) |
| Q70 | varchar |  |  | SI | Visual acuity (decimal) |
| Q71 | varchar |  |  | SI | Visual acuity (logMAR) |
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