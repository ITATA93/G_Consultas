# SQLUser.ARC_ItemDelivTimeRes

**Schema:** SQLUser
**Columnas:** 77
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DTR_ParRef | varchar | PK |  | NO | ARC_ItmMast Parent Reference |
| DTR_Childsub | double |  |  | NO | Childsub |
| DTR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DTR_CreatedDate | date |  |  | SI | Created Date |
| DTR_CreatedTime | time |  |  | SI | Created Time |
| DTR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DTR_DateFrom | date |  |  | SI | Date From |
| DTR_DateTo | date |  |  | SI | Date To |
| DTR_Priority_DR | bigint |  | FK | SI | Des Ref Priority |
| DTR_RecLoc_DR | bigint |  | FK | SI | Des Ref RecLoc |
| DTR_RowId | varchar |  |  | NO | - |
| DTR_Time | varchar |  |  | SI | Time |
| DTR_UpdatedDate | date |  |  | SI | Updated Date |
| DTR_UpdatedTime | time |  |  | SI | Updated Time |
| DTR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Age? |
| Q02 | - |  |  | SI | Time? (to the nearest hour) |
| Q03 | - |  |  | SI | Address for recall at the end of test: '42 West St... |
| Q03a | - |  |  | SI | (this should be repeated by the patient to ensure ... |
| Q03b | - |  |  | SI | Address recall correct? |
| Q04 | - |  |  | SI | Year? |
| Q05 | - |  |  | SI | Name of this place? |
| Q06 | - |  |  | SI | Identification of two persons (doctor, nurse etc.)... |
| Q07 | - |  |  | SI | Date of birth? |
| Q08 | - |  |  | SI | Last year of second world war? |
| Q09 | - |  |  | SI | Name of the present monarch? |
| Q10 | - |  |  | SI | Count backwards 20 to 1 |
| Q17 | - |  |  | SI | Date |
| Q18 | - |  |  | SI | Time |
| Q19 | - |  |  | SI | The Abbreviated Mental Test Score was described in... |
| Q20 | - |  |  | SI | 1.&nbsp |
| Q21 | - |  |  | SI | 2.&nbsp |
| Q22 | - |  |  | SI | 3.&nbsp |
| QAMTS | - |  |  | SI | The Abbreviated mental test score (AMTS) is a ques... |
| QSCORE1 | - |  |  | SI | Significantly Impaired: less than 7 correct answer... |
| QSCORE2 | - |  |  | SI | Probably Impaired: 7 correct answers |
| QSCORE3 | - |  |  | SI | Normal: 8 or more correct answers |
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