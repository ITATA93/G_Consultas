# questionnaire.QTCPICC

> Pre Isotretinoin counselling

**Schema:** questionnaire
**Columnas:** 63
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Pre Isotretinoin counselling

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Weight |
| Q01ObsDR | varchar |  | FK | SI | Weight DR |
| Q02 | varchar |  |  | SI | Patient has read and understands patient informati... |
| Q03 | varchar |  |  | SI | Have the following side effects been discussed in ... |
| Q04 | varchar |  |  | SI | 1 - Potential risk of depression and/or mood swing... |
| Q05 | varchar |  |  | SI | 2 - Hyperlipidaemia |
| Q06 | varchar |  |  | SI | 3 - Teratogenic risk (in females) |
| Q07 | varchar |  |  | SI | Patient advised to ask someone close to them to ob... |
| Q08 | varchar |  |  | SI | If there are any concerns Isotretinoin treatment s... |
| Q09 | varchar |  |  | SI | Have the following results been recorded and check... |
| Q10 | varchar |  |  | SI | The importance of not becoming pregnant for one mo... |
| Q11 | varchar |  |  | SI | Read and understood patient information leaflet on... |
| Q12 | varchar |  |  | SI | If patient is female and is of child bearing age a... |
| Q13 | varchar |  |  | SI | If sexually active the patient has been advised to... |
| Q14 | varchar |  |  | SI | If not sexually active and of child bearing age pa... |
| Q15 | varchar |  |  | SI | continue with it regularly until one month after s... |
| Q16 | varchar |  |  | SI | If patient is female and sexually active and not u... |
| Q17 | varchar |  |  | SI | Patient has been advised to attend Family Planning... |
| Q18 | varchar |  |  | SI | Acknowledgement form has been signed |
| Q19 | varchar |  |  | SI | Patient has been given the telephone number of the... |
| Q20 | varchar |  |  | SI | Completed blood form given to patient for repeat b... |
| Q21 | varchar |  |  | SI | Notes |
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