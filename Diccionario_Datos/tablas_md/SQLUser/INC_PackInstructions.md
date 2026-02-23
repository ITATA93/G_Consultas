# SQLUser.INC_PackInstructions

**Schema:** SQLUser
**Columnas:** 85
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Incidentes**. Reportes de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PKINS_RowId | bigint | PK |  | NO | - |
| PKINS_Code | varchar |  |  | SI | Code |
| PKINS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PKINS_CreatedDate | date |  |  | SI | Created Date |
| PKINS_CreatedTime | time |  |  | SI | Created Time |
| PKINS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PKINS_DateFrom | date |  |  | SI | Date From |
| PKINS_DateTo | date |  |  | SI | Date To |
| PKINS_Desc | varchar |  |  | SI | Description |
| PKINS_Owner | varchar |  |  | SI | Owner |
| PKINS_UpdatedDate | date |  |  | SI | Updated Date |
| PKINS_UpdatedTime | time |  |  | SI | Updated Time |
| PKINS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Asthma |
| Q04 | - |  |  | SI | How is your asthma today? |
| Q05 | - |  |  | SI | How much of a problem is your asthma when you run,... |
| Q06 | - |  |  | SI | Does your asthma make you cough? |
| Q07 | - |  |  | SI | Does your asthma make you wake up during the night... |
| Q08 | - |  |  | SI | During the last 4 weeks, how many days did your ch... |
| Q09 | - |  |  | SI | During the last 4 weeks, how many days did your ch... |
| Q10 | - |  |  | SI | During the last 4 weeks, how many days did your ch... |
| Q11 | - |  |  | SI | Score |
| Q12 | - |  |  | SI | Classification |
| Q13 | - |  |  | SI | 0 - 11 |
| Q14 | - |  |  | SI | Very poorly controlled asthma |
| Q15 | - |  |  | SI | 12 - 19 |
| Q16 | - |  |  | SI | Poorly controlled asthma |
| Q17 | - |  |  | SI | 20 - 27 |
| Q18 | - |  |  | SI | Well controlled asthma |
| Q19 | - |  |  | SI | 0 - 11: Very poorly controlled asthma |
| Q20 | - |  |  | SI | 12 - 19: Poorly controlled asthma |
| Q21 | - |  |  | SI | 20 - 27: Well controlled asthma |
| Q22 | - |  |  | SI | The Child Asthma Control Test (CACT) is a 7-item s... |
| Q23 | - |  |  | SI | Guidelines |
| Q24 | - |  |  | SI | • Let your child respond to the first 4 questions ... |
| Q25 | - |  |  | SI | Complete the remaining 3 questions (5 to 7) on you... |
| Q26 | - |  |  | SI | Provenance Details |
| Q27 | - |  |  | SI | Based on the publication: |
| Q28 | - |  |  | SI | • Development of the Asthma Control Test: A survey... |
| Q29 | - |  |  | SI | • Development and cross-sectional validation of th... |
| Q30 | - |  |  | SI | Important information for use |
| Q31 | - |  |  | SI | • The GSK Asthma Control Test is for persons whom ... |
| Q32 | - |  |  | SI | prevention, monitoring, prediction, prognosis, tre... |
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