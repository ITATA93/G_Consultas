# SQLUser.PAC_ComplaintStatus

**Schema:** SQLUser
**Columnas:** 91
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CMS_RowId | bigint | PK |  | NO | - |
| CMS_Code | varchar |  |  | NO | Code |
| CMS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CMS_CreatedDate | date |  |  | SI | Created Date |
| CMS_CreatedTime | time |  |  | SI | Created Time |
| CMS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CMS_DateFrom | date |  |  | SI | Date From |
| CMS_DateTo | date |  |  | SI | Date To |
| CMS_Desc | varchar |  |  | NO | Description |
| CMS_Owner | varchar |  |  | SI | Owner |
| CMS_UpdatedDate | date |  |  | SI | Updated Date |
| CMS_UpdatedTime | time |  |  | SI | Updated Time |
| CMS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Now we want you to remember what your friend or re... |
| Q04 | - |  |  | SI | 10 years ago was in year |
| Q05 | - |  |  | SI | Below are situations where this person has to use ... |
| Q06 | - |  |  | SI | Note the importance of comparing his/her present p... |
| Q07 | - |  |  | SI | So if 10 years ago this person always forgot where... |
| Q08 | - |  |  | SI | Please indicate the changes you have observed. |
| Q09 | - |  |  | SI | Completed by |
| Q10 | - |  |  | SI | Relationship to patient |
| Q11 | - |  |  | SI | Compared with 10 years ago how is this person at: |
| Q12 | - |  |  | SI | Remembering things about family and friends e.g. o... |
| Q13 | - |  |  | SI | Remembering things that have happened recently |
| Q14 | - |  |  | SI | Recalling conversations a few days later |
| Q15 | - |  |  | SI | Remembering his/her address and telephone number |
| Q16 | - |  |  | SI | Remembering what day and month it is |
| Q17 | - |  |  | SI | Remembering where things are usually kept |
| Q18 | - |  |  | SI | Remembering where to find things which have been p... |
| Q19 | - |  |  | SI | Knowing how to work familiar machines around the h... |
| Q20 | - |  |  | SI | Learning to use a new gadget or machine around the... |
| Q21 | - |  |  | SI | Learning new things in general |
| Q22 | - |  |  | SI | Following a story in a book or on TV |
| Q23 | - |  |  | SI | Making decisions on everyday matters |
| Q24 | - |  |  | SI | Handling money for shopping |
| Q25 | - |  |  | SI | Handling financial matters e.g. the pension, deali... |
| Q26 | - |  |  | SI | Handling other everyday arithmetic problems e.g. k... |
| Q27 | - |  |  | SI | Using his/her intelligence to understand what's go... |
| Q28 | - |  |  | SI | Notes |
| Q29 | - |  |  | SI | Score |
| Q30 | - |  |  | SI | The score should be assessed as a continuum betwee... |
| Q31 | - |  |  | SI | between intermediate states being indicated by ave... |
| Q32 | - |  |  | SI | Where the Short IQCODE is used for screening an av... |
| Q33 | - |  |  | SI | Different thresholds may apply if the patient is n... |
| Q34 | - |  |  | SI | Jorm, A. F. and Korten, A. E. (1988). Assessment o... |
| Q35 | - |  |  | SI | https://rsph.anu.edu.au/research/tools-resources/i... |
| Q36 | - |  |  | SI | Scores of ≤ 3.31 indicate that dementia is unlikel... |
| Q37 | - |  |  | SI | Other |
| Q38 | - |  |  | SI | Relationship to patient |
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