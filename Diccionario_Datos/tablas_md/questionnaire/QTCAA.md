# questionnaire.QTCAA

> Ascites Assessment

**Schema:** questionnaire
**Columnas:** 67
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Ascites Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Is the patient receiving anticoagulants? |
| Q02 | varchar |  |  | SI | Ensure this is documented on Medications chart |
| Q03 | varchar |  |  | SI | Current Treatment	 |
| Q04 | varchar |  |  | SI | Problems with Appetite 	 |
| Q05 | varchar |  |  | SI | Issues / Concerns 	 |
| Q06 | varchar |  |  | SI | Problems with Breathlessness |
| Q07 | varchar |  |  | SI | Issues / Concerns 	 |
| Q08 | varchar |  |  | SI | Problems with Bowels / Urine	 |
| Q09 | varchar |  |  | SI | Issues / Concerns 	 |
| Q10 | varchar |  |  | SI | Problems with Nausea and Vomiting |
| Q11 | varchar |  |  | SI | Issues / Concerns  |
| Q12 | varchar |  |  | SI | Problems with Pain |
| Q13 | varchar |  |  | SI | Issues / Concerns |
| Q14 | varchar |  |  | SI | Problems with Sleep |
| Q15 | varchar |  |  | SI | Issues / Concerns 	 |
| Q16 | varchar |  |  | SI | Problems with Fatigue |
| Q17 | varchar |  |  | SI | Issues / Concerns |
| Q18 | varchar |  |  | SI | General Assessment / Key Concerns	 |
| Q19 | varchar |  |  | SI | Document patients understanding of Ascites	 |
| Q20 | varchar |  |  | SI | Date of Admission 	 |
| Q21 | varchar |  |  | SI | Reason for Admission	 |
| Q22 | varchar |  |  | SI | Plan |
| Q23 | varchar |  |  | SI | Home Circumstances 	 |
| Q24 | varchar |  |  | SI | Support At Home  |
| Q25 | varchar |  |  | SI | Key Concerns	 |
| Q26 | varchar |  |  | SI | Referrals needed	 |
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