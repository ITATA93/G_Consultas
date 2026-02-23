# questionnaire.QTCCDPREV

> Cardiac Device/Pacemaker Review

**Schema:** questionnaire
**Columnas:** 79
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Cardiac Device/Pacemaker Review

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Device |
| Q02 | date |  |  | SI | Clinic date	 |
| Q03 | date |  |  | SI | Date implant inserted	 |
| Q04 | varchar |  |  | SI | Device manufacturer |
| Q05 | varchar |  |  | SI | Device manufacturer  |
| Q06 | varchar |  |  | SI | Medtronic (Pacemaker) |
| Q07 | varchar |  |  | SI | Medtronic (ILR)	 |
| Q08 | varchar |  |  | SI | ELA Sorin	 |
| Q09 | varchar |  |  | SI | Boston Scientific	 |
| Q10 | varchar |  |  | SI | St Jude Medical	 |
| Q11 | varchar |  |  | SI | Biotronic	 |
| Q12 | varchar |  |  | SI | Vitatron |
| Q13 | varchar |  |  | SI | Model or type (Pacemaker)	 |
| Q14 | varchar |  |  | SI | Model or type (ILR)	 |
| Q15 | varchar |  |  | SI | Mode (Single)	 |
| Q16 | varchar |  |  | SI | Mode (Dual)	 |
| Q17 | numeric |  |  | SI | Base rate	 |
| Q18 | numeric |  |  | SI | Magnet rate	 |
| Q19 | numeric |  |  | SI | Threshold A =	 |
| Q20 | numeric |  |  | SI | A=XV@ 	 |
| Q21 | numeric |  |  | SI | Threshold V =	 |
| Q22 | numeric |  |  | SI | V=XV@	 |
| Q23 | numeric |  |  | SI | Sensing P =	 |
| Q24 | numeric |  |  | SI | R=	 |
| Q25 | numeric |  |  | SI | Impedance A =	 |
| Q26 | numeric |  |  | SI | V=	 |
| Q27 | varchar |  |  | SI | Notes |
| Q28 | varchar |  |  | SI | ( please include wound appearance, high rates, any... |
| Q29 | varchar |  |  | SI | (30-180 bpm) |
| Q30 | varchar |  |  | SI | (70-110 bpm) |
| Q31 | varchar |  |  | SI | (0-20 V) |
| Q32 | varchar |  |  | SI | (0-5 MS) |
| Q33 | varchar |  |  | SI | (0-20 V)	 |
| Q34 | varchar |  |  | SI | (0-5 MS) |
| Q35 | varchar |  |  | SI | (0-20 mV) |
| Q36 | varchar |  |  | SI | (0-60 mV) |
| Q37 | varchar |  |  | SI | (0-3500 ohms) |
| Q38 | varchar |  |  | SI | (0-3500 ohms) |
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