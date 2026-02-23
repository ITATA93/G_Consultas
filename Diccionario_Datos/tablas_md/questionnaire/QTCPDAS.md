# questionnaire.QTCPDAS

> Peritoneal Dialysis (PD) Assessment Sheet

**Schema:** questionnaire
**Columnas:** 73
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Peritoneal Dialysis (PD) Assessment Sheet

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | date |  |  | SI | Date of starting Peritoneal Dialysis (PD) |
| Q04 | varchar |  |  | SI | Type of dialysis |
| Q05 | numeric |  |  | SI | Number of exchanges |
| Q06 | numeric |  |  | SI | Total volume (ml) |
| Q07 | varchar |  |  | SI | Type of PD solutions |
| Q08 | varchar |  |  | SI | Type |
| Q09 | numeric |  |  | SI | Total volume (ml) |
| Q10 | varchar |  |  | SI | If on tidal specify % |
| Q11 | varchar |  |  | SI | Duration of night therapy |
| Q12 | numeric |  |  | SI | Number of night cycles |
| Q13 | numeric |  |  | SI | Total volume (ml) |
| Q14 | varchar |  |  | SI | Volume / solution of last fill |
| Q15 | varchar |  |  | SI | Volume / solution of day exchange (if applicable) |
| Q17 | varchar |  |  | SI | PD: compliance |
| Q18 | varchar |  |  | SI | If compliance poor (specify) |
| Q19 | varchar |  |  | SI | PD: bowel movements |
| Q20 | varchar |  |  | SI | If bowel movements Poor (specify) |
| Q21 | varchar |  |  | SI | PD: catheter status |
| Q22 | varchar |  |  | SI | PD: catheter dressing |
| Q23 | varchar |  |  | SI | If catheter dressing wet and dirty (describe) |
| Q24 | varchar |  |  | SI | PD: titanium adapter |
| Q25 | varchar |  |  | SI | If titanium adapter poor (specify) |
| Q26 | varchar |  |  | SI | Symptoms of peritonitis |
| Q27 | varchar |  |  | SI | If peritonitis present (describe) |
| Q28 | varchar |  |  | SI | PD: extension set well maintained |
| Q29 | date |  |  | SI | PD: extension set last time changed |
| Q30 | varchar |  |  | SI | PD: extension set poor |
| Q31 | varchar |  |  | SI | PD: exit site |
| Q33 | varchar |  |  | SI | Comments |
| Q34 | varchar |  |  | SI | If catheter dressing wet and dirty (describe) |
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