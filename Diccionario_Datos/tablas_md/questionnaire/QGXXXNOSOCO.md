# questionnaire.QGXXXNOSOCO

> Nosocomial Infections

**Schema:** questionnaire
**Columnas:** 119
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Nosocomial Infections

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Nosocomial infection type |
| Q01N | varchar |  |  | SI | Note |
| Q03 | varchar |  |  | SI | Urinary tract infection (UTI) |
| Q04 | date |  |  | SI | Diagnostic date |
| Q05 | varchar |  |  | SI | UTI cause |
| Q05ObsDR | varchar |  | FK | SI | UTI cause DR |
| Q06 | varchar |  |  | SI | Urinary catheter type |
| Q06ObsDR | varchar |  | FK | SI | Urinary catheter type DR |
| Q07 | date |  |  | SI | Catheterization date |
| Q08 | varchar |  |  | SI | UTI catheterization the last hour |
| Q08ObsDR | varchar |  | FK | SI | UTI catheterization the last hour DR |
| Q09 | varchar |  |  | SI | UTI sign and symptoms |
| Q09N | varchar |  |  | SI | Note |
| Q11 | varchar |  |  | SI | Urinary exams / tests |
| Q11N | varchar |  |  | SI | Note |
| Q13 | varchar |  |  | SI | Laboratory diagnostic nosocomial infections |
| Q14 | varchar |  |  | SI | Note |
| Q15 | varchar |  |  | SI | Hospital-acquired pneumonia (HAP) |
| Q16 | date |  |  | SI | Diagnostic date |
| Q17 | varchar |  |  | SI | Respiratory infection type |
| Q17ObsDR | varchar |  | FK | SI | Respiratory infection type DR |
| Q18 | varchar |  |  | SI | Respiratory infection cause |
| Q18N | varchar |  |  | SI | Note |
| Q18ObsDR | varchar |  | FK | SI | Respiratory infection cause DR |
| Q20 | varchar |  |  | SI | Respiratory ventilation |
| Q20ObsDR | varchar |  | FK | SI | Respiratory ventilation DR |
| Q21 | varchar |  |  | SI | Respiratory Ventilation the last hour |
| Q21ObsDR | varchar |  | FK | SI | Respiratory Ventilation the last hour DR |
| Q22 | varchar |  |  | SI | Respiratory signs and symptoms |
| Q22N | varchar |  |  | SI | Note |
| Q24 | varchar |  |  | SI | Laboratory diagnostic HAP |
| Q25 | varchar |  |  | SI | Note |
| Q26 | varchar |  |  | SI | Catheter-associated Intravascular Infection |
| Q27 | date |  |  | SI | Diagnostic date |
| Q28 | date |  |  | SI | Date catheter from |
| Q29 | date |  |  | SI | Date catheter to |
| Q30 | varchar |  |  | SI | Intravascular catheter type |
| Q30ObsDR | varchar |  | FK | SI | Intravascular catheter type DR |
| Q31 | varchar |  |  | SI | Intravascular catheter  localization |
| Q31ObsDR | varchar |  | FK | SI | Intravascular catheter  localization DR |
| Q32 | varchar |  |  | SI | Intravascular infection signs and symptoms |
| Q32N | varchar |  |  | SI | Note |
| Q33 | varchar |  |  | SI | Laboratory diagnostic intravascular infection |
| Q34 | varchar |  |  | SI | Note |
| Q35 | varchar |  |  | SI | Surgical site infection (SSI) |
| Q36 | date |  |  | SI | SSI diagnostic date |
| Q37 | date |  |  | SI | Date Surgery |
| Q38 | varchar |  |  | SI | Implantat in situ? |
| Q38N | varchar |  |  | SI | Note |
| Q38ObsDR | varchar |  | FK | SI | Implantat in situ? DR |
| Q40 | varchar |  |  | SI | SSI Infection type |
| Q40ObsDR | varchar |  | FK | SI | SSI Infection type DR |
| Q41 | varchar |  |  | SI | SSI Signs and Symptoms |
| Q41N | varchar |  |  | SI | Note |
| Q42 | varchar |  |  | SI | SSI  exams / tests |
| Q43 | varchar |  |  | SI | Laboratory diagnostic SSI |
| Q44 | varchar |  |  | SI | Note |
| Q45 | varchar |  |  | SI | Bacteremia |
| Q46 | date |  |  | SI | Diagnostic Date |
| Q47 | varchar |  |  | SI | Bacteremia cause |
| Q47N | varchar |  |  | SI | Note |
| Q47ObsDR | varchar |  | FK | SI | Bacteremia cause DR |
| Q49 | varchar |  |  | SI | Bacteremia exams / test |
| Q50 | varchar |  |  | SI | Bacteremia signs and symptoms |
| Q50N | varchar |  |  | SI | Note |
| Q51 | varchar |  |  | SI | Laboratory diagnostic bacteremia |
| Q52 | varchar |  |  | SI | Note |
| Q53 | varchar |  |  | SI | Methicillin-resistant Staphylococcus aureus (MRSA) |
| Q54 | date |  |  | SI | Diagnostic date |
| Q55 | varchar |  |  | SI | MRSA admission screening |
| Q55ObsDR | varchar |  | FK | SI | MRSA admission screening DR |
| Q56 | varchar |  |  | SI | MRSA Screening |
| Q56N | varchar |  |  | SI | Note |
| Q58 | varchar |  |  | SI | MRSA signs and symptoms |
| Q58N | varchar |  |  | SI | Note |
| Q60 | varchar |  |  | SI | Note |
| Q64 | date |  |  | SI | Date |
| Q65 | time |  |  | SI | Time |
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