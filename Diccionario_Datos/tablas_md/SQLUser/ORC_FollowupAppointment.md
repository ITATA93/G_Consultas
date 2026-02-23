# SQLUser.ORC_FollowupAppointment

**Schema:** SQLUser
**Columnas:** 85
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| FOLAPP_RowId | bigint | PK |  | NO | - |
| FOLAPP_Code | varchar |  |  | NO | Code |
| FOLAPP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| FOLAPP_CreatedDate | date |  |  | SI | Created Date |
| FOLAPP_CreatedTime | time |  |  | SI | Created Time |
| FOLAPP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| FOLAPP_DateFrom | date |  |  | SI | Date From |
| FOLAPP_DateTo | date |  |  | SI | Date To |
| FOLAPP_Desc | varchar |  |  | NO | Description |
| FOLAPP_Owner | varchar |  |  | SI | Owner |
| FOLAPP_UpdatedDate | date |  |  | SI | Updated Date |
| FOLAPP_UpdatedTime | time |  |  | SI | Updated Time |
| FOLAPP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Main diagnosis |
| Q04 | - |  |  | SI | Others |
| Q05 | - |  |  | SI | Main reason |
| Q06 | - |  |  | SI | Duration |
| Q07 | - |  |  | SI | Procedures / Interventions |
| Q08 | - |  |  | SI | Others |
| Q09 | - |  |  | SI | Device |
| Q10 | - |  |  | SI | Others |
| Q11 | - |  |  | SI | ECG lead |
| Q12 | - |  |  | SI | Operator |
| Q13 | - |  |  | SI | Receipt |
| Q14 | - |  |  | SI | Therapy |
| Q15 | - |  |  | SI | Holter device number |
| Q16 | - |  |  | SI | Exam date |
| Q17 | - |  |  | SI | Base rhythm |
| Q18 | - |  |  | SI | Over main rhythm |
| Q19 | - |  |  | SI | Atrioventricular conduction |
| Q20 | - |  |  | SI | Intraventricular conduction |
| Q21 | - |  |  | SI | Ventricular extrasystoles |
| Q22 | - |  |  | SI | Couples |
| Q23 | - |  |  | SI | Polymorphism |
| Q24 | - |  |  | SI | Non - sustained ventricular tachycardia |
| Q25 | - |  |  | SI | Sustained ventricular tachycardia |
| Q26 | - |  |  | SI | Supraventricular extrasystoles (frequency) |
| Q27 | - |  |  | SI | Supraventricular extrasystoles |
| Q28 | - |  |  | SI | Pause |
| Q29 | - |  |  | SI | Pause maximum duration (msec) |
| Q30 | - |  |  | SI | Wolff-Parkinson-White |
| Q31 | - |  |  | SI | ST segment modifications |
| Q32 | - |  |  | SI | Conclusion |
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