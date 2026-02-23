# SQLUser.PAC_LabDelComplications

**Schema:** SQLUser
**Columnas:** 78
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LDCOMPL_RowId | bigint | PK |  | NO | - |
| LDCOMPL_Active | varchar |  |  | SI | Active flag |
| LDCOMPL_Code | varchar |  |  | NO | Code |
| LDCOMPL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LDCOMPL_CreatedDate | date |  |  | SI | Created Date |
| LDCOMPL_CreatedTime | time |  |  | SI | Created Time |
| LDCOMPL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LDCOMPL_DateFrom | date |  |  | SI | Date From |
| LDCOMPL_DateTo | date |  |  | SI | Date To |
| LDCOMPL_Desc | varchar |  |  | NO | Description |
| LDCOMPL_NationalCode | varchar |  |  | SI | National Code |
| LDCOMPL_Owner | varchar |  |  | SI | Owner |
| LDCOMPL_UpdatedDate | date |  |  | SI | Updated Date |
| LDCOMPL_UpdatedTime | time |  |  | SI | Updated Time |
| LDCOMPL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q1 | - |  |  | SI | Date |
| Q10 | - |  |  | SI | Organized or serious attempt (well thought-out pla... |
| Q11 | - |  |  | SI | No social supports (no close family, friends, job,... |
| Q12 | - |  |  | SI | Stated future intent (determined to repeat attempt... |
| Q13 | - |  |  | SI | Score |
| Q14 | - |  |  | SI | Classification |
| Q15 | - |  |  | SI | ≥6 |
| Q16 | - |  |  | SI | High suicide risk, need psychiatry directed hospit... |
| Q17 | - |  |  | SI | &lt |
| Q18 | - |  |  | SI | May be safe to discharge, depending on circumstanc... |
| Q19 | - |  |  | SI | Provenance details |
| Q2 | - |  |  | SI | Time |
| Q20 | - |  |  | SI | The modified SAD PERSONS score is a modification b... |
| Q21 | - |  |  | SI | 1. Hockberger RS, Rothstein RJ. Assessment of suic... |
| Q22 | - |  |  | SI | 2. Patterson WM, Dohn HH, Bird J, Patterson GA. Ev... |
| Q23 | - |  |  | SI | The modified SAD PERSONS score is a modification b... |
| Q3 | - |  |  | SI | Sex |
| Q4 | - |  |  | SI | Age |
| Q5 | - |  |  | SI | Depression or hopelessness (admits to depression o... |
| Q6 | - |  |  | SI | Previous attempts or psychiatric care (previous in... |
| Q7 | - |  |  | SI | Excessive alcohol or drug use (stigmata of chronic... |
| Q8 | - |  |  | SI | Rational thinking loss (organic brain syndrome or&... |
| Q9 | - |  |  | SI | Separated, divorced or widowed |
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