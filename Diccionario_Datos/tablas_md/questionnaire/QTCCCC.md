# questionnaire.QTCCCC

> Clinical Imaging Consent

**Schema:** questionnaire
**Columnas:** 67
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Clinical Imaging Consent

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Photographed / audio-video recorded	 |
| Q02 | varchar |  |  | SI | And/or study models of mouth being taken	 |
| Q03 | varchar |  |  | SI | Clinical management	 |
| Q04 | varchar |  |  | SI | Education |
| Q05 | varchar |  |  | SI | Publication & research	 |
| Q06 | varchar |  |  | SI | Other	 |
| Q07 | varchar |  |  | SI | Health professional to specify	 |
| Q08 | longvarbinary |  |  | SI | Signature	 |
| Q08UDt | date |  |  | SI | Signature	 Last Updated Date |
| Q08UTm | time |  |  | SI | Signature	 Last Updated Time |
| Q09 | varchar |  |  | SI | They may be used to help plan and evaluate care, c... |
| Q10 | varchar |  |  | SI | The images will form part of your confidential med... |
| Q11 | varchar |  |  | SI | Images may also be seen by health professionals fo... |
| Q12 | varchar |  |  | SI |  They may be used during talks, conference present... |
| Q13 | varchar |  |  | SI | This may involve images being used, for example in... |
| Q14 | varchar |  |  | SI | Images will be seen by health professionals who ac... |
| Q15 | varchar |  |  | SI | They may also be seen by the general public. All i... |
| Q16 | varchar |  |  | SI | I have been given the opportunity to ask questions... |
| Q17 | varchar |  |  | SI | I consent to myself / patient listed above being |
| Q18 | varchar |  |  | SI | For the purposes of: |
| Q19 | varchar |  |  | SI | Name of person signing (if not the patient) |
| Q20 | varchar |  |  | SI | Relationship to patient |
| Q21 | varchar |  |  | SI | Reason patient unable to sign |
| Q22 | date |  |  | SI | Date |
| Q23 | time |  |  | SI | Time |
| Q24 | varchar |  |  | SI | Images will only be seen by treating health profes... |
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