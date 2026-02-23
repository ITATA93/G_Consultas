# questionnaire.QTCAHPAUPAC

> Pediatric Audiology Case History

**Schema:** questionnaire
**Columnas:** 79
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Pediatric Audiology Case History

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Are the parents related? |
| Q02 | varchar |  |  | SI | Primary reason for referral |
| Q03 | varchar |  |  | SI | How long was the pregnancy? |
| Q04 | numeric |  |  | SI | How much did the child weigh at birth? (gm) |
| Q05 | varchar |  |  | SI | Did the mother take any of the following medicatio... |
| Q06 | varchar |  |  | SI | Other medications |
| Q07 | varchar |  |  | SI | Were there any of the following complications thro... |
| Q08 | varchar |  |  | SI | Other delivery complications |
| Q09 | varchar |  |  | SI | Did the child suffer from or experienced any compl... |
| Q10 | varchar |  |  | SI | Other after delivery complications |
| Q11 | varchar |  |  | SI | Child's Developmental Milestones |
| Q12 | varchar |  |  | SI | First held his/her head up alone |
| Q13 | varchar |  |  | SI | Sat alone unsupported |
| Q14 | varchar |  |  | SI | Babbled |
| Q15 | varchar |  |  | SI | Crawled |
| Q16 | varchar |  |  | SI | Walked unattended |
| Q17 | varchar |  |  | SI | Said his/her first word |
| Q18 | varchar |  |  | SI | In comparison to his/her peers and siblings, did y... |
| Q19 | varchar |  |  | SI | Was the child hospitalized before? |
| Q20 | varchar |  |  | SI | When Was the Child Hospitalized?  |
| Q21 | varchar |  |  | SI | For what reason was the child hospitalized? |
| Q22 | varchar |  |  | SI | Surgery (specify) |
| Q23 | varchar |  |  | SI | Others (specify) |
| Q24 | varchar |  |  | SI | Does the child take any of the following medicatio... |
| Q25 | varchar |  |  | SI | Does the child have any of the following allergies... |
| Q26 | varchar |  |  | SI | Does the child take any of the following medicatio... |
| Q27 | varchar |  |  | SI | Does the child have recurrent ear infections? |
| Q28 | varchar |  |  | SI | Does the child complain of ear pain / discharge? |
| Q29 | varchar |  |  | SI | Does the child have any of the following health co... |
| Q30 | varchar |  |  | SI | Infections (specify) |
| Q31 | varchar |  |  | SI | Note: Please reveiw all medication history in the ... |
| Q32 | varchar |  |  | SI | Does the child respond to loud noise? |
| Q33 | varchar |  |  | SI | Does the child respond to his/her own name when ca... |
| Q34 | varchar |  |  | SI | How does the child respond to questions/ direction... |
| Q35 | varchar |  |  | SI | How does the child interact with other peers? |
| Q36 | varchar |  |  | SI | Did the child have a hearing screening before?  |
| Q37 | varchar |  |  | SI | Is there a family history of hearing loss and/or i... |
| Q38 | varchar |  |  | SI | Additional Comments |
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