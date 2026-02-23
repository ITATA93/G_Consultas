# SQLUser.LBC_CourierSchedule

**Schema:** SQLUser
**Columnas:** 73
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCCS_ParRef | bigint | PK |  | NO | Parent Courier DR |
| LBCCS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCCS_RowID | varchar |  |  | NO | - |
| LBCCS_TimeEnd | time |  |  | NO | Time End |
| LBCCS_TimeStart | time |  |  | NO | Time Start |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Relevant history |
| Q04 | - |  |  | SI | Patient has had a recent pulmonary function test |
| Q05 | - |  |  | SI | Patient a smoker or ex-smoker |
| Q06 | - |  |  | SI | Quit date if applicable |
| Q07 | - |  |  | SI | Patient has had a recent stress test |
| Q08 | - |  |  | SI | Date of stress test |
| Q09 | - |  |  | SI | Patient has had a recent  electrocardiogram (ECG) |
| Q10 | - |  |  | SI | Date of latest ECG |
| Q11 | - |  |  | SI | Patient has had a recent echocardiogram |
| Q12 | - |  |  | SI | Date of latest echocardiogram |
| Q13 | - |  |  | SI | Patient has had a recent dobutamine stress echo / ... |
| Q14 | - |  |  | SI | Date of dobutamine test |
| Q15 | - |  |  | SI | Recent blood results checked for estimated glomeru... |
| Q16 | - |  |  | SI | History and investigation notes |
| Q17 | - |  |  | SI | Patient female and aged between 10 and 60 years of... |
| Q18 | - |  |  | SI | Pregnancy test result |
| Q18ObsDR | - |  |  | SI | Pregnancy test result DR |
| Q19 | - |  |  | SI | Patient is breastfeeding |
| Q20 | - |  |  | SI | Beta blocker given in the night |
| Q21 | - |  |  | SI | Name and dose of beta blocker |
| Q22 | - |  |  | SI | Beta blocker given in the morning |
| Q23 | - |  |  | SI | Name and dose of beta blocker |
| Q24 | - |  |  | SI | Other medications taken to slow heart rate |
| Q25 | - |  |  | SI | No caffeine or stimulants for 12 hours |
| Q26 | - |  |  | SI | Medication / Stimulant notes |
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
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*