# questionnaire.QTCCCDV

> "Critical Care Death Verification	"

**Schema:** questionnaire
**Columnas:** 81
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* "Critical Care Death Verification	"

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Were any treatments withheld from this patient	 |
| Q02 | varchar |  |  | SI | Was treatment withdrawn from this patient?	 |
| Q03 | varchar |  |  | SI | Was there a discussion with the family prior to wi... |
| Q04 | varchar |  |  | SI | Treatment discussion withdrawal lead by	 |
| Q05 | date |  |  | SI | Date of withdrawal	 |
| Q06 | time |  |  | SI | Time of withdrawal	 |
| Q07 | varchar |  |  | SI | Was there a Brainstem death test?	 |
| Q08 | varchar |  |  | SI | Was a SNOD referral undertaken?	 |
| Q09 | varchar |  |  | SI | If so by whom?	 |
| Q10 | varchar |  |  | SI | Note |
| Q11 | varchar |  |  | SI | Is the patient unconscious	 |
| Q12 | varchar |  |  | SI | Is there a response to supra orbital pressure	 |
| Q13 | varchar |  |  | SI | Is there a carotid pulse?	 |
| Q14 | varchar |  |  | SI | Are  heart sounds audible on ausciltation	 |
| Q15 | varchar |  |  | SI | Is there respiratory effort	 |
| Q16 | varchar |  |  | SI | Are breath sounds audible on ausciltation	 |
| Q17 | varchar |  |  | SI | Do the pupils react to light	 |
| Q18 | varchar |  |  | SI | Have you observed the above parameters for 5 minut... |
| Q19 | date |  |  | SI | Date of death 	 |
| Q20 | time |  |  | SI | Time of Death	 |
| Q21 | varchar |  |  | SI | Name of verifying Doctor	 |
| Q22 | varchar |  |  | SI | Grade |
| Q23 | numeric |  |  | SI | GMC number	 |
| Q24 | varchar |  |  | SI | Note |
| Q25 | varchar |  |  | SI | Systolic |
| Q25ObsDR | varchar |  | FK | SI | Systolic DR |
| Q26 | varchar |  |  | SI | Pulse |
| Q26ObsDR | varchar |  | FK | SI | Pulse DR |
| Q27 | varchar |  |  | SI | Note |
| Q28 | date |  |  | SI | Date From	 |
| Q29 | date |  |  | SI | Date To	 |
| Q30 | varchar |  |  | SI | Title |
| Q31 | varchar |  |  | SI | Surname |
| Q32 | varchar |  |  | SI | Forename |
| Q33 | varchar |  |  | SI | Other Name	 |
| Q34 | date |  |  | SI | Date of Birth	 |
| Q35 | varchar |  |  | SI | Professional Registration Issuer	 |
| Q36 | numeric |  |  | SI | Professional Body Registration	 |
| Q37 | varchar |  |  | SI | Diastolic |
| Q37ObsDR | varchar |  | FK | SI | Diastolic DR |
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