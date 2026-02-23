# questionnaire.QTCRPTER

> Renal Pre-Transplant Education Record

**Schema:** questionnaire
**Columnas:** 79
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Renal Pre-Transplant Education Record

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Education provided by |
| Q04 | varchar |  |  | SI | Other educator comments |
| Q05 | varchar |  |  | SI | Education delivered |
| Q06 | varchar |  |  | SI | Other delivery |
| Q07 | varchar |  |  | SI | Education booklet provided |
| Q08 | varchar |  |  | SI | Renal Transplant Topics |
| Q09 | varchar |  |  | SI | Renal replacement therapy is lifelong |
| Q10 | varchar |  |  | SI | Functions of the kidney |
| Q11 | varchar |  |  | SI | Transplant is a renal replacement therapy option a... |
| Q12 | varchar |  |  | SI | Advantages of renal transplant |
| Q13 | varchar |  |  | SI | Transplant waiting list |
| Q14 | varchar |  |  | SI | Facts about live kidney donation |
| Q15 | varchar |  |  | SI | Staying healthy |
| Q16 | varchar |  |  | SI | Tests to expect before kidney transplant |
| Q17 | varchar |  |  | SI | Review by transplant assessment team |
| Q18 | varchar |  |  | SI | Kidney transplant surgery travel preparation |
| Q19 | varchar |  |  | SI | Patient and family education notes |
| Q20 | varchar |  |  | SI | Need to remain healthy |
| Q21 | varchar |  |  | SI | Must be adherent with treatment |
| Q22 | varchar |  |  | SI | Must always be contactable |
| Q23 | varchar |  |  | SI | Transplant waitlist patient responsibilities notes |
| Q24 | varchar |  |  | SI | Placement of the transplant kidney |
| Q25 | varchar |  |  | SI | Surgical procedure |
| Q26 | varchar |  |  | SI | Removal of Tenckhoff catheter |
| Q27 | varchar |  |  | SI | Post-operative care discussed |
| Q28 | varchar |  |  | SI | Possible complications post surgery discussed |
| Q29 | varchar |  |  | SI | Day of surgery and post-op care notes |
| Q30 | varchar |  |  | SI | Returning to home / community |
| Q31 | varchar |  |  | SI | Living a healthy lifestyle |
| Q32 | varchar |  |  | SI | Attending all medical check-ups and completing dia... |
| Q33 | varchar |  |  | SI | Immunosuppressants and importance of taking medica... |
| Q34 | varchar |  |  | SI | Risk of infection, cancer and diabetes |
| Q35 | varchar |  |  | SI | Possibility of kidney rejection |
| Q36 | varchar |  |  | SI | Kidney transplantation average life span of 10 to ... |
| Q37 | varchar |  |  | SI | Reinforce renal transplant is an alternative treat... |
| Q38 | varchar |  |  | SI | Life after kidney transplant notes |
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