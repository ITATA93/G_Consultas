# questionnaire.QGXXXPOC

> Pre Operative Dual Sign off Checklists

**Schema:** questionnaire
**Columnas:** 131
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Pre Operative Dual Sign off Checklists

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01a | bit |  |  | SI | ID band |
| Q01b | bit |  |  | SI | ID band |
| Q02a | time |  |  | SI | Patient last ate/drank |
| Q02aa | date |  |  | SI | Patient last ate / drank |
| Q02b | time |  |  | SI | Patient last ate/drank |
| Q02bb | date |  |  | SI | Patient last ate / drank |
| Q03a | bit |  |  | SI | Surgical consent form signed |
| Q04a | bit |  |  | SI | Operation site marked |
| Q04b | bit |  |  | SI | Operation site marked |
| Q05a | varchar |  |  | SI | Notes |
| Q05b | varchar |  |  | SI | Notes |
| Q05c | bit |  |  | SI | Pre-operative medication |
| Q05d | bit |  |  | SI | Pre-operative medication |
| Q06a | bit |  |  | SI | Anaesthetic chart |
| Q06b | bit |  |  | SI | Anaesthetic chart |
| Q07a | bit |  |  | SI | Drug chart |
| Q07b | bit |  |  | SI | Drug chart |
| Q08a | bit |  |  | SI | Blood forms |
| Q08b | bit |  |  | SI | Blood forms |
| Q09a | bit |  |  | SI | Cross match forms |
| Q09b | bit |  |  | SI | Cross match forms |
| Q10a | bit |  |  | SI | X-rays |
| Q10b | bit |  |  | SI | X-rays |
| Q10c | bit |  |  | SI | ECG |
| Q10d | bit |  |  | SI | ECG |
| Q10e | varchar |  |  | SI | Catheters / Drains |
| Q10f | varchar |  |  | SI | Catheters / Drains |
| Q11a | bit |  |  | SI | Patient ID labels |
| Q11b | bit |  |  | SI | Patient ID labels |
| Q12a | bit |  |  | SI | Anti-embolism stockings |
| Q12b | bit |  |  | SI | Anti-embolism stockings |
| Q13a | bit |  |  | SI | Shaved |
| Q13b | bit |  |  | SI | Shaved |
| Q14a | time |  |  | SI | Passed urine |
| Q14aa | date |  |  | SI | Patient last ate / drank |
| Q14b | time |  |  | SI | Passed urine |
| Q14bb | date |  |  | SI | Patient last ate / drank |
| Q15 | varchar |  |  | SI | Dentures / Crowns |
| Q15a | varchar |  |  | SI | Dentures / Crowns |
| Q16 | varchar |  |  | SI | Jewellery |
| Q16a | varchar |  |  | SI | Jewellery |
| Q17 | varchar |  |  | SI | Spectacles / Contact lenses |
| Q17a | varchar |  |  | SI | Spectacles / Contact lenses |
| Q18 | varchar |  |  | SI | Underwear |
| Q18a | varchar |  |  | SI | Underwear |
| Q19 | varchar |  |  | SI | Prosthesis |
| Q19a | varchar |  |  | SI | Prosthesis |
| Q19b | varchar |  |  | SI | Implants |
| Q19c | varchar |  |  | SI | Implants |
| Q20 | varchar |  |  | SI | Hearing aid |
| Q20a | varchar |  |  | SI | Hearing aid |
| Q21 | varchar |  |  | SI | Nail polish / Make up |
| Q21a | varchar |  |  | SI | Nail Polish / Make up |
| Q21b | bit |  |  | SI | Rashes |
| Q21bb | bit |  |  | SI | Rashes |
| Q21c | bit |  |  | SI | Septic foci |
| Q21cc | bit |  |  | SI | Septic foci |
| Q21d | varchar |  |  | SI | Others |
| Q21e | varchar |  |  | SI | Isolation precaution |
| Q21ee | varchar |  |  | SI | Isolation precaution |
| Q21f | varchar |  |  | SI | Level of consciousness |
| Q21g | varchar |  |  | SI | Level of consciousness |
| Q22 | varchar |  |  | SI | Inhalers |
| Q22a | varchar |  |  | SI | Inhalers |
| Q23 | varchar |  |  | SI | Others |
| Q3b | bit |  |  | SI | Surgical consent form signed |
| Q3c | bit |  |  | SI | Anaesthesia consent form signed |
| Q3d | bit |  |  | SI | Anaesthesia consent form signed |
| Q3e | bit |  |  | SI | General consent form signed |
| Q3f | bit |  |  | SI | General consent form signed |
| Q71 | varchar |  |  | SI | List the treatment(s)/ operation(s)/ investigation... |
| Q72 | varchar |  |  | SI | Free text - List the treatment(s)/ operation(s)/ i... |
| Q73a | varchar |  |  | SI | Care provider |
| Q73b | varchar |  |  | SI | Care provider role |
| Q73c | longvarbinary |  |  | SI | Signature |
| Q73cUDt | date |  |  | SI | Signature Last Updated Date |
| Q73cUTm | time |  |  | SI | Signature Last Updated Time |
| Q76a | varchar |  |  | SI | Care provider |
| Q76b | varchar |  |  | SI | Care provider role |
| Q76c | longvarbinary |  |  | SI | Signature |
| Q76cUDt | date |  |  | SI | Signature Last Updated Date |
| Q76cUTm | time |  |  | SI | Signature Last Updated Time |
| Q79 | time |  |  | SI | Patient last ate |
| Q79b | time |  |  | SI | Patient last ate |
| Q80a | time |  |  | SI | Patient last drank |
| Q80b | time |  |  | SI | Patient last drank |
| Q83 | date |  |  | SI | Date |
| Q84 | time |  |  | SI | Time |
| Q85 | varchar |  |  | SI | Passed urine |
| Q86 | varchar |  |  | SI | Passed urine |
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