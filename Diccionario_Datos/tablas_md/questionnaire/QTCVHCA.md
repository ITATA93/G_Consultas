# questionnaire.QTCVHCA

> Viral Hepatitis Clinic Assessment

**Schema:** questionnaire
**Columnas:** 89
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Viral Hepatitis Clinic Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Hepatitis |
| Q04 | varchar |  |  | SI | Hepatitis B status |
| Q05 | varchar |  |  | SI | Hepatitis B status details |
| Q06 | varchar |  |  | SI | Hepatitis C status |
| Q07 | varchar |  |  | SI | Hepatitis C status details |
| Q08 | varchar |  |  | SI | Hepatitis C genotype |
| Q09 | varchar |  |  | SI | Hepatitis C genotype details |
| Q10 | varchar |  |  | SI | Therapy history |
| Q11 | varchar |  |  | SI | Co-infections |
| Q12 | varchar |  |  | SI | Hepatitis D status |
| Q13 | varchar |  |  | SI | Hepatitis D status details |
| Q14 | varchar |  |  | SI | Hepatitis A status |
| Q15 | varchar |  |  | SI | Hepatitis A status details |
| Q16 | varchar |  |  | SI | Extended liver screen |
| Q17 | varchar |  |  | SI | Extended liver screen details |
| Q18 | varchar |  |  | SI | Hepatitis notes |
| Q19 | varchar |  |  | SI | Other Viruses |
| Q20 | varchar |  |  | SI | HIV status |
| Q21 | varchar |  |  | SI | HIV status details |
| Q22 | varchar |  |  | SI | Cirrhosis |
| Q23 | varchar |  |  | SI | Cirrhosis details |
| Q24 | varchar |  |  | SI | Liver fibrosis |
| Q25 | varchar |  |  | SI | Liver fibrosis details |
| Q26 | varchar |  |  | SI | Fibro scan result |
| Q27 | numeric |  |  | SI | Hepascore |
| Q28 | numeric |  |  | SI | APRI score |
| Q29 | varchar |  |  | SI | Other virus notes |
| Q30 | varchar |  |  | SI | Gastroscopy Variceal Screening |
| Q31 | varchar |  |  | SI | Gastroscopy variceal screening required |
| Q32 | date |  |  | SI | Date of last variceal screen |
| Q33 | varchar |  |  | SI | Variceal screen details |
| Q34 | date |  |  | SI | Next variceal screen due |
| Q35 | varchar |  |  | SI | Variceal screening notes |
| Q36 | varchar |  |  | SI | Hepatocellular Carcinoma Screening |
| Q37 | varchar |  |  | SI | Hepatocellular Carcinoma (HCC) screening required |
| Q38 | date |  |  | SI | Date of last HCC screen |
| Q39 | varchar |  |  | SI | HHC screen details |
| Q40 | date |  |  | SI | Next HCC screen due |
| Q41 | varchar |  |  | SI | HCC notes |
| Q42 | varchar |  |  | SI | Bone Mineral Density Screening |
| Q43 | varchar |  |  | SI | Bone Mineral Density (BMD) screen in cirrhotic pat... |
| Q44 | varchar |  |  | SI | Comments on last BMD |
| Q45 | date |  |  | SI | Date of last BMD screen |
| Q46 | varchar |  |  | SI | BMD screen details |
| Q47 | date |  |  | SI | Next BMD screen due |
| Q48 | varchar |  |  | SI | BMD notes |
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