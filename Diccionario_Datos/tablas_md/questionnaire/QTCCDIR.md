# questionnaire.QTCCDIR

> Cardiac Device Interrogation Report

**Schema:** questionnaire
**Columnas:** 110
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Cardiac Device Interrogation Report

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Reason for follow-up |
| Q04 | varchar |  |  | SI | Other reason for follow up details |
| Q05 | varchar |  |  | SI | Device |
| Q06 | varchar |  |  | SI | Device model |
| Q07 | varchar |  |  | SI | Presenting rhythm |
| Q08 | numeric |  |  | SI | Rate (bpm) |
| Q09 | varchar |  |  | SI | Underlying rhythm |
| Q10 | numeric |  |  | SI | Total atrial paced (%) |
| Q11 | numeric |  |  | SI | Total ventricular paced (%) |
| Q12 | numeric |  |  | SI | Biventricular paced (%) |
| Q13 | numeric |  |  | SI | Left ventricular paced (%) |
| Q14 | numeric |  |  | SI | Atrial tachycardia / Atrial fibrillation burden (%... |
| Q15 | varchar |  |  | SI | Model |
| Q16 | numeric |  |  | SI | Lower rate |
| Q17 | varchar |  |  | SI | Paced atrioventricular / Sensed atrioventricular |
| Q18 | varchar |  |  | SI | Cardiac resynchronisation therapy pacemaker (Adapt... |
| Q19 | numeric |  |  | SI | Battery voltage (V) |
| Q20 | numeric |  |  | SI | Last charge time (sec) |
| Q21 | varchar |  |  | SI | Remaining longevity estimate * |
| Q22 | varchar |  |  | SI | Lead measurements |
| Q23 | varchar |  |  | SI | Atrium |
| Q24 | varchar |  |  | SI | Right ventricle |
| Q25 | varchar |  |  | SI | Left ventricle |
| Q26 | varchar |  |  | SI | Sensing value |
| Q27 | varchar |  |  | SI | Pacing threshold |
| Q28 | varchar |  |  | SI | Impedance |
| Q29 | numeric |  |  | SI | Sensing value (mV) - Atrium |
| Q30 | numeric |  |  | SI | Sensing value (mV) - RV |
| Q31 | numeric |  |  | SI | Pacing threshold (V) - Atrium |
| Q32 | numeric |  |  | SI | Pacing threshold (V) - RV |
| Q33 | numeric |  |  | SI | Pacing threshold (V) - LV |
| Q34 | varchar |  |  | SI | V@ |
| Q35 | varchar |  |  | SI | V@ |
| Q36 | varchar |  |  | SI | V@ |
| Q37 | numeric |  |  | SI | Pacing threshold (ms) - Atrium |
| Q38 | numeric |  |  | SI | Pacing threshold (ms) - RV |
| Q39 | numeric |  |  | SI | Pacing threshold (ms) - LV |
| Q40 | varchar |  |  | SI | ms |
| Q41 | varchar |  |  | SI | ms |
| Q42 | varchar |  |  | SI | ms |
| Q43 | numeric |  |  | SI | Impedance (Ω) - Atrium |
| Q44 | numeric |  |  | SI | Impedance (Ω) - RV |
| Q45 | numeric |  |  | SI | Impedance (Ω) - LV |
| Q46 | numeric |  |  | SI | RV Defib |
| Q47 | numeric |  |  | SI | SVC Defib |
| Q48 | varchar |  |  | SI | Ω |
| Q49 | varchar |  |  | SI | Ω |
| Q50 | numeric |  |  | SI | LV pace polarity |
| Q51 | varchar |  |  | SI | Findings / Events |
| Q52 | varchar |  |  | SI | Programming changes |
| Q53 | varchar |  |  | SI | Sensing value	- Atrium |
| Q54 | varchar |  |  | SI | Pacing threshold - Atrium |
| Q55 | varchar |  |  | SI | Impedance - Atrium |
| Q56 | varchar |  |  | SI | Ω |
| Q57 | varchar |  |  | SI | Ω |
| Q58 | varchar |  |  | SI | Ω |
| Q59 | varchar |  |  | SI | Sensing value - Right ventricle |
| Q60 | varchar |  |  | SI | Pacing threshold - Right ventricle |
| Q61 | varchar |  |  | SI | Impedance - Right ventricle |
| Q62 | varchar |  |  | SI | Pacing threshold - Left ventricle |
| Q63 | varchar |  |  | SI | Impedance - Left ventricle |
| Q64 | varchar |  |  | SI | Right ventricle |
| Q65 | varchar |  |  | SI | Right ventricle |
| Q66 | varchar |  |  | SI | Left ventricle |
| Q67 | varchar |  |  | SI | mV |
| Q68 | varchar |  |  | SI | mV |
| Q69 | varchar |  |  | SI | LV pace polarity |
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