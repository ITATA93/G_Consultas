# SQLUser.PAC_TriageCatChangeReason

**Schema:** SQLUser
**Columnas:** 92
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TRCATCHR_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | I have been advised that I/my* should |
| Q04 | - |  |  | SI | And I have decided to refuse the medical advice do... |
| Q05 | - |  |  | SI | Parent / Guardian reason for refusing medical advi... |
| Q06 | - |  |  | SI | I acknowledge that I have made this decision for m... |
| Q07 | - |  |  | SI | *In the case of a minor the parent or guardian's s... |
| Q08 | - |  |  | SI | *In the case of an adult under Guardianship the gu... |
| Q09 | - |  |  | SI | Patient signature |
| Q09UDt | - |  |  | SI | Patient signature Last Updated Date |
| Q09UTm | - |  |  | SI | Patient signature Last Updated Time |
| Q10 | - |  |  | SI | Care provider |
| Q11 | - |  |  | SI | (designation) |
| Q12 | - |  |  | SI | Care provider signature |
| Q12UDt | - |  |  | SI | Care provider signature Last Updated Date |
| Q12UTm | - |  |  | SI | Care provider signature Last Updated Time |
| Q13 | - |  |  | SI | I confirm I am a person with parental / guardiansh... |
| Q14 | - |  |  | SI | Parent / Guardian signature |
| Q14UDt | - |  |  | SI | Parent / Guardian signature Last Updated Date |
| Q14UTm | - |  |  | SI | Parent / Guardian signature Last Updated Time |
| Q15 | - |  |  | SI | Parent / Guardian name |
| Q16 | - |  |  | SI | Witness signature |
| Q16UDt | - |  |  | SI | Witness signature Last Updated Date |
| Q16UTm | - |  |  | SI | Witness signature Last Updated Time |
| Q17 | - |  |  | SI | Witness name |
| Q18 | - |  |  | SI | The above was explained to the patient who decline... |
| Q19 | - |  |  | SI | Mental Health Inpatient only - I have assessed thi... |
| Q20 | - |  |  | SI | Patient left against medical advice |
| Q21 | - |  |  | SI | Patient left ward / Centre / Department |
| Q22 | - |  |  | SI | On |
| Q23 | - |  |  | SI | Time |
| Q24 | - |  |  | SI | Staff 1 signature |
| Q24UDt | - |  |  | SI | Staff 1 signature Last Updated Date |
| Q24UTm | - |  |  | SI | Staff 1 signature Last Updated Time |
| Q25 | - |  |  | SI | Staff 1 name |
| Q26 | - |  |  | SI | Staff 1 signature |
| Q26UDt | - |  |  | SI | Staff 1 signature Last Updated Date |
| Q26UTm | - |  |  | SI | Staff 1 signature Last Updated Time |
| Q27 | - |  |  | SI | Staff 1 name |
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
| TRCATCHR_Code | varchar |  |  | NO | Code |
| TRCATCHR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| TRCATCHR_CreatedDate | date |  |  | SI | Created Date |
| TRCATCHR_CreatedTime | time |  |  | SI | Created Time |
| TRCATCHR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| TRCATCHR_DateFrom | date |  |  | SI | Date From |
| TRCATCHR_DateTo | date |  |  | SI | Date To |
| TRCATCHR_Desc | varchar |  |  | NO | Description |
| TRCATCHR_Owner | varchar |  |  | SI | Owner |
| TRCATCHR_UpdatedDate | date |  |  | SI | Updated Date |
| TRCATCHR_UpdatedTime | time |  |  | SI | Updated Time |
| TRCATCHR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*