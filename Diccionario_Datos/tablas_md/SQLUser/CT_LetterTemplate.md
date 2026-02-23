# SQLUser.CT_LetterTemplate

**Schema:** SQLUser
**Columnas:** 89
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LT_RowId | bigint | PK |  | NO | - |
| LT_BaseTable | varchar |  |  | SI | - |
| LT_Code | varchar |  |  | NO | - |
| LT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LT_CreateBrowser | varchar |  |  | SI | - |
| LT_CreatedDate | date |  |  | SI | Created Date |
| LT_CreatedTime | time |  |  | SI | Created Time |
| LT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LT_DateFrom | date |  |  | SI | - |
| LT_DateTo | date |  |  | SI | - |
| LT_DefaultSickNotesStatus | varchar |  |  | SI | - |
| LT_Desc | varchar |  |  | NO | - |
| LT_Language | bigint |  |  | SI | - |
| LT_LetterCategory_DR | bigint |  | FK | SI | - |
| LT_LinkMaster | bigint |  |  | SI | - |
| LT_Owner | varchar |  |  | SI | Owner |
| LT_Report | bigint |  |  | SI | - |
| LT_Signature1 | varchar |  |  | SI | Signature 1 |
| LT_Signature2 | varchar |  |  | SI | Signature 2 |
| LT_Signature3 | varchar |  |  | SI | Signature 3 |
| LT_Signature4 | varchar |  |  | SI | Signature 4 |
| LT_Signature5 | varchar |  |  | SI | Signature 5 |
| LT_Signature6 | varchar |  |  | SI | Signature 6 |
| LT_Signature7 | varchar |  |  | SI | Signature 7 |
| LT_Signature8 | varchar |  |  | SI | Signature 8 |
| LT_StreamData | longvarchar |  |  | SI | Letter Template
HTMLRichText |
| LT_UpdateBrowser | varchar |  |  | SI | - |
| LT_UpdatedDate | date |  |  | SI | Updated Date |
| LT_UpdatedTime | time |  |  | SI | Updated Time |
| LT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| LT_WrittenCommuFormat | bigint |  |  | SI | - |
| Q01 | - |  |  | SI | Is current pregnancy with a new partner |
| Q01ObsDR | - |  |  | SI | Is current pregnancy with a new partner DR |
| Q02 | - |  |  | SI | Are you and the baby's father blood relatives |
| Q02ObsDR | - |  |  | SI | Are you and the baby's father blood relatives DR |
| Q03 | - |  |  | SI | How do you describe your baby's father's ethinc gr... |
| Q04 | - |  |  | SI | Date of Birth |
| Q05 | - |  |  | SI | Occupation |
| Q06 | - |  |  | SI | Smoker |
| Q06ObsDR | - |  |  | SI | Smoker DR |
| Q07 | - |  |  | SI | Units of alcohol per week |
| Q07ObsDR | - |  |  | SI | Units of alcohol per week DR |
| Q08 | - |  |  | SI | Does you partner currently use any oral street dru... |
| Q08ObsDR | - |  |  | SI | Does you partner currently use any oral street dru... |
| Q09 | - |  |  | SI | Does your current partner ever inject drugs |
| Q09ObsDR | - |  |  | SI | Does your current partner ever inject drugs DR |
| Q10 | - |  |  | SI | Any health issues |
| Q11 | - |  |  | SI | Comments/any other information |
| Q12 | - |  |  | SI | Midwife countersigning |
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