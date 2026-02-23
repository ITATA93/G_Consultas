# questionnaire.QTCMRIQ

> MRI Questionnaire

**Schema:** questionnaire
**Columnas:** 89
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* MRI Questionnaire

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | MRI Safety |
| Q02 | varchar |  |  | SI | Does the patient have a pacemaker or artificial he... |
| Q02a | varchar |  |  | SI | PLEASE NOTE - It is extremely dangerous to perform... |
| Q02b | varchar |  |  | SI | Is this MRI compatible / programmable? |
| Q02b1 | varchar |  |  | SI | The patient is incompatible for MRI – Cannot be or... |
| Q02c | date |  |  | SI | Date of insertion |
| Q02d | varchar |  |  | SI | Place of insertion |
| Q03 | varchar |  |  | SI | Does the patient have any aneurysm clips in their ... |
| Q03a | varchar |  |  | SI | PLEASE NOTE, It is extremely dangerous to perform ... |
| Q03b | date |  |  | SI | Date of insertion |
| Q03c | varchar |  |  | SI | Place of insertion |
| Q04 | varchar |  |  | SI | Does the patient have any electronic devices / imp... |
| Q04a | varchar |  |  | SI | PLEASE NOTE, Implanted electronic devices must be ... |
| Q04b | date |  |  | SI | Date of insertion |
| Q04c | varchar |  |  | SI | Place of insertion |
| Q05 | varchar |  |  | SI | Has the patient ever worked with metal filings? (e... |
| Q05a | varchar |  |  | SI | Has the patient ever had fragments in their eyes? |
| Q05a1 | varchar |  |  | SI | Please request an XR Orbits at the same time |
| Q06 | varchar |  |  | SI | Weight (kg) |
| Q06ObsDR | varchar |  | FK | SI | Weight (kg) DR |
| Q07 | varchar |  |  | SI | Height (cm) |
| Q07ObsDR | varchar |  | FK | SI | Height (cm) DR |
| Q08 | varchar |  |  | SI | BMI (kg/m2) |
| Q09 | varchar |  |  | SI | Has the patient had a previous MRI? |
| Q09a | date |  |  | SI | Date of MRI |
| Q09b | varchar |  |  | SI | Body part |
| Q10 | varchar |  |  | SI | Has the patient had previous surgery? |
| Q10a | date |  |  | SI | Date of surgery |
| Q10b | varchar |  |  | SI | Procedure (free text) |
| Q10c | varchar |  |  | SI | Procedure |
| Q10d | varchar |  |  | SI | Operation |
| Q11 | varchar |  |  | SI | Is the patient able to lie flat and still for 30 m... |
| Q11a | varchar |  |  | SI | Please, consider sedation |
| Q12 | varchar |  |  | SI | Is there a clip on the catheter bag drain? |
| Q12a | varchar |  |  | SI | Change to bag with no metal clips |
| Q13 | varchar |  |  | SI | Does the patient have pump drivers attached? |
| Q13a | varchar |  |  | SI | Must be removed prior to arrival |
| Q14 | varchar |  |  | SI | Renal Function |
| Q15 | varchar |  |  | SI | Is the patient aged over 65? |
| Q16 | varchar |  |  | SI | Is the patient diabetic? |
| Q17 | varchar |  |  | SI | Does the patient suffer from heart failure? |
| Q18 | varchar |  |  | SI | Does the patient have any known chronic kidney dis... |
| Q19 | varchar |  |  | SI | Did you answer 'Yes' to a Renal Function question? |
| Q19a | numeric |  |  | SI | Estimated Glomerular Filtration Rate (eGFR) level |
| Q19b | date |  |  | SI | Date of last eGFR test |
| Q19c | numeric |  |  | SI | Creatinine level |
| Q19d | date |  |  | SI | Date of last Creatinine test |
| Q19e | varchar |  |  | SI | If this test is older than 6 weeks then please ens... |
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