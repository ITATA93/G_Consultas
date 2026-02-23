# questionnaire.QTCSSIPBS

> Surgical Site Infection Prevention Bundle Score

**Schema:** questionnaire
**Columnas:** 74
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Surgical Site Infection Prevention Bundle Score

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Bundle Compliance Percentage |
| Q04 | varchar |  |  | SI | % |
| Q05 | varchar |  |  | SI | Surgical Procedure |
| Q06 | varchar |  |  | SI | Booked Procedure |
| Q07 | varchar |  |  | SI | Actual procedure |
| Q08 | date |  |  | SI | Date of procedure |
| Q09 | varchar |  |  | SI | Name of surgeon |
| Q10 | varchar |  |  | SI | Theatre N°: |
| Q11 | time |  |  | SI | Time of procedure: from |
| Q12 | time |  |  | SI | To |
| Q13 | varchar |  |  | SI | For high-risk orthopedic or cardiothoracic interve... |
| Q14 | varchar |  |  | SI | Bath taken night prior to surgery or on the day of... |
| Q15 | varchar |  |  | SI | Trichotomy not practiced |
| Q16 | varchar |  |  | SI | If performed trichotomy: used the electric razor (... |
| Q17 | varchar |  |  | SI | If performed trichotomy: performed shortly before ... |
| Q18 | varchar |  |  | SI | Antibiotic prophylaxis within 30-60 minutes prior ... |
| Q19 | varchar |  |  | SI | Single dose antibiotic prophylaxis, except in prot... |
| Q20 | varchar |  |  | SI | Skin antisepsis with 2% chlorhexidine in 70% alcoh... |
| Q21 | varchar |  |  | SI | Peri-operative normothermia (> 36 ° C) (possibly a... |
| Q22 | varchar |  |  | SI | Peri-operative High blood glucose test result |
| Q23 | varchar |  |  | SI | Sterile dressing not handled / removed for the fir... |
| Q24 | varchar |  |  | SI | Comments |
| Q25 | varchar |  |  | SI | Score |
| Q26 | varchar |  |  | SI | Classification |
| Q27 | varchar |  |  | SI | 0 - 100: |
| Q28 | varchar |  |  | SI | Higher percetage indicates higher compliance |
| Q29 | varchar |  |  | SI | This questionnaire is used in the clinical practic... |
| Q30 | varchar |  |  | SI | 0 - 100: Higher percetage indicates higher complia... |
| Q31 | varchar |  |  | SI | Aseptic technique for wound dressing |
| Q32 | varchar |  |  | SI | If performed trichotomy: this has been done outsid... |
| Q33 | varchar |  |  | SI | If performed trichotomy: this has been done outsid... |
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