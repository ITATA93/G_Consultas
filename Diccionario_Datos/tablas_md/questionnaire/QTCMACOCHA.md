# questionnaire.QTCMACOCHA

> MACOCHA Scoring

**Schema:** questionnaire
**Columnas:** 74
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* MACOCHA Scoring

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Mallampati score III - IV |
| Q04 | varchar |  |  | SI | Mouth opening < 3 Pt. finger |
| Q05 | varchar |  |  | SI | Reduced mobility of cervical spine |
| Q06 | varchar |  |  | SI | Obstructive sleep apnea syndrome (OSA) |
| Q07 | varchar |  |  | SI | Coma |
| Q08 | varchar |  |  | SI | Severe hypoxemia SPO2 < 80% on room air |
| Q09 | varchar |  |  | SI | Non anesthesiologist |
| Q10 | longvarbinary |  |  | SI | Physician signature |
| Q10UDt | date |  |  | SI | Physician signature Last Updated Date |
| Q10UTm | time |  |  | SI | Physician signature Last Updated Time |
| Q11 | date |  |  | SI | Date |
| Q12 | time |  |  | SI | Time |
| Q13 | varchar |  |  | SI | Physician's name |
| Q14 | varchar |  |  | SI | Score |
| Q15 | varchar |  |  | SI | Classification |
| Q16 | varchar |  |  | SI | 0 - 4 |
| Q17 | varchar |  |  | SI | Easy intubation |
| Q18 | varchar |  |  | SI | ≥ 5 |
| Q19 | varchar |  |  | SI | Suspected to be difficult intubation |
| Q20 | varchar |  |  | SI | 0 - 4: Easy intubation |
| Q21 | varchar |  |  | SI | ≥ 5: Suspected to be difficult intubation |
| Q22 | varchar |  |  | SI | MACOCHA scoring tool provides a provision to predi... |
| Q23 | varchar |  |  | SI | The Mallampati Score |
| Q24 | varchar |  |  | SI | Complete visualization of the soft palate |
| Q25 | varchar |  |  | SI | Complete visualization of the uvula |
| Q26 | varchar |  |  | SI | Visualization of only the base of the uvula |
| Q27 | varchar |  |  | SI | Soft palate is not visible at all |
| Q28 | varchar |  |  | SI | Class 1 |
| Q29 | varchar |  |  | SI | Class 2 |
| Q30 | varchar |  |  | SI | Class 3 |
| Q31 | varchar |  |  | SI | Class 4 |
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