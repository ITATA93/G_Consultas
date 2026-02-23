# questionnaire.QTCTCPPO

> Timeout Checklist for Procedures Outside Operating Theater

**Schema:** questionnaire
**Columnas:** 107
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Timeout Checklist for Procedures Outside Operating Theater

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Invasive procedure to be performed |
| Q02 | varchar |  |  | SI | History and physical exam completed (If the patien... |
| Q03 | varchar |  |  | SI | Informed consent obtained |
| Q04 | varchar |  |  | SI | Correct patient identity |
| Q05 | varchar |  |  | SI | Correct site marked |
| Q06 | varchar |  |  | SI | Correct side marked |
| Q07 | varchar |  |  | SI | Site |
| Q08 | varchar |  |  | SI | Correct site verified |
| Q09 | varchar |  |  | SI | Correct side verified |
| Q10 | varchar |  |  | SI | Correct equipment available  |
| Q11 | varchar |  |  | SI | Required resources available  |
| Q12 | varchar |  |  | SI | Ready to setup procedure  |
| Q13 | varchar |  |  | SI | Ready to proceed with procedure  |
| Q14 | varchar |  |  | SI | Physician performing procedure |
| Q15 | longvarbinary |  |  | SI | Physician performing procedure signature |
| Q15UDt | date |  |  | SI | Physician performing procedure signature Last Upda... |
| Q15UTm | time |  |  | SI | Physician performing procedure signature Last Upda... |
| Q16 | varchar |  |  | SI | Procedure nurse name |
| Q17 | longvarbinary |  |  | SI | Procedure nurse signature |
| Q17UDt | date |  |  | SI | Procedure nurse signature Last Updated Date |
| Q17UTm | time |  |  | SI | Procedure nurse signature Last Updated Time |
| Q18 | varchar |  |  | SI | Technician name |
| Q19 | longvarbinary |  |  | SI | Technician signature |
| Q19UDt | date |  |  | SI | Technician signature Last Updated Date |
| Q19UTm | time |  |  | SI | Technician signature Last Updated Time |
| Q20 | varchar |  |  | SI | Other |
| Q21 | longvarbinary |  |  | SI | Other signature |
| Q21UDt | date |  |  | SI | Other signature Last Updated Date |
| Q21UTm | time |  |  | SI | Other signature Last Updated Time |
| Q22 | varchar |  |  | SI | Other |
| Q23 | longvarbinary |  |  | SI | Other signature |
| Q23UDt | date |  |  | SI | Other signature Last Updated Date |
| Q23UTm | time |  |  | SI | Other signature Last Updated Time |
| Q24 | varchar |  |  | SI | Name of procedure, completion of sponge, sharp, an... |
| Q25 | varchar |  |  | SI | Specimen identified and labeled |
| Q26 | varchar |  |  | SI | Any equipment problems to be addressed |
| Q27 | varchar |  |  | SI | Implants and special equipment used were checked |
| Q28 | varchar |  |  | SI | Safety belt detached after trolley fixed and secur... |
| Q29 | varchar |  |  | SI | Guide-wire removed |
| Q30 | date |  |  | SI | Date |
| Q31 | time |  |  | SI | Time |
| Q32 | date |  |  | SI | Sign-in |
| Q33 | time |  |  | SI | Sign-in time |
| Q34 | varchar |  |  | SI | Confirmed patient identity |
| Q35 | varchar |  |  | SI | Relevant documents, images and studies are availab... |
| Q36 | date |  |  | SI | Timeout |
| Q37 | time |  |  | SI | Timeout time |
| Q38 | date |  |  | SI | Sign-out |
| Q39 | time |  |  | SI | Sign-out time |
| Q40 | varchar |  |  | SI | Procedure completed as planned? |
| Q41 | varchar |  |  | SI | Name of procedure that was recorded has been confi... |
| Q42 | varchar |  |  | SI | Completion of sponge, sharp and instrument counts ... |
| Q43 | varchar |  |  | SI | Sharps removed from the tray |
| Q44 | varchar |  |  | SI | Procedure comments |
| Q45 | date |  |  | SI | Procedure start date |
| Q46 | time |  |  | SI | Procedure start time |
| Q47 | date |  |  | SI | Procedure finish date |
| Q48 | time |  |  | SI | Procedure finish time |
| Q49 | varchar |  |  | SI | Introduction of team members |
| Q50 | varchar |  |  | SI | Essential lab results available |
| Q51 | varchar |  |  | SI | Antibiotic prophylaxis given |
| Q52 | varchar |  |  | SI | Body Site |
| Q53 | varchar |  |  | SI | Care provider 1 name |
| Q54 | varchar |  |  | SI | Care provider 2 name |
| Q55 | varchar |  |  | SI | Care provider 1 name |
| Q56 | varchar |  |  | SI | Care provider 2 name |
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