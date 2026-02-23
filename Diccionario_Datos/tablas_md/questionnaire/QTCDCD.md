# questionnaire.QTCDCD

> Dialysis Deferment / Cancellation

**Schema:** questionnaire
**Columnas:** 108
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Dialysis Deferment / Cancellation

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Deferment or cancellation |
| Q04 | varchar |  |  | SI | Reason |
| Q05 | varchar |  |  | SI | Dummy1 |
| Q06 | varchar |  |  | SI | Vital Signs Observations |
| Q07 | varchar |  |  | SI | Systolic |
| Q07ObsDR | varchar |  | FK | SI | Systolic DR |
| Q08 | varchar |  |  | SI | Diastolic |
| Q08ObsDR | varchar |  | FK | SI | Diastolic DR |
| Q09 | varchar |  |  | SI | Heart Rate |
| Q09ObsDR | varchar |  | FK | SI | Heart Rate DR |
| Q10 | varchar |  |  | SI | Respirations |
| Q10ObsDR | varchar |  | FK | SI | Respirations DR |
| Q11 | varchar |  |  | SI | Oxygen Saturation |
| Q11ObsDR | varchar |  | FK | SI | Oxygen Saturation DR |
| Q12 | varchar |  |  | SI | Temperature |
| Q12ObsDR | varchar |  | FK | SI | Temperature DR |
| Q13 | varchar |  |  | SI | Stat Lab / Point of Care Results |
| Q14 | varchar |  |  | SI | Serum Potassium |
| Q14ObsDR | varchar |  | FK | SI | Serum Potassium DR |
| Q15 | varchar |  |  | SI | Dummy2 |
| Q16 | varchar |  |  | SI | Fluid Status Assessment |
| Q17 | varchar |  |  | SI | Dyspnoea |
| Q17ObsDR | varchar |  | FK | SI | Dyspnoea DR |
| Q18 | varchar |  |  | SI | Oedema |
| Q18ObsDR | varchar |  | FK | SI | Oedema DR |
| Q19 | varchar |  |  | SI | Urine output |
| Q20 | varchar |  |  | SI | Urine Output (mL) |
| Q20ObsDR | varchar |  | FK | SI | Urine Output (mL) DR |
| Q21 | varchar |  |  | SI | Chest pain |
| Q22 | varchar |  |  | SI | Chest pain details |
| Q23 | varchar |  |  | SI | Vomiting |
| Q24 | varchar |  |  | SI | Diarrhoea |
| Q25 | varchar |  |  | SI | Appetite |
| Q26 | varchar |  |  | SI | Current weight |
| Q26ObsDR | varchar |  | FK | SI | Current weight DR |
| Q27 | varchar |  |  | SI | Dry Weight Target (Renal Replacement Therapy) |
| Q27ObsDR | varchar |  | FK | SI | Dry Weight Target (Renal Replacement Therapy) DR |
| Q28 | varchar |  |  | SI | Greater than 8% variance weight gain |
| Q29 | varchar |  |  | SI | Clinical assessment notes |
| Q30 | varchar |  |  | SI | Missed Session Review |
| Q31 | numeric |  |  | SI | Total number of dialysis sessions missed over last... |
| Q32 | varchar |  |  | SI | Dates missed in last 7 days |
| Q33 | varchar |  |  | SI | Review previous missed dialysis session reasons |
| Q34 | varchar |  |  | SI | Missed session review notes |
| Q35 | varchar |  |  | SI | Treatment Plan |
| Q36 | varchar |  |  | SI | Doctor in attendance |
| Q37 | varchar |  |  | SI | Attending doctor |
| Q38 | varchar |  |  | SI | Plan |
| Q39 | longvarbinary |  |  | SI | Signature of doctor |
| Q39UDt | date |  |  | SI | Signature of doctor Last Updated Date |
| Q39UTm | time |  |  | SI | Signature of doctor Last Updated Time |
| Q40 | varchar |  |  | SI | Name of doctor contacted |
| Q41 | varchar |  |  | SI | Verbal plan |
| Q42 | varchar |  |  | SI | Name of care provider taking verbal plan and inter... |
| Q43 | longvarbinary |  |  | SI | Signature of care provider |
| Q43UDt | date |  |  | SI | Signature of care provider Last Updated Date |
| Q43UTm | time |  |  | SI | Signature of care provider Last Updated Time |
| Q44 | varchar |  |  | SI | Clinical Nurse Manager / Haemodialysis Coordinator... |
| Q45 | varchar |  |  | SI | Reason CNM / HD Coordinator not aware |
| Q46 | varchar |  |  | SI | Explanation of plan and interventions provided to ... |
| Q47 | varchar |  |  | SI | Interpreter details, if applicable |
| Q48 | varchar |  |  | SI | Additional Requirements |
| Q49 | varchar |  |  | SI | Dummy3 |
| Q50 | varchar |  |  | SI | Dummy4 |
| Q51 | varchar |  |  | SI | Dummy5 |
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