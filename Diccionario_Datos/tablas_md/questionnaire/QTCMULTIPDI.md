# questionnaire.QTCMULTIPDI

> Multiple Pregnancy Place, Timing and Mode of Delivery

**Schema:** questionnaire
**Columnas:** 78
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Multiple Pregnancy Place, Timing and Mode of Delivery

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Have the following topics been discussed?	 |
| Q02 | varchar |  |  | SI | More likely to have your babies earlier	 |
| Q03 | varchar |  |  | SI | Dichorionic / Diamniotic aim for delivery after 37... |
| Q04 | varchar |  |  | SI | Monochorionic / Diamniotic aim for delivery after ... |
| Q05 | varchar |  |  | SI | Monochorionic / Monoamniotic aim for delivery at 3... |
| Q06 | varchar |  |  | SI | Notes	 |
| Q07 | varchar |  |  | SI | Vaginal birth is usual if twin 1 is cephalic (Dich... |
| Q08 | varchar |  |  | SI | Continuous monitoring during labour	 |
| Q09 | varchar |  |  | SI | Twin 1 may have Fetal Scalp Electrode applied	 |
| Q10 | varchar |  |  | SI | Procedure following birth of Twin 1	 |
| Q11 | varchar |  |  | SI | Twin 2 non-cephalic complex interventions may be r... |
| Q12 | varchar |  |  | SI | Risk of Caesarean section if twin 2 is small (<3%)... |
| Q13 | varchar |  |  | SI | Notes |
| Q14 | varchar |  |  | SI | Elective Caesarean section  for Twin 1 Breech	 |
| Q15 | varchar |  |  | SI | Elective Caesarean section  for Twin 1 Placenta Pr... |
| Q16 | varchar |  |  | SI | Elective Caesarean section  - Maternal choice	 |
| Q17 | varchar |  |  | SI | Notes |
| Q18 | varchar |  |  | SI | Risk of bleeding	 |
| Q19 | varchar |  |  | SI | Risk of bladder damage	 |
| Q20 | varchar |  |  | SI | Risk of wound infection	 |
| Q21 | varchar |  |  | SI | Risk of thrombosis	 |
| Q22 | varchar |  |  | SI | Longer hospital stay may be required	 |
| Q23 | varchar |  |  | SI | Babies may have 'wet lung' and require special car... |
| Q24 | varchar |  |  | SI | Longer recovery and driving restrictions	 |
| Q25 | varchar |  |  | SI | May affect future birth options	 |
| Q26 | varchar |  |  | SI | Can make breast feeding more difficult	 |
| Q27 | varchar |  |  | SI | May avoid complex delivery of Twin 2 if not cephal... |
| Q28 | varchar |  |  | SI | Avoids Emergency Caesarean section which may occur... |
| Q29 | varchar |  |  | SI | Notes |
| Q30 | varchar |  |  | SI | Pain relief in labour leaflet given	 |
| Q31 | varchar |  |  | SI | Epidural anaesthesia discussed	 |
| Q32 | varchar |  |  | SI | Notes |
| Q33 | varchar |  |  | SI | Advised re: number of health professionals present... |
| Q34 | varchar |  |  | SI | Increase risk of admission to Neonatal Unit	 |
| Q35 | varchar |  |  | SI | Preferred mode of birth	 |
| Q36 | varchar |  |  | SI | Contingency Plan	 |
| Q37 | varchar |  |  | SI | Notes	 |
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