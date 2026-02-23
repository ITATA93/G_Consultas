# SQLUser.PAC_DiagCodeSys

**Schema:** SQLUser
**Columnas:** 82
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DCS_RowId | bigint | PK |  | NO | - |
| DCS_Code | varchar |  |  | NO | Code |
| DCS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DCS_CreatedDate | date |  |  | SI | Created Date |
| DCS_CreatedTime | time |  |  | SI | Created Time |
| DCS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DCS_DateFrom | date |  |  | SI | Date From |
| DCS_DateTo | date |  |  | SI | Date To |
| DCS_Desc | varchar |  |  | NO | Description |
| DCS_Owner | varchar |  |  | SI | Owner |
| DCS_UpdatedDate | date |  |  | SI | Updated Date |
| DCS_UpdatedTime | time |  |  | SI | Updated Time |
| DCS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | We are interested in knowing whether you are havin... |
| Q04 | - |  |  | SI | Please provide an answer for each activity. |
| Q05 | - |  |  | SI | Today, do you or would you have any difficulty at ... |
| Q06 | - |  |  | SI | Any of your usual work, housework, or school activ... |
| Q07 | - |  |  | SI | Your usual hobbies, recreational, or sporting acti... |
| Q08 | - |  |  | SI | Getting into or out of the bath |
| Q09 | - |  |  | SI | Walking between rooms |
| Q10 | - |  |  | SI | Putting on your shoes or socks |
| Q11 | - |  |  | SI | Squatting |
| Q12 | - |  |  | SI | Lifting an object, like a bag of groceries from th... |
| Q13 | - |  |  | SI | Performing light activities around your home |
| Q14 | - |  |  | SI | Performing heavy activities around your home |
| Q15 | - |  |  | SI | Getting into or out of a car |
| Q16 | - |  |  | SI | Walking 2 blocks |
| Q17 | - |  |  | SI | Walking a mile |
| Q18 | - |  |  | SI | Going up or down 10 stairs (about 1 flight of stai... |
| Q19 | - |  |  | SI | Standing for 1 hour |
| Q20 | - |  |  | SI | Sitting for 1 hour |
| Q21 | - |  |  | SI | Running on even ground |
| Q22 | - |  |  | SI | Running on uneven ground |
| Q23 | - |  |  | SI | Making sharp turns while running fast |
| Q24 | - |  |  | SI | Hopping |
| Q25 | - |  |  | SI | Rolling over in bed |
| Q26 | - |  |  | SI | Minimum level of detectable change (90% confidence... |
| Q27 | - |  |  | SI | The higher the score indicates a higher functional... |
| Q28 | - |  |  | SI | Binkley JM, Stratford PW, Lott SA, Riddle DL. The ... |
| Q29 | - |  |  | SI | The Lower Extremity Functional Scale (LEFS) can be... |
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