# SQLUser.OE_OrdActivityModif

**Schema:** SQLUser
**Columnas:** 82
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Órdenes Médicas**. Solicitudes de exámenes, procedimientos, etc.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ACTMOD_ParRef | varchar | PK |  | NO | OE_OrdItem Parent Reference |
| ACTMOD_ActivityModif_DR | bigint |  | FK | SI | Des Ref ActivityModif |
| ACTMOD_Childsub | double |  |  | NO | Childsub |
| ACTMOD_RowId | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | Are the parents related? |
| Q02 | - |  |  | SI | Primary reason for referral |
| Q03 | - |  |  | SI | How long was the pregnancy? |
| Q04 | - |  |  | SI | How much did the child weigh at birth? (gm) |
| Q05 | - |  |  | SI | Did the mother take any of the following medicatio... |
| Q06 | - |  |  | SI | Other medications |
| Q07 | - |  |  | SI | Were there any of the following complications thro... |
| Q08 | - |  |  | SI | Other delivery complications |
| Q09 | - |  |  | SI | Did the child suffer from or experienced any compl... |
| Q10 | - |  |  | SI | Other after delivery complications |
| Q11 | - |  |  | SI | Child's Developmental Milestones |
| Q12 | - |  |  | SI | First held his/her head up alone |
| Q13 | - |  |  | SI | Sat alone unsupported |
| Q14 | - |  |  | SI | Babbled |
| Q15 | - |  |  | SI | Crawled |
| Q16 | - |  |  | SI | Walked unattended |
| Q17 | - |  |  | SI | Said his/her first word |
| Q18 | - |  |  | SI | In comparison to his/her peers and siblings, did y... |
| Q19 | - |  |  | SI | Was the child hospitalized before? |
| Q20 | - |  |  | SI | When Was the Child Hospitalized? |
| Q21 | - |  |  | SI | For what reason was the child hospitalized? |
| Q22 | - |  |  | SI | Surgery (specify) |
| Q23 | - |  |  | SI | Others (specify) |
| Q24 | - |  |  | SI | Does the child take any of the following medicatio... |
| Q25 | - |  |  | SI | Does the child have any of the following allergies... |
| Q26 | - |  |  | SI | Does the child take any of the following medicatio... |
| Q27 | - |  |  | SI | Does the child have recurrent ear infections? |
| Q28 | - |  |  | SI | Does the child complain of ear pain / discharge? |
| Q29 | - |  |  | SI | Does the child have any of the following health co... |
| Q30 | - |  |  | SI | Infections (specify) |
| Q31 | - |  |  | SI | Note: Please reveiw all medication history in the ... |
| Q32 | - |  |  | SI | Does the child respond to loud noise? |
| Q33 | - |  |  | SI | Does the child respond to his/her own name when ca... |
| Q34 | - |  |  | SI | How does the child respond to questions/ direction... |
| Q35 | - |  |  | SI | How does the child interact with other peers? |
| Q36 | - |  |  | SI | Did the child have a hearing screening before? |
| Q37 | - |  |  | SI | Is there a family history of hearing loss and/or i... |
| Q38 | - |  |  | SI | Additional Comments |
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