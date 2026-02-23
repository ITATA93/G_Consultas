# questionnaire.QTCICPPRSTR

> Invasive Cardiac Procedure Post Removal of Sheath and TR Band Checklist

**Schema:** questionnaire
**Columnas:** 101
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Invasive Cardiac Procedure Post Removal of Sheath and TR Band Checklist

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Catheter insertion site |
| Q04 | varchar |  |  | SI | Variance |
| Q05 | varchar |  |  | SI | Insertions sites remain free of ooze and haematoma |
| Q06 | varchar |  |  | SI | Variance |
| Q07 | varchar |  |  | SI | Femoral sheath removed as per protocol |
| Q08 | varchar |  |  | SI | Variance |
| Q09 | varchar |  |  | SI | Femoral compression device removed as per protocol |
| Q10 | varchar |  |  | SI | Variance |
| Q11 | varchar |  |  | SI | Radial&nbsp;compression device removed as per prot... |
| Q12 | varchar |  |  | SI | Variance |
| Q13 | varchar |  |  | SI | Observations remained within normal parameters |
| Q14 | varchar |  |  | SI | Variance |
| Q15 | varchar |  |  | SI | Neurovascular observations remained within normal ... |
| Q16 | varchar |  |  | SI | Variance |
| Q17 | varchar |  |  | SI | Intravenous cannula patent |
| Q18 | varchar |  |  | SI | Variance |
| Q19 | varchar |  |  | SI | Medications administered as prescribed |
| Q20 | varchar |  |  | SI | Variance |
| Q21 | varchar |  |  | SI | Gastrointestinal / Urinary |
| Q22 | varchar |  |  | SI | Tolerating ordered diet |
| Q23 | varchar |  |  | SI | Variance |
| Q24 | varchar |  |  | SI | Passed urine post procedure |
| Q25 | varchar |  |  | SI | Variance |
| Q26 | varchar |  |  | SI | Hygiene Care |
| Q27 | varchar |  |  | SI | Showered with assistance |
| Q28 | varchar |  |  | SI | Variance |
| Q29 | varchar |  |  | SI | Activity / Mobility |
| Q30 | varchar |  |  | SI | Mobilised after 1 hour |
| Q31 | varchar |  |  | SI | Variance |
| Q32 | varchar |  |  | SI | Arterial Femoral approach - rest in bed 6 hours po... |
| Q33 | varchar |  |  | SI | Variance |
| Q34 | varchar |  |  | SI | Venous Femoral approach - mobilise as directed by ... |
| Q35 | varchar |  |  | SI | Variance |
| Q36 | varchar |  |  | SI | Education |
| Q37 | varchar |  |  | SI | Complete cardiac education phase 1 and post proced... |
| Q38 | varchar |  |  | SI | Variance |
| Q39 | varchar |  |  | SI | Referrals |
| Q40 | varchar |  |  | SI | Internal consult request made to appropriate servi... |
| Q41 | varchar |  |  | SI | Variance |
| Q42 | varchar |  |  | SI | Referrals made to external providers as appropriat... |
| Q43 | varchar |  |  | SI | Variance |
| Q44 | varchar |  |  | SI | Variance |
| Q45 | varchar |  |  | SI | Variance |
| Q46 | varchar |  |  | SI | Variance |
| Q47 | varchar |  |  | SI | Variance |
| Q48 | varchar |  |  | SI | Variance |
| Q49 | varchar |  |  | SI | Variance |
| Q50 | varchar |  |  | SI | Variance |
| Q51 | varchar |  |  | SI | Variance |
| Q52 | varchar |  |  | SI | Variance |
| Q53 | varchar |  |  | SI | Variance |
| Q54 | varchar |  |  | SI | Variance |
| Q55 | varchar |  |  | SI | Variance |
| Q56 | varchar |  |  | SI | Variance |
| Q57 | varchar |  |  | SI | Variance |
| Q58 | varchar |  |  | SI | Variance |
| Q59 | varchar |  |  | SI | Variance |
| Q60 | varchar |  |  | SI | Variance |
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