# questionnaire.QGXXXMANC

> Antenatal check

**Schema:** questionnaire
**Columnas:** 101
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Antenatal check

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Systolic blood pressure |
| Q01ObsDR | varchar |  | FK | SI | Systolic blood pressure DR |
| Q02 | varchar |  |  | SI | Diastolic blood pressure |
| Q02ObsDR | varchar |  | FK | SI | Diastolic blood pressure DR |
| Q03 | varchar |  |  | SI | Urinalysis abnormalities |
| Q03ObsDR | varchar |  | FK | SI | Urinalysis abnormalities DR |
| Q04 | varchar |  |  | SI | Oedema |
| Q04ObsDR | varchar |  | FK | SI | Oedema DR |
| Q05 | varchar |  |  | SI | Urinalysis |
| Q05ObsDR | varchar |  | FK | SI | Urinalysis DR |
| Q06 | varchar |  |  | SI | Presentation |
| Q06ObsDR | varchar |  | FK | SI | Presentation DR |
| Q07 | varchar |  |  | SI | External cephalic version offered |
| Q07ObsDR | varchar |  | FK | SI | External cephalic version offered DR |
| Q08 | varchar |  |  | SI | External cephalic version accepted |
| Q08ObsDR | varchar |  | FK | SI | External cephalic version accepted DR |
| Q09 | varchar |  |  | SI | External cephalic version discussed / info given |
| Q09ObsDR | varchar |  | FK | SI | External cephalic version discussed / info given D... |
| Q10 | varchar |  |  | SI | Details of external cephalic version procedure |
| Q11 | varchar |  |  | SI | Fundal height |
| Q11ObsDR | varchar |  | FK | SI | Fundal height DR |
| Q12 | varchar |  |  | SI | Lie |
| Q12ObsDR | varchar |  | FK | SI | Lie DR |
| Q13 | varchar |  |  | SI | Presentation / 5ths palpable |
| Q13ObsDR | varchar |  | FK | SI | Presentation / 5ths palpable DR |
| Q14 | varchar |  |  | SI | Fetal heart rate |
| Q14ObsDR | varchar |  | FK | SI | Fetal heart rate DR |
| Q15 | varchar |  |  | SI | Position |
| Q15ObsDR | varchar |  | FK | SI | Position DR |
| Q16 | varchar |  |  | SI | Fetal movement felt |
| Q16ObsDR | varchar |  | FK | SI | Fetal movement felt DR |
| Q17 | varchar |  |  | SI | Comments |
| Q18 | varchar |  |  | SI | Is follow-up to brief intervention required |
| Q18ObsDR | varchar |  | FK | SI | Is follow-up to brief intervention required DR |
| Q19 | varchar |  |  | SI | Alcohol units per week - currently |
| Q19ObsDR | varchar |  | FK | SI | Alcohol units per week - currently DR |
| Q20 | varchar |  |  | SI | Maximum units per day - currently |
| Q20ObsDR | varchar |  | FK | SI | Maximum units per day - currently DR |
| Q21 | varchar |  |  | SI | Plans for care |
| Q22 | varchar |  |  | SI | Midwife countersigning |
| Q23 | varchar |  |  | SI | Gestation: Weeks |
| Q23ObsDR | varchar |  | FK | SI | Gestation: Weeks DR |
| Q24 | varchar |  |  | SI | Weight in late pregnancy |
| Q24ObsDR | varchar |  | FK | SI | Weight in late pregnancy DR |
| Q25 | varchar |  |  | SI | Has thrombosis risk changed |
| Q25ObsDR | varchar |  | FK | SI | Has thrombosis risk changed DR |
| Q26 | varchar |  |  | SI | Urine Blood |
| Q26ObsDR | varchar |  | FK | SI | Urine Blood DR |
| Q27 | varchar |  |  | SI | Urine Glucose |
| Q27ObsDR | varchar |  | FK | SI | Urine Glucose DR |
| Q28 | varchar |  |  | SI | Urine Protein |
| Q28ObsDR | varchar |  | FK | SI | Urine Protein DR |
| Q29 | varchar |  |  | SI | Urine Leukocytes |
| Q29ObsDR | varchar |  | FK | SI | Urine Leukocytes DR |
| Q30 | varchar |  |  | SI | Urine Ketones |
| Q30ObsDR | varchar |  | FK | SI | Urine Ketones DR |
| Q31 | varchar |  |  | SI | Gestation: Days |
| Q31ObsDR | varchar |  | FK | SI | Gestation: Days DR |
| Q32 | date |  |  | SI | Date |
| Q33 | time |  |  | SI | Time |
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