# SQLUser.ORC_Equipment

**Schema:** SQLUser
**Columnas:** 95
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EQ_RowId | bigint | PK |  | NO | - |
| EQ_ARCIM_DR | varchar |  | FK | SI | Des Ref ARCIM |
| EQ_Angiography | varchar |  |  | SI | Angiography |
| EQ_BedAttachment | varchar |  |  | SI | Bed Attachment |
| EQ_Code | varchar |  |  | NO | Code |
| EQ_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| EQ_CreatedDate | date |  |  | SI | Created Date |
| EQ_CreatedTime | time |  |  | SI | Created Time |
| EQ_CreatedUser_DR | bigint |  | FK | SI | Created User |
| EQ_DateFrom | date |  |  | SI | DateFrom |
| EQ_DateTo | date |  |  | SI | DateTo |
| EQ_Desc | varchar |  |  | NO | Description |
| EQ_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| EQ_Location_DR | bigint |  | FK | SI | Des Ref Location |
| EQ_Number | double |  |  | SI | Number |
| EQ_OperatingTable | varchar |  |  | SI | Operating Table |
| EQ_Owner | varchar |  |  | SI | Owner |
| EQ_PositionalAid | varchar |  |  | SI | Positional Aid |
| EQ_Resource_DR | bigint |  | FK | SI | Des Ref Resource |
| EQ_Sigmoidoscopy | varchar |  |  | SI | Sigmoidoscopy |
| EQ_TurnAroundTimeMins | double |  |  | SI | TurnAroundTimeMins |
| EQ_UpdatedDate | date |  |  | SI | Updated Date |
| EQ_UpdatedTime | time |  |  | SI | Updated Time |
| EQ_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Characteristics of dizziness |
| Q02 | - |  |  | SI | Note |
| Q03 | - |  |  | SI | Tendency to fall |
| Q04 | - |  |  | SI | Loss of balance when walking and veering to which ... |
| Q05 | - |  |  | SI | Onset & Course |
| Q06 | - |  |  | SI | Type of vertigo |
| Q07 | - |  |  | SI | Note |
| Q08 | - |  |  | SI | Dizziness between episodes |
| Q09 | - |  |  | SI | Can anticipate the attack |
| Q10 | - |  |  | SI | First dizzy episode |
| Q11 | - |  |  | SI | Most recent episode |
| Q12 | - |  |  | SI | Duration of each episode (sec,min,hr,day) |
| Q13 | - |  |  | SI | Frequency of episodes |
| Q14 | - |  |  | SI | Occupation |
| Q15 | - |  |  | SI | Exacerbating Factors |
| Q15A | - |  |  | SI | Alleviation Factors |
| Q16 | - |  |  | SI | Note |
| Q17 | - |  |  | SI | Relation between dizziness and stress or anxiety? |
| Q18 | - |  |  | SI | What causes an episode? |
| Q19 | - |  |  | SI | What makes the dizziness better? |
| Q20 | - |  |  | SI | Associated symptoms |
| Q21 | - |  |  | SI | Past / present medical history |
| Q22 | - |  |  | SI | Note |
| Q23 | - |  |  | SI | Note |
| Q24 | - |  |  | SI | Previous treatment for dizziness |
| Q25 | - |  |  | SI | Characteristics of Dizziness |
| Q26 | - |  |  | SI | Onset & Course |
| Q27 | - |  |  | SI | Personal & Social |
| Q28 | - |  |  | SI | Exacerbating & Remitting Factors |
| Q29 | - |  |  | SI | Associated Symptoms |
| Q30 | - |  |  | SI | Present / Past Medical History |
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