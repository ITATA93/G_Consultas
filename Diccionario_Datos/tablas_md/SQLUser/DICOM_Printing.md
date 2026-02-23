# SQLUser.DICOM_Printing

**Schema:** SQLUser
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Imágenes Diagnósticas**. Radiología y estudios de imagen.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PR_RowId | bigint | PK |  | NO | - |
| PR_AETitle | varchar |  |  | SI | AETitle |
| PR_Date | date |  |  | SI | Date |
| PR_Format | varchar |  |  | SI | Format |
| PR_IPAddress | varchar |  |  | SI | Printer IPAddress |
| PR_Images | varchar |  |  | SI | Images |
| PR_OEORI_DR | varchar |  | FK | SI | Des Ref OEORI |
| PR_Port | varchar |  |  | SI | Dicom Port |
| PR_Reason | varchar |  |  | SI | Reason |
| PR_Status | varchar |  |  | SI | Status |
| PR_Time | time |  |  | SI | Time |
| PR_TimeInMins | double |  |  | SI | PR_TimeInMins |
| Q01 | - |  |  | SI | Checklist (Record evidence and comments in the box... |
| Q02 | - |  |  | SI | Does the unborn baby, infant, child or young perso... |
| Q03 | - |  |  | SI | Healthy? |
| Q03a | - |  |  | SI | Note |
| Q05 | - |  |  | SI | Safe from harm? |
| Q05a | - |  |  | SI | Note |
| Q07 | - |  |  | SI | Learning and developing? |
| Q07a | - |  |  | SI | Note |
| Q09 | - |  |  | SI | Having a positive impact on others? |
| Q09a | - |  |  | SI | Note |
| Q11 | - |  |  | SI | Free from the negative impact of poverty? |
| Q11a | - |  |  | SI | Note |
| Q13 | - |  |  | SI | If you answered No to any of the previous question... |
| Q14 | - |  |  | SI | Can you provide the additional services needed? |
| Q15 | - |  |  | SI | If you answered No or Not sure to any of the previ... |
| Q16 | - |  |  | SI | Who will do this assessment? |
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