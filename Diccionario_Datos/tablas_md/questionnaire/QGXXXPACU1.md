# questionnaire.QGXXXPACU1

> PACU-Record

**Schema:** questionnaire
**Columnas:** 84
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* PACU-Record

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q13 | bit |  |  | SI | Cooling device |
| Q14 | varchar |  |  | SI | Monitors used |
| Q15 | varchar |  |  | SI | Nurses notes |
| Q16 | varchar |  |  | SI | Dressing comments |
| Q17 | varchar |  |  | SI | Drainage comments |
| Q18 | varchar |  |  | SI | Handover received from |
| Q19 | date |  |  | SI | Conscious at  |
| Q20 | time |  |  | SI | Conscious at  |
| Q21 | varchar |  |  | SI | Conscious on arrival |
| Q22 | varchar |  |  | SI | Airway |
| Q23 | varchar |  |  | SI | Anaesthetic type |
| Q24 | varchar |  |  | SI | Intravenous (IV) access in situ |
| Q25 | varchar |  |  | SI | IV comment |
| Q26 | varchar |  |  | SI | Neurovascular status |
| Q27 | varchar |  |  | SI | Neurovascular comments |
| Q28 | varchar |  |  | SI | Post Anaesthetic Care (PAC) |
| Q29 | numeric |  |  | SI | Sedation Score (RASS) |
| Q30 | varchar |  |  | SI | PAC comments |
| Q31 | varchar |  |  | SI | Wound drainage on arrival |
| Q32 | varchar |  |  | SI | Pulse |
| Q32ObsDR | varchar |  | FK | SI | Pulse DR |
| Q33 | varchar |  |  | SI | Dressings |
| Q34 | date |  |  | SI | Date |
| Q35 | varchar |  |  | SI | O2 administered l/min |
| Q35ObsDR | varchar |  | FK | SI | O2 administered l/min DR |
| Q36 | time |  |  | SI | Time |
| Q37 | varchar |  |  | SI | Catheter in situ |
| Q38 | varchar |  |  | SI | Catheter comments |
| Q39 | varchar |  |  | SI | For catheters remaining in situ, please complete i... |
| Q40 | varchar |  |  | SI | Irrigation checked |
| Q41 | varchar |  |  | SI | O2 flow rate (L/min) |
| Q41ObsDR | varchar |  | FK | SI | O2 flow rate (L/min) DR |
| Q42 | varchar |  |  | SI | Pain score |
| Q42ObsDR | varchar |  | FK | SI | Pain score DR |
| Q46 | varchar |  |  | SI | Airway comments |
| QQ10 | bit |  |  | SI | Dressing status |
| QQ11 | bit |  |  | SI | Catheter checked |
| QQ12 | bit |  |  | SI | Irrigation checked |
| QQ13 | bit |  |  | SI | Mouth care given |
| QQ22 | bit |  |  | SI | Warming Blanket / Machine |
| QQ23 | bit |  |  | SI | IV cannula removed |
| QQ25 | numeric |  |  | SI | Pain score |
| QQ3 | varchar |  |  | SI | Initial Assessment |
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