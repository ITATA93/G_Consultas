# questionnaire.QTCDTF

> Dialysis Treatment Form

**Schema:** questionnaire
**Columnas:** 79
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Dialysis Treatment Form

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Type of dialysis |
| Q02 | varchar |  |  | SI | Haemodiafiltration type |
| Q03 | numeric |  |  | SI | Session No |
| Q04 | varchar |  |  | SI | Machine |
| Q05 | varchar |  |  | SI | Machine No. |
| Q06 | numeric |  |  | SI | Treatment duration (hours) |
| Q07 | varchar |  |  | SI | Dialyzer |
| Q08 | varchar |  |  | SI | Dialysate bath |
| Q09 | numeric |  |  | SI | Dialysate concentrate - Sodium (NA) (mmol/L) |
| Q10 | numeric |  |  | SI | Dialysate concentrate - Potassium (K) (mmol/L) |
| Q11 | numeric |  |  | SI | Dialysate concentrate - Calcium (CA) (mmol/L) |
| Q12 | numeric |  |  | SI | Dialysate concentrate - Bicarbonate (HCO3) (mmol/L... |
| Q13 | numeric |  |  | SI | Dialysate fluid temperature (C) |
| Q14 | varchar |  |  | SI | Ultra filtration profile |
| Q15 | varchar |  |  | SI | Mode |
| Q16 | varchar |  |  | SI | Sodium (Na) profile |
| Q17 | numeric |  |  | SI | Start value (mmol/L) |
| Q18 | numeric |  |  | SI | End value (mmol/L) |
| Q19 | numeric |  |  | SI | Duration (hours) |
| Q20 | varchar |  |  | SI | Bicarbonate (HCO3) profile |
| Q21 | numeric |  |  | SI | Start value (mmol/L) |
| Q22 | numeric |  |  | SI | End value (mmol/L) |
| Q23 | numeric |  |  | SI | Duration (hours) |
| Q24 | varchar |  |  | SI | Isolated ultrafiltration |
| Q25 | numeric |  |  | SI | Isolated ultrafiltration volume (L) |
| Q26 | numeric |  |  | SI | Duration (hours) |
| Q28 | varchar |  |  | SI | Vascular access |
| Q28ObsDR | varchar |  | FK | SI | Vascular access DR |
| Q29 | varchar |  |  | SI | Access site location |
| Q30 | varchar |  |  | SI | Catheter locking solution (if permanent / temporar... |
| Q31 | varchar |  |  | SI | Dialysis needle size |
| Q31ObsDR | varchar |  | FK | SI | Dialysis needle size DR |
| Q32 | numeric |  |  | SI | Arterial volume (ml) |
| Q33 | numeric |  |  | SI | Venous volume (ml) |
| Q34 | varchar |  |  | SI | Dialysis treatment comments |
| Q35 | date |  |  | SI | Date |
| Q36 | time |  |  | SI | Time |
| Q37 | varchar |  |  | SI | Access site location |
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