# SQLUser.OE_HL7Messages

**Schema:** SQLUser
**Columnas:** 85
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HL7_RowId | bigint | PK |  | NO | - |
| HL7_Acknowledged | varchar |  |  | SI | Acknowledged |
| HL7_ConnectedToEnsemble | varchar |  |  | SI | ConnectedToEnsemble |
| HL7_DateAcknow | date |  |  | SI | Date Acknowledged |
| HL7_DateReceived | date |  |  | SI | Date Received |
| HL7_ExtRequestNo | varchar |  |  | SI | External Request No |
| HL7_File | varchar |  |  | SI | File |
| HL7_FillerNumber | varchar |  |  | SI | Filler Number |
| HL7_KeyValue1 | varchar |  |  | SI | Key Value1 |
| HL7_KeyValue2 | varchar |  |  | SI | Key Value2 |
| HL7_KeyValue3 | varchar |  |  | SI | Key Value3 |
| HL7_LinkID | varchar |  |  | NO | Link ID |
| HL7_MessageType | varchar |  |  | SI | Event Message Type |
| HL7_PatDOB | date |  |  | SI | Patient DOB |
| HL7_PatName | varchar |  |  | SI | Patient Name |
| HL7_ReasonForFailure | varchar |  |  | SI | Reason For Failure |
| HL7_Record | varchar |  |  | SI | Record |
| HL7_RegNo | varchar |  |  | SI | Reg No |
| HL7_RejectionType | varchar |  |  | SI | Rejection Type |
| HL7_Sex | varchar |  |  | SI | Sex |
| HL7_TestCode | varchar |  |  | SI | Test Code |
| HL7_TimeAcknow | time |  |  | SI | Time Acknowledged |
| HL7_TimeReceived | time |  |  | SI | Time Received |
| HL7_Trace_DR | varchar |  | FK | SI | Des Ref to SS_HL7Trace |
| HL7_UploadNo | double |  |  | SI | Upload No |
| HL7_User_DR | bigint |  | FK | SI | Des Ref User |
| HL7_Version | varchar |  |  | SI | Version |
| Q01 | - |  |  | SI | Ability to Use Telephone |
| Q02 | - |  |  | SI | Shopping |
| Q03 | - |  |  | SI | Food Preparation |
| Q04 | - |  |  | SI | Housekeeping |
| Q05 | - |  |  | SI | Laundry |
| Q06 | - |  |  | SI | Mode of Transportation |
| Q07 | - |  |  | SI | Responsibility for Own Medications |
| Q08 | - |  |  | SI | Ability to Handle Finances |
| Q09 | - |  |  | SI | Score Ranges from 0 to 8 |
| Q10 | - |  |  | SI | 0 = Low Function (Dependent) |
| Q11 | - |  |  | SI | 8 = High Function (Independent) |
| Q12 | - |  |  | SI | Score Ranges from 0 to 5 for Men (*) |
| Q13 | - |  |  | SI | 0 = Low Function (Dependent) |
| Q14 | - |  |  | SI | 5 = High Function (Independent) |
| Q15 | - |  |  | SI | (*)There are eight domains of function measured wi... |
| Q16 | - |  |  | SI | for men, the areas of food preparation, housekeepi... |
| Q17 | - |  |  | SI | A summary score ranges from 0 (low function, depen... |
| Q18 | - |  |  | SI | The Lawton Instrumental Activities of Daily Living... |
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