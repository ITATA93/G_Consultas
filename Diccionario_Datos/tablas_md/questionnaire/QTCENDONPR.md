# questionnaire.QTCENDONPR

> Endoscopy Nursing Procedure Report

**Schema:** questionnaire
**Columnas:** 94
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Endoscopy Nursing Procedure Report

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Procedure type |
| Q04 | varchar |  |  | SI | Intravascular access established |
| Q05 | varchar |  |  | SI | Sedation method |
| Q06 | time |  |  | SI | Xylocaine throat spray time given |
| Q07 | varchar |  |  | SI | Procedure preparation comments |
| Q08 | varchar |  |  | SI | Rectal examination |
| Q09 | varchar |  |  | SI | Haemorrhoid treatment |
| Q11 | date |  |  | SI | Gastroscopy start date / time |
| Q12 | time |  |  | SI | Gastroscopy start time |
| Q13 | date |  |  | SI | Gastroscopy finish date / time |
| Q14 | time |  |  | SI | Gastroscopy finish |
| Q15 | date |  |  | SI | Lower endoscopy start date / time |
| Q16 | time |  |  | SI | Lower endoscopy start time |
| Q17 | date |  |  | SI | Lower endoscopy finish date / time |
| Q18 | time |  |  | SI | Lower endoscopy finish |
| Q19 | date |  |  | SI | Procedure start date / time |
| Q20 | time |  |  | SI | Procedure start time |
| Q21 | date |  |  | SI | Procedure end date / time |
| Q22 | time |  |  | SI | Procedure end time |
| Q24 | varchar |  |  | SI | Colonoscope advanced to |
| Q25 | varchar |  |  | SI | Reason for not reaching caecum |
| Q26 | varchar |  |  | SI | Colonoscope progression assistance |
| Q27 | numeric |  |  | SI | Withdrawal time (in minutes) |
| Q30 | varchar |  |  | SI | Biopsy(s) taken |
| Q31 | varchar |  |  | SI | Biopsy details |
| Q32 | varchar |  |  | SI | Diathermy used |
| Q33 | varchar |  |  | SI | Diathermy site |
| Q34 | varchar |  |  | SI | Procedural photos captured |
| Q35 | varchar |  |  | SI | Sphincterotomy performed |
| Q36 | varchar |  |  | SI | Lithotripsy |
| Q37 | varchar |  |  | SI | Bile duct stent inserted |
| Q39 | varchar |  |  | SI | Procedure comments |
| Q40 | varchar |  |  | SI | Diathermy pads removed |
| Q41 | time |  |  | SI | Fully awake time |
| Q42 | varchar |  |  | SI | Post procedure comments |
| Q43 | varchar |  |  | SI | Boston Bowel Preparation Score |
| Q45 | varchar |  |  | SI | BBPS, Left Colon |
| Q45ObsDR | varchar |  | FK | SI | BBPS, Left Colon DR |
| Q46 | varchar |  |  | SI | BBPS, Right Colon |
| Q46ObsDR | varchar |  | FK | SI | BBPS, Right Colon DR |
| Q47 | varchar |  |  | SI | BBPS, Transverse Colon |
| Q47ObsDR | varchar |  | FK | SI | BBPS, Transverse Colon DR |
| Q48 | varchar |  |  | SI | Reference: Lai EJ, Calderwood AH, Doros G, Fix OK,... |
| Q49 | varchar |  |  | SI | Gastrointest Endosc 2009;69:620-625. doi:10.1016/j... |
| Q50 | varchar |  |  | SI | Gastroscopy Specimens & Interventions |
| Q51 | varchar |  |  | SI | Gastroscopy Specimens & Interventions |
| Q52 | varchar |  |  | SI | Lower Endoscopy Specimens & Interventions |
| Q53 | varchar |  |  | SI | Lower Endoscopy Specimens & Interventions |
| Q54 | varchar |  |  | SI | Lower Endoscopy Specimens & Interventions |
| Q55 | varchar |  |  | SI | Lower Endoscopy Specimens & Interventions |
| Q57 | varchar |  |  | SI | Scope Guide Used |
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