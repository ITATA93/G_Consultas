# questionnaire.QTCIQCODE

> Short Form of the Informant Questionnaire on Cognitive Decline in the Elderly (Short IQCODE)

**Schema:** questionnaire
**Columnas:** 79
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Short Form of the Informant Questionnaire on Cognitive Decline in the Elderly (Short IQCODE)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Now we want you to remember what your friend or re... |
| Q04 | numeric |  |  | SI | 10 years ago was in year |
| Q05 | varchar |  |  | SI | Below are situations where this person has to use ... |
| Q06 | varchar |  |  | SI | Note the importance of comparing his/her present p... |
| Q07 | varchar |  |  | SI | So if 10 years ago this person always forgot where... |
| Q08 | varchar |  |  | SI | Please indicate the changes you have observed. |
| Q09 | varchar |  |  | SI | Completed by |
| Q10 | varchar |  |  | SI | Relationship to patient |
| Q11 | varchar |  |  | SI | Compared with 10 years ago how is this person at: |
| Q12 | varchar |  |  | SI | Remembering things about family and friends e.g. o... |
| Q13 | varchar |  |  | SI | Remembering things that have happened recently |
| Q14 | varchar |  |  | SI | Recalling conversations a few days later |
| Q15 | varchar |  |  | SI | Remembering his/her address and telephone number |
| Q16 | varchar |  |  | SI | Remembering what day and month it is |
| Q17 | varchar |  |  | SI | Remembering where things are usually kept |
| Q18 | varchar |  |  | SI | Remembering where to find things which have been p... |
| Q19 | varchar |  |  | SI | Knowing how to work familiar machines around the h... |
| Q20 | varchar |  |  | SI | Learning to use a new gadget or machine around the... |
| Q21 | varchar |  |  | SI | Learning new things in general |
| Q22 | varchar |  |  | SI | Following a story in a book or on TV |
| Q23 | varchar |  |  | SI | Making decisions on everyday matters |
| Q24 | varchar |  |  | SI | Handling money for shopping |
| Q25 | varchar |  |  | SI | Handling financial matters e.g. the pension, deali... |
| Q26 | varchar |  |  | SI | Handling other everyday arithmetic problems e.g. k... |
| Q27 | varchar |  |  | SI | Using his/her intelligence to understand what's go... |
| Q28 | varchar |  |  | SI | Notes |
| Q29 | varchar |  |  | SI | Score |
| Q30 | varchar |  |  | SI | The score should be assessed as a continuum betwee... |
| Q31 | varchar |  |  | SI | between intermediate states being indicated by ave... |
| Q32 | varchar |  |  | SI | Where the Short IQCODE is used for screening an av... |
| Q33 | varchar |  |  | SI | Different thresholds may apply if the patient is n... |
| Q34 | varchar |  |  | SI | Jorm, A. F. and Korten, A. E. (1988). Assessment o... |
| Q35 | varchar |  |  | SI | https://rsph.anu.edu.au/research/tools-resources/i... |
| Q36 | varchar |  |  | SI | Scores of ≤ 3.31 indicate that dementia is unlikel... |
| Q37 | varchar |  |  | SI | Other |
| Q38 | varchar |  |  | SI | Relationship to patient |
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