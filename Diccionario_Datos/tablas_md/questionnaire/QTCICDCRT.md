# questionnaire.QTCICDCRT

> Implantable Cardioverter Defibrillators/Cardiac Resynchronization Therapy

**Schema:** questionnaire
**Columnas:** 80
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Implantable Cardioverter Defibrillators/Cardiac Resynchronization Therapy

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Procedure type	 |
| Q02 | varchar |  |  | SI | Lead details |
| Q03 | varchar |  |  | SI | Venous approach right atrium |
| Q04 | varchar |  |  | SI | Right atrium |
| Q05 | varchar |  |  | SI | Pacing system analyzer |
| Q06 | varchar |  |  | SI | Device |
| Q07 | numeric |  |  | SI | Threshold (mV) |
| Q08 | numeric |  |  | SI | P-wave (mV) |
| Q09 | numeric |  |  | SI | Slew rate (volts/second) |
| Q10 | numeric |  |  | SI | Impedance (Ohm) |
| Q11 | varchar |  |  | SI | Device threshold |
| Q12 | varchar |  |  | SI | Device P-wave |
| Q13 | varchar |  |  | SI | Device slew rate |
| Q14 | varchar |  |  | SI | Device impedance |
| Q15 | varchar |  |  | SI | Venous approach Right Ventricle (RV) |
| Q16 | varchar |  |  | SI | Right ventricle |
| Q17 | varchar |  |  | SI | Pacing system analyzer |
| Q18 | varchar |  |  | SI | Device |
| Q19 | numeric |  |  | SI | Threshold (mV) |
| Q20 | numeric |  |  | SI | P-wave (mV) |
| Q21 | numeric |  |  | SI | Slew rate (volts/second) |
| Q22 | numeric |  |  | SI | Impedance (Ohm) |
| Q23 | varchar |  |  | SI | Device threshold |
| Q24 | varchar |  |  | SI | Device P-wave |
| Q25 | varchar |  |  | SI | Device slew rate |
| Q26 | varchar |  |  | SI | Device impedance |
| Q27 | varchar |  |  | SI | Venous approach Left Ventricle (LV) |
| Q28 | varchar |  |  | SI | Left ventricle |
| Q29 | varchar |  |  | SI | Pacing system analyzer |
| Q30 | varchar |  |  | SI | Device |
| Q31 | numeric |  |  | SI | Threshold (mv) |
| Q32 | numeric |  |  | SI | P-wave (mv) |
| Q33 | numeric |  |  | SI | Slew rate (v/s) |
| Q34 | numeric |  |  | SI | Impedance (ohm) |
| Q35 | varchar |  |  | SI | Device threshold |
| Q36 | varchar |  |  | SI | Device P-wave |
| Q37 | varchar |  |  | SI | Device slew rate |
| Q38 | varchar |  |  | SI | Device impedance |
| Q39 | varchar |  |  | SI | Comments / Issues |
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