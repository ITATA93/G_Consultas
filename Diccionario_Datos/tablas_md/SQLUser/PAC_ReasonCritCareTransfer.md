# SQLUser.PAC_ReasonCritCareTransfer

**Schema:** SQLUser
**Columnas:** 89
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RCCT_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Pain onset |
| Q04 | - |  |  | SI | Pain onset time |
| Q05 | - |  |  | SI | Details of event leading to onset |
| Q06 | - |  |  | SI | Pain rating scale |
| Q07 | - |  |  | SI | Please see guidelines section  for details on all ... |
| Q08 | - |  |  | SI | Numerical rating pain scale (0 to 10) |
| Q09 | - |  |  | SI | 4 point verbal rating pain scale |
| Q09ObsDR | - |  |  | SI | 4 point verbal rating pain scale DR |
| Q10 | - |  |  | SI | Visual Analogue Scale (0 to 10) |
| Q10ObsDR | - |  |  | SI | Visual Analogue Scale (0 to 10) DR |
| Q11 | - |  |  | SI | Wong-Baker FACES pain rating scale |
| Q11ObsDR | - |  |  | SI | Wong-Baker FACES pain rating scale DR |
| Q12 | - |  |  | SI | Patient's description of pain |
| Q12ObsDR | - |  |  | SI | Patient's description of pain DR |
| Q13 | - |  |  | SI | Pattern |
| Q14 | - |  |  | SI | Aggravating factors - what makes the pain worse? |
| Q14ObsDR | - |  |  | SI | Aggravating factors - what makes the pain worse? D... |
| Q15 | - |  |  | SI | Relieving factors - what makes the pain better? |
| Q15ObsDR | - |  |  | SI | Relieving factors - what makes the pain better? DR |
| Q16 | - |  |  | SI | Care provider type |
| Q17 | - |  |  | SI | Specialty |
| Q18 | - |  |  | SI | Numeric Rating Scale (0 - 10) |
| Q19 | - |  |  | SI | Visual Analogue Scale (VAS) |
| Q20 | - |  |  | SI | A VAS is usually a 100-mm long horizontal line wit... |
| Q21 | - |  |  | SI | Patients are instructed to mark the point on the l... |
| Q22 | - |  |  | SI | When reading the VAS, the position of the responde... |
| Q23 | - |  |  | SI | The VAS should not have any markings (e. g., ident... |
| Q24 | - |  |  | SI | Wong - Baker FACES® Pain Rating Scale Image |
| Q25 | - |  |  | SI | 4 Point Verbal Rating Scale |
| Q26 | - |  |  | SI | None: Negative response to questioning |
| Q27 | - |  |  | SI | Mild: Pain reported in response to questioning onl... |
| Q28 | - |  |  | SI | Moderate: Pain reported in response to questioning... |
| Q29 | - |  |  | SI | Severe: Strong verbal response or response accompa... |
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
| RCCT_Code | varchar |  |  | NO | Code |
| RCCT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| RCCT_CreatedDate | date |  |  | SI | Created Date |
| RCCT_CreatedTime | time |  |  | SI | Created Time |
| RCCT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RCCT_DateFrom | date |  |  | SI | Date From |
| RCCT_DateTo | date |  |  | SI | Date To |
| RCCT_Default | varchar |  |  | SI | Default |
| RCCT_Desc | varchar |  |  | NO | Description |
| RCCT_Owner | varchar |  |  | SI | Owner |
| RCCT_UpdatedDate | date |  |  | SI | Updated Date |
| RCCT_UpdatedTime | time |  |  | SI | Updated Time |
| RCCT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*