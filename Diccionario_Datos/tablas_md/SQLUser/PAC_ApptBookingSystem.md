# SQLUser.PAC_ApptBookingSystem

**Schema:** SQLUser
**Columnas:** 93
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| APPTBS_RowId | bigint | PK |  | NO | - |
| APPTBS_Code | varchar |  |  | NO | Code |
| APPTBS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| APPTBS_CreatedDate | date |  |  | SI | Created Date |
| APPTBS_CreatedTime | time |  |  | SI | Created Time |
| APPTBS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| APPTBS_DateFrom | date |  |  | SI | Date From |
| APPTBS_DateTo | date |  |  | SI | Date To |
| APPTBS_Desc | varchar |  |  | NO | Description |
| APPTBS_NationalCode | varchar |  |  | SI | National Code |
| APPTBS_Owner | varchar |  |  | SI | Owner |
| APPTBS_UpdatedDate | date |  |  | SI | Updated Date |
| APPTBS_UpdatedTime | time |  |  | SI | Updated Time |
| APPTBS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Procedure type	 |
| Q02 | - |  |  | SI | Lead details |
| Q03 | - |  |  | SI | Venous approach right atrium |
| Q04 | - |  |  | SI | Right atrium |
| Q05 | - |  |  | SI | Pacing system analyzer |
| Q06 | - |  |  | SI | Device |
| Q07 | - |  |  | SI | Threshold (mV) |
| Q08 | - |  |  | SI | P-wave (mV) |
| Q09 | - |  |  | SI | Slew rate (volts/second) |
| Q10 | - |  |  | SI | Impedance (Ohm) |
| Q11 | - |  |  | SI | Device threshold |
| Q12 | - |  |  | SI | Device P-wave |
| Q13 | - |  |  | SI | Device slew rate |
| Q14 | - |  |  | SI | Device impedance |
| Q15 | - |  |  | SI | Venous approach Right Ventricle (RV) |
| Q16 | - |  |  | SI | Right ventricle |
| Q17 | - |  |  | SI | Pacing system analyzer |
| Q18 | - |  |  | SI | Device |
| Q19 | - |  |  | SI | Threshold (mV) |
| Q20 | - |  |  | SI | P-wave (mV) |
| Q21 | - |  |  | SI | Slew rate (volts/second) |
| Q22 | - |  |  | SI | Impedance (Ohm) |
| Q23 | - |  |  | SI | Device threshold |
| Q24 | - |  |  | SI | Device P-wave |
| Q25 | - |  |  | SI | Device slew rate |
| Q26 | - |  |  | SI | Device impedance |
| Q27 | - |  |  | SI | Venous approach Left Ventricle (LV) |
| Q28 | - |  |  | SI | Left ventricle |
| Q29 | - |  |  | SI | Pacing system analyzer |
| Q30 | - |  |  | SI | Device |
| Q31 | - |  |  | SI | Threshold (mv) |
| Q32 | - |  |  | SI | P-wave (mv) |
| Q33 | - |  |  | SI | Slew rate (v/s) |
| Q34 | - |  |  | SI | Impedance (ohm) |
| Q35 | - |  |  | SI | Device threshold |
| Q36 | - |  |  | SI | Device P-wave |
| Q37 | - |  |  | SI | Device slew rate |
| Q38 | - |  |  | SI | Device impedance |
| Q39 | - |  |  | SI | Comments / Issues |
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