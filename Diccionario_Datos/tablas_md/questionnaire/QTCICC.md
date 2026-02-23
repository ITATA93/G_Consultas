# questionnaire.QTCICC

> Infection Control Checklist

**Schema:** questionnaire
**Columnas:** 76
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Infection Control Checklist

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | MRSA/VRE/Clostridioides (Clostridium) difficile/Ot... |
| Q02 | varchar |  |  | SI | Diarrhoea / Gastroenteritis |
| Q03 | varchar |  |  | SI | Acute respiratory infection / influenza |
| Q04 | varchar |  |  | SI | Other infection / infectious disease |
| Q05 | varchar |  |  | SI | Is isolation required? |
| Q06 | varchar |  |  | SI | Is isolation required? |
| Q07 | varchar |  |  | SI | Is isolation required? |
| Q08 | varchar |  |  | SI | Is isolation required? |
| Q09 | varchar |  |  | SI | Intensive precautions are to be commenced and Infe... |
| Q10 | varchar |  |  | SI | Previous positive result for CPE (Carbapenemase-pr... |
| Q11 | varchar |  |  | SI | Notify Infection Prevention Control |
| Q12 | varchar |  |  | SI | Direct transfer from an overseas hospital? |
| Q13 | varchar |  |  | SI | Commence CPE and C.auris screening |
| Q14 | varchar |  |  | SI | Overnight stay in an overseas healthcare or long t... |
| Q15 | varchar |  |  | SI | Commence CPE and C.auris screening |
| Q16 | varchar |  |  | SI | A room contact of a confirmed case or a case who h... |
| Q17 | varchar |  |  | SI | Commence CPE and Ca.auris screening |
| Q18 | varchar |  |  | SI | A ward contact where a transmission of CPE / Candi... |
| Q19 | varchar |  |  | SI | Commence CPE and Ca.auris screening |
| Q20 | varchar |  |  | SI | Faeces specimen, or if not clinically or practical... |
| Q21 | varchar |  |  | SI | Groin and axilla swabs, as minimum (consider addit... |
| Q22 | varchar |  |  | SI | - Methicillin-resistant Staphylococcus aureus |
| Q23 | varchar |  |  | SI | - Vancomycin-Resistant Enterococcus |
| Q24 | varchar |  |  | SI | - Multi-Resistant Organisms  |
| Q25 | varchar |  |  | SI | C.auris Screening: |
| Q26 | varchar |  |  | SI | CPE Screening: |
| Q27 | varchar |  |  | SI | MRSA |
| Q28 | varchar |  |  | SI | VRE |
| Q29 | varchar |  |  | SI | MRO |
| Q30 | varchar |  |  | SI | Faeces specimen, or if not clinically or practical... |
| Q31 | varchar |  |  | SI | Groin and axilla swabs, as minimum (consider addit... |
| Q32 | varchar |  |  | SI | Skin rash |
| Q33 | date |  |  | SI | Date |
| Q34 | time |  |  | SI | Time |
| Q35 | varchar |  |  | SI | Is isolation required? |
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