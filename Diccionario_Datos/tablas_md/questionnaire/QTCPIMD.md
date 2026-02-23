# questionnaire.QTCPIMD

> Pacemaker / Implantable Defibrillator Checklist

**Schema:** questionnaire
**Columnas:** 109
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Pacemaker / Implantable Defibrillator Checklist

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Pre-procedure Checklist |
| Q04 | varchar |  |  | SI | Interpreter required |
| Q05 | varchar |  |  | SI | Variance |
| Q06 | varchar |  |  | SI | Aboriginal health worker required |
| Q07 | varchar |  |  | SI | Variance |
| Q08 | varchar |  |  | SI | Consent signed |
| Q09 | varchar |  |  | SI | Variance |
| Q10 | varchar |  |  | SI | Patient armband in place and correct |
| Q11 | varchar |  |  | SI | Variance |
| Q12 | varchar |  |  | SI | All allergies documented |
| Q13 | varchar |  |  | SI | Variance |
| Q14 | varchar |  |  | SI | Fasting status |
| Q15 | varchar |  |  | SI | Variance |
| Q16 | varchar |  |  | SI | Baseline bloods reviewed including potassium level... |
| Q17 | varchar |  |  | SI | Variance |
| Q18 | varchar |  |  | SI | Intravascular cannula in situ and patent |
| Q19 | varchar |  |  | SI | Variance |
| Q20 | varchar |  |  | SI | Medications reviewed and withheld as ordered by do... |
| Q21 | varchar |  |  | SI | Variance |
| Q22 | varchar |  |  | SI | Check pre-medication order |
| Q23 | varchar |  |  | SI | Variance |
| Q24 | varchar |  |  | SI | Patient resting comfortably prior to procedure |
| Q25 | varchar |  |  | SI | Variance |
| Q26 | varchar |  |  | SI | Education provided regarding device insertion and ... |
| Q27 | varchar |  |  | SI | Variance |
| Q28 | varchar |  |  | SI | Day 0 - Post procedure |
| Q29 | varchar |  |  | SI | Reviewed by cardiologist |
| Q30 | varchar |  |  | SI | Variance |
| Q31 | varchar |  |  | SI | Leave patient on continuous monitoring until revie... |
| Q32 | varchar |  |  | SI | Variance |
| Q33 | varchar |  |  | SI | Once patient fully awake oral fluids and diet as o... |
| Q34 | varchar |  |  | SI | Variance |
| Q35 | varchar |  |  | SI | Rest in bed, can sit up in bed after 4 hours |
| Q36 | varchar |  |  | SI | Variance |
| Q37 | varchar |  |  | SI | Post operative procedure information sheet provide... |
| Q38 | varchar |  |  | SI | Variance |
| Q39 | varchar |  |  | SI | Day 1 |
| Q40 | varchar |  |  | SI | Observations remained within normal parameters |
| Q41 | varchar |  |  | SI | Variance |
| Q42 | varchar |  |  | SI | Continuous cardiac monitoring until device check a... |
| Q43 | varchar |  |  | SI | Variance |
| Q44 | varchar |  |  | SI | 12 lead electrocardiogram (ECG) conducted and revi... |
| Q45 | varchar |  |  | SI | Variance |
| Q46 | varchar |  |  | SI | Once device checked by Cardiology reviewed, patien... |
| Q47 | varchar |  |  | SI | Variance |
| Q48 | varchar |  |  | SI | Tolerating diet as ordered |
| Q49 | varchar |  |  | SI | Variance |
| Q50 | varchar |  |  | SI | Once mobilising, remove Thromboembolic Deterrent S... |
| Q51 | varchar |  |  | SI | Variance |
| Q52 | varchar |  |  | SI | Ensure regular medications are charted and reviewe... |
| Q53 | varchar |  |  | SI | Variance |
| Q54 | varchar |  |  | SI | If Cardiology review and patient is for discharge,... |
| Q55 | varchar |  |  | SI | Variance |
| Q56 | varchar |  |  | SI | Patient provided with post device care education, ... |
| Q57 | varchar |  |  | SI | Variance |
| Q58 | varchar |  |  | SI | Contact relevant Cardiac clinical nurse consultant... |
| Q59 | varchar |  |  | SI | Variance |
| Q60 | varchar |  |  | SI | Contact Aboriginal health worker if required for a... |
| Q61 | varchar |  |  | SI | Variance |
| Q62 | varchar |  |  | SI | Contact Interpreter if required for additional dis... |
| Q63 | varchar |  |  | SI | Variance |
| Q64 | varchar |  |  | SI | Cardiology appointment provided to patient |
| Q65 | varchar |  |  | SI | Variance |
| Q66 | varchar |  |  | SI | Device card given to the patient |
| Q67 | varchar |  |  | SI | Variance |
| Q68 | varchar |  |  | SI | Day of procedure |
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