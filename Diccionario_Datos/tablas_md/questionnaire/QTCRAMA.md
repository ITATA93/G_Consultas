# questionnaire.QTCRAMA

> Refusal to Accept Medical Advice

**Schema:** questionnaire
**Columnas:** 80
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Refusal to Accept Medical Advice

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | I have been advised that I/my* should |
| Q04 | varchar |  |  | SI | And I have decided to refuse the medical advice do... |
| Q05 | varchar |  |  | SI | Parent / Guardian reason for refusing medical advi... |
| Q06 | varchar |  |  | SI | I acknowledge that I have made this decision for m... |
| Q07 | varchar |  |  | SI | *In the case of a minor the parent or guardian's s... |
| Q08 | varchar |  |  | SI | *In the case of an adult under Guardianship the gu... |
| Q09 | longvarbinary |  |  | SI | Patient signature |
| Q09UDt | date |  |  | SI | Patient signature Last Updated Date |
| Q09UTm | time |  |  | SI | Patient signature Last Updated Time |
| Q10 | varchar |  |  | SI | Care provider |
| Q11 | varchar |  |  | SI | (designation) |
| Q12 | longvarbinary |  |  | SI | Care provider signature |
| Q12UDt | date |  |  | SI | Care provider signature Last Updated Date |
| Q12UTm | time |  |  | SI | Care provider signature Last Updated Time |
| Q13 | varchar |  |  | SI | I confirm I am a person with parental / guardiansh... |
| Q14 | longvarbinary |  |  | SI | Parent / Guardian signature |
| Q14UDt | date |  |  | SI | Parent / Guardian signature Last Updated Date |
| Q14UTm | time |  |  | SI | Parent / Guardian signature Last Updated Time |
| Q15 | varchar |  |  | SI | Parent / Guardian name |
| Q16 | longvarbinary |  |  | SI | Witness signature |
| Q16UDt | date |  |  | SI | Witness signature Last Updated Date |
| Q16UTm | time |  |  | SI | Witness signature Last Updated Time |
| Q17 | varchar |  |  | SI | Witness name |
| Q18 | varchar |  |  | SI | The above was explained to the patient who decline... |
| Q19 | varchar |  |  | SI | Mental Health Inpatient only - I have assessed thi... |
| Q20 | varchar |  |  | SI | Patient left against medical advice |
| Q21 | varchar |  |  | SI | Patient left ward / Centre / Department |
| Q22 | date |  |  | SI | On |
| Q23 | time |  |  | SI | Time |
| Q24 | longvarbinary |  |  | SI | Staff 1 signature |
| Q24UDt | date |  |  | SI | Staff 1 signature Last Updated Date |
| Q24UTm | time |  |  | SI | Staff 1 signature Last Updated Time |
| Q25 | varchar |  |  | SI | Staff 1 name |
| Q26 | longvarbinary |  |  | SI | Staff 1 signature |
| Q26UDt | date |  |  | SI | Staff 1 signature Last Updated Date |
| Q26UTm | time |  |  | SI | Staff 1 signature Last Updated Time |
| Q27 | varchar |  |  | SI | Staff 1 name |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*