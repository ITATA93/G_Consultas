# SQLUser.IN_Manuf_Request

**Schema:** SQLUser
**Columnas:** 106
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Incidentes**. Registro de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INMRQ_RowId | bigint | PK |  | NO | - |
| INMRQ_Approved | varchar |  |  | NO | Approved |
| INMRQ_CTCP_DR | varchar |  | FK | NO | Des REf to CTCP (req.Doctor) |
| INMRQ_Date | date |  |  | NO | Date of Request |
| INMRQ_Date_Approved | date |  |  | SI | Date of Approval |
| INMRQ_Date_Created | date |  |  | NO | Date Created |
| INMRQ_INCI_DR | bigint |  | FK | SI | Des Ref to INCI |
| INMRQ_Ingredients | varchar |  |  | SI | Ingredients |
| INMRQ_No | varchar |  |  | NO | Man. Request No |
| INMRQ_Reason | varchar |  |  | SI | Reason for Request |
| INMRQ_Remarks | varchar |  |  | SI | Remarks |
| INMRQ_StockCode | varchar |  |  | SI | Stock Code |
| INMRQ_Time_Created | time |  |  | NO | Time Created |
| INMRQ_User_DR | bigint |  | FK | SI | Des Ref to SSU |
| Q01 | - |  |  | SI | View |
| Q02 | - |  |  | SI | Blindness |
| Q02N | - |  |  | SI | Note |
| Q02ObsDR | - |  |  | SI | Blindness DR |
| Q04 | - |  |  | SI | Blindness partial |
| Q04N | - |  |  | SI | Note |
| Q04ObsDR | - |  |  | SI | Blindness partial DR |
| Q06 | - |  |  | SI | Ocular prothesis |
| Q06N | - |  |  | SI | Note |
| Q06ObsDR | - |  |  | SI | Ocular prothesis DR |
| Q08 | - |  |  | SI | Glasses |
| Q08N | - |  |  | SI | Note |
| Q08ObsDR | - |  |  | SI | Glasses DR |
| Q10 | - |  |  | SI | Contact Lenses |
| Q10N | - |  |  | SI | Note |
| Q10ObsDR | - |  |  | SI | Contact Lenses DR |
| Q12 | - |  |  | SI | Ocular bandage |
| Q12N | - |  |  | SI | Note |
| Q12ObsDR | - |  |  | SI | Ocular bandage DR |
| Q14 | - |  |  | SI | Hearing |
| Q15 | - |  |  | SI | Deafness |
| Q15N | - |  |  | SI | Note |
| Q15ObsDR | - |  |  | SI | Deafness DR |
| Q17 | - |  |  | SI | Hearing loss |
| Q17N | - |  |  | SI | Note |
| Q17ObsDR | - |  |  | SI | Hearing loss DR |
| Q19 | - |  |  | SI | Hearing aids |
| Q19N | - |  |  | SI | Note |
| Q19ObsDR | - |  |  | SI | Hearing aids DR |
| Q21 | - |  |  | SI | Language |
| Q22 | - |  |  | SI | Aphasia |
| Q22N | - |  |  | SI | Note |
| Q22ObsDR | - |  |  | SI | Aphasia DR |
| Q24 | - |  |  | SI | Dysarthria |
| Q24N | - |  |  | SI | Note |
| Q24ObsDR | - |  |  | SI | Dysarthria DR |
| Q26 | - |  |  | SI | Stuttering |
| Q26N | - |  |  | SI | Note |
| Q26ObsDR | - |  |  | SI | Stuttering DR |
| Q27 | - |  |  | SI | Inability to understand |
| Q27N | - |  |  | SI | Note |
| Q27ObsDR | - |  |  | SI | Inability to understand DR |
| Q29 | - |  |  | SI | Failure of communication |
| Q29N | - |  |  | SI | Note |
| Q29ObsDR | - |  |  | SI | Failure of communication DR |
| Q31 | - |  |  | SI | State of mind |
| Q32 | - |  |  | SI | State of mind |
| Q32N | - |  |  | SI | Note |
| Q32ObsDR | - |  |  | SI | State of mind DR |
| Q34 | - |  |  | SI | Oriented |
| Q34N | - |  |  | SI | Note |
| Q34ObsDR | - |  |  | SI | Oriented DR |
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