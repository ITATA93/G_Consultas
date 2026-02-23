# SQLUser.CT_InterfaceCodingSystem

**Schema:** SQLUser
**Columnas:** 95
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTICS_RowID | bigint | PK |  | NO | - |
| CTICS_Code | varchar |  |  | NO | Code |
| CTICS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CTICS_Comment | varchar |  |  | SI | Notes |
| CTICS_CreatedDate | date |  |  | SI | Created Date |
| CTICS_CreatedTime | time |  |  | SI | Created Time |
| CTICS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CTICS_DateFrom | date |  |  | SI | Effective date for the record |
| CTICS_DateTo | date |  |  | SI | Last day the record is active  |
| CTICS_Desc | varchar |  |  | NO | Description |
| CTICS_Owner | varchar |  |  | SI | Owner |
| CTICS_System | varchar |  |  | SI | System Created |
| CTICS_UpdatedDate | date |  |  | SI | Updated Date |
| CTICS_UpdatedTime | time |  |  | SI | Updated Time |
| CTICS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Gestation |
| Q04 | - |  |  | SI | weeks |
| Q05 | - |  |  | SI | Gestation days |
| Q06 | - |  |  | SI | days |
| Q07 | - |  |  | SI | Indication for amniocentesis |
| Q08 | - |  |  | SI | Other indication for amniocentesis |
| Q09 | - |  |  | SI | Consent obtained |
| Q10 | - |  |  | SI | Serology checked |
| Q11 | - |  |  | SI | Rhesus status checked |
| Q12 | - |  |  | SI | Plurality |
| Q13 | - |  |  | SI | Fetal cardiac activity pre procedure |
| Q14 | - |  |  | SI | Fetal heart rate pre procedure (bpm) |
| Q15 | - |  |  | SI | Fetus 2 cardiac activity pre procedure |
| Q16 | - |  |  | SI | Fetus 2 heart rate pre procedure (bpm) |
| Q17 | - |  |  | SI | Fetus 3 cardiac activity pre procedure |
| Q18 | - |  |  | SI | Placenta traversed |
| Q19 | - |  |  | SI | Volume amniotic fluid obtained (mls) |
| Q20 | - |  |  | SI | Amniotic fluid aspect |
| Q21 | - |  |  | SI | Other amniotic fluid aspect |
| Q22 | - |  |  | SI | Number of attempts |
| Q23 | - |  |  | SI | Procedure notes |
| Q24 | - |  |  | SI | Fetal cardiac activity post procedure |
| Q24ObsDR | - |  |  | SI | Fetal cardiac activity post procedure DR |
| Q25 | - |  |  | SI | Fetal heart rate post procedure (bpm) |
| Q25ObsDR | - |  |  | SI | Fetal heart rate post procedure (bpm) DR |
| Q26 | - |  |  | SI | Fetus 2 cardiac activity post procedure |
| Q26ObsDR | - |  |  | SI | Fetus 2 cardiac activity post procedure DR |
| Q27 | - |  |  | SI | Fetus 2 heart rate post procedure (bpm) |
| Q27ObsDR | - |  |  | SI | Fetus 2 heart rate post procedure (bpm) DR |
| Q28 | - |  |  | SI | Fetus 3 cardiac activity post procedure |
| Q28ObsDR | - |  |  | SI | Fetus 3 cardiac activity post procedure DR |
| Q29 | - |  |  | SI | Fetus 3 heart rate post procedure (bpm) |
| Q29ObsDR | - |  |  | SI | Fetus 3 heart rate post procedure (bpm) DR |
| Q30 | - |  |  | SI | Management plan |
| Q31 | - |  |  | SI | Fetus 3 heart rate pre procedure (bpm) |
| Q32 | - |  |  | SI | Pre-Procedure |
| Q33 | - |  |  | SI | Procedure Details |
| Q34 | - |  |  | SI | Post-Procedure |
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