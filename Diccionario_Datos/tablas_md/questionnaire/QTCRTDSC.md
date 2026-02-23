# questionnaire.QTCRTDSC

> Respiratory Therapy Device and Safety Checks

**Schema:** questionnaire
**Columnas:** 79
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Respiratory Therapy Device and Safety Checks

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Ventilation Day |
| Q03ObsDR | varchar |  | FK | SI | Ventilation Day DR |
| Q04 | varchar |  |  | SI | Total Invasive Ventilation Days |
| Q04ObsDR | varchar |  | FK | SI | Total Invasive Ventilation Days DR |
| Q05 | varchar |  |  | SI | Total Non Invasive Ventilation Days |
| Q05ObsDR | varchar |  | FK | SI | Total Non Invasive Ventilation Days DR |
| Q06 | varchar |  |  | SI | Devices present and functioning at time of assessm... |
| Q07 | date |  |  | SI | Aerosol Set-up Date |
| Q08 | date |  |  | SI | Bacteria Filter |
| Q09 | date |  |  | SI | Heat and Moisture Exchanger |
| Q10 | date |  |  | SI | In Line Suction Catheter |
| Q11 | date |  |  | SI | Ventilator Circuit |
| Q12 | date |  |  | SI | Bag Valve Mask |
| Q13 | varchar |  |  | SI | Endotracheal Tube retie / retape date |
| Q13ObsDR | varchar |  | FK | SI | Endotracheal Tube retie / retape date DR |
| Q14 | varchar |  |  | SI | Endotracheal Tube retie / retape time |
| Q14ObsDR | varchar |  | FK | SI | Endotracheal Tube retie / retape time DR |
| Q15 | varchar |  |  | SI | Endotracheal Tube Position |
| Q15ObsDR | varchar |  | FK | SI | Endotracheal Tube Position DR |
| Q16 | varchar |  |  | SI | Endotracheal Tube Position on XRAY |
| Q16ObsDR | varchar |  | FK | SI | Endotracheal Tube Position on XRAY DR |
| Q17 | varchar |  |  | SI | Date of Endotracheal Tube Xray |
| Q17ObsDR | varchar |  | FK | SI | Date of Endotracheal Tube Xray DR |
| Q18 | numeric |  |  | SI | Airway above carina (cm) |
| Q19 | varchar |  |  | SI | Adjusted by |
| Q20 | numeric |  |  | SI | If Pushed / Pulled, how much adjusted? (cm) |
| Q21 | varchar |  |  | SI | Lip Condition |
| Q22 | varchar |  |  | SI | Pressure on nasal bridge |
| Q23 | varchar |  |  | SI | Pressure on nostril or septum |
| Q24 | varchar |  |  | SI | Pressure on forehead |
| Q25 | varchar |  |  | SI | Airway security |
| Q26 | varchar |  |  | SI | Respiratory Therapy Checks completed |
| Q27 | varchar |  |  | SI |  Patient's appearance |
| Q28 | varchar |  |  | SI | Sedation / Paralysis |
| Q29 | varchar |  |  | SI | Cardiopulmonary Support |
| Q30 | varchar |  |  | SI | RT Device and Safety Check Comments  |
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