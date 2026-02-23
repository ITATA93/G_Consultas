# questionnaire.QGXXXPSIR

> Patient Safety Incident Report

**Schema:** questionnaire
**Columnas:** 92
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Patient Safety Incident Report

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Incident Category |
| Q03 | date |  |  | SI | Incident Date / Time |
| Q04 | time |  |  | SI | Incident Time |
| Q08 | varchar |  |  | SI | Narrative around incident |
| Q09 | varchar |  |  | SI | Inmediate action taken |
| Q10 | bit |  |  | SI | Approximate Date / Time |
| Q19 | varchar |  |  | SI | Incident comments |
| Q27 | varchar |  |  | SI | Injury details |
| Q31 | varchar |  |  | SI | Actions taken to prevent incident occurring again |
| Q32 | varchar |  |  | SI | Escalation |
| Q33 | varchar |  |  | SI | Outcome & Impact Comments |
| Q34 | varchar |  |  | SI | Other people Involved? |
| Q35 | varchar |  |  | SI | Name of others and their roles |
| Q36 | varchar |  |  | SI | Incident Severity |
| Q37 | varchar |  |  | SI | Incident Probability |
| Q38 | varchar |  |  | SI | Former fall reported in the same episode |
| Q39 | varchar |  |  | SI | Who observed the fall? |
| Q40 | varchar |  |  | SI | Prior to the fall, what was the patient doing or t... |
| Q41 | varchar |  |  | SI | Was the fall unassisted or assisted? |
| Q42 | varchar |  |  | SI | Prior to the fall, was a fall risk assessment docu... |
| Q43 | varchar |  |  | SI | Applied evaluations |
| Q44 | varchar |  |  | SI | Required investigations |
| Q45 | varchar |  |  | SI | Type of investigations |
| Q46 | varchar |  |  | SI | Investigations outcomes |
| Q47 | varchar |  |  | SI | Possible clinical risk - Medications |
| Q48 | varchar |  |  | SI | Possible clinical risk - Sensory deficit |
| Q49 | varchar |  |  | SI | Sentinel event |
| Q50 | varchar |  |  | SI | Other documentation available |
| Q51 | varchar |  |  | SI | Notes on available documentation |
| QINFIN | varchar |  |  | SI | Finalcial Impact |
| QIRACC | varchar |  |  | SI | Patient Accident Incident |
| QIRCF | varchar |  |  | SI | Contributing Factors |
| QIRCF1 | varchar |  |  | SI | Contributing Factors comments |
| QIRCS | varchar |  |  | SI | Care Setting |
| QIRDEV | varchar |  |  | SI | Medical Device / Equipment Incident |
| QIRDEV1 | varchar |  |  | SI | Description |
| QIRDEV2 | varchar |  |  | SI | Manufacturer |
| QIRDEV3 | varchar |  |  | SI | Model |
| QIRDEV4 | varchar |  |  | SI | Serial Number |
| QIRLoc | varchar |  |  | SI | Location |
| QIRMED | varchar |  |  | SI | Medication incident |
| QIRProb | varchar |  |  | SI | Incident Probability |
| QIRRisk | varchar |  |  | SI | Risk Assessment previously done |
| QIRRisk2 | date |  |  | SI | Date of last Risk Assessment |
| QIRRisk3 | varchar |  |  | SI | Score from last Risk Assessment |
| QIRRisk4 | varchar |  |  | SI | Risk Re-Assessment required |
| QIRRiskGrad | varchar |  |  | SI | Risk Grading |
| QIRSEV | varchar |  |  | SI | Incident Severity |
| QIRSecLoc | varchar |  |  | SI | Secondary Location |
| QIRTTT | varchar |  |  | SI | Treatment or Procedure Incident |
| QIRTType | varchar |  |  | SI | Incident Type |
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