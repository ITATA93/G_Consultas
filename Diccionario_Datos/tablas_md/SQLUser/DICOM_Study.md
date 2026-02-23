# SQLUser.DICOM_Study

**Schema:** SQLUser
**Columnas:** 71
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Imágenes Diagnósticas**. Radiología y estudios de imagen.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DCSTY_RowID | varchar | PK |  | NO | - |
| DCSTY_AccessionNumber | varchar |  |  | SI | Accession Number |
| DCSTY_DeleteStatus | varchar |  |  | SI | Status of Study |
| DCSTY_DeleteStatusDate | date |  |  | SI | Delete Status Date |
| DCSTY_DeleteStatusTime | time |  |  | SI | Delete status time |
| DCSTY_Description | varchar |  |  | SI | Description |
| DCSTY_Patient_DR | varchar |  | FK | SI | DICOM Patient DR |
| DCSTY_RefDoctorName | varchar |  |  | SI | Ref Doctor Name |
| DCSTY_StudyDate | date |  |  | SI | Study Date |
| DCSTY_StudyID | varchar |  |  | SI | StudyID |
| DCSTY_StudyInstanceUID | varchar |  |  | NO | Study Instance UID |
| DCSTY_StudyTime | time |  |  | SI | Study Time |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Age ≥72 years old |
| Q04 | - |  |  | SI | Cancer type (gastrointestinal or genitourinary) |
| Q05 | - |  |  | SI | Chemotherapy dosing (standard dosing) |
| Q06 | - |  |  | SI | More than one chemotherapy drug (polychemotherapy) |
| Q07 | - |  |  | SI | Haemoglobin (&lt |
| Q08 | - |  |  | SI | Creatinine clearance (&lt |
| Q09 | - |  |  | SI | Hearing (fair, poor, or deaf) |
| Q10 | - |  |  | SI | Number of falls in the past 6 months (one or more) |
| Q11 | - |  |  | SI | Take medications with some help or unable |
| Q12 | - |  |  | SI | Walking one block, somewhat limited or limited a l... |
| Q13 | - |  |  | SI | Decreased social activity because of physical or e... |
| Q14 | - |  |  | SI | The CARG Chemotherapy Toxicity Tool was published ... |
| Q15 | - |  |  | SI | And estimates the proportion of patients that deve... |
| Q16 | - |  |  | SI | 1. Hurria A, Togawa K, Mohile SG, et al. Predictin... |
| Q17 | - |  |  | SI | 2. National Cancer Institute Common Terminology Cr... |
| Q18 | - |  |  | SI | https://ctep.cancer.gov/protocoldevelopment/electr... |
| Q19 | - |  |  | SI | Cancer and Aging Research Group (CARG) Chemotherap... |
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