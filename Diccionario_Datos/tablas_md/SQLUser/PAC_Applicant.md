# SQLUser.PAC_Applicant

**Schema:** SQLUser
**Columnas:** 86
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| APPL_RowId | bigint | PK |  | NO | - |
| APPL_Code | varchar |  |  | NO | Code |
| APPL_CreatedDate | date |  |  | SI | Created Date |
| APPL_CreatedTime | time |  |  | SI | Created Time |
| APPL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| APPL_DateFrom | date |  |  | SI | DateFrom |
| APPL_DateTo | date |  |  | SI | DateTo |
| APPL_Desc | varchar |  |  | NO | Description |
| APPL_UpdatedDate | date |  |  | SI | Updated Date |
| APPL_UpdatedTime | time |  |  | SI | Updated Time |
| APPL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | MRSA/VRE/Clostridioides (Clostridium) difficile/Ot... |
| Q02 | - |  |  | SI | Diarrhoea / Gastroenteritis |
| Q03 | - |  |  | SI | Acute respiratory infection / influenza |
| Q04 | - |  |  | SI | Other infection / infectious disease |
| Q05 | - |  |  | SI | Is isolation required? |
| Q06 | - |  |  | SI | Is isolation required? |
| Q07 | - |  |  | SI | Is isolation required? |
| Q08 | - |  |  | SI | Is isolation required? |
| Q09 | - |  |  | SI | Intensive precautions are to be commenced and Infe... |
| Q10 | - |  |  | SI | Previous positive result for CPE (Carbapenemase-pr... |
| Q11 | - |  |  | SI | Notify Infection Prevention Control |
| Q12 | - |  |  | SI | Direct transfer from an overseas hospital? |
| Q13 | - |  |  | SI | Commence CPE and C.auris screening |
| Q14 | - |  |  | SI | Overnight stay in an overseas healthcare or long t... |
| Q15 | - |  |  | SI | Commence CPE and C.auris screening |
| Q16 | - |  |  | SI | A room contact of a confirmed case or a case who h... |
| Q17 | - |  |  | SI | Commence CPE and Ca.auris screening |
| Q18 | - |  |  | SI | A ward contact where a transmission of CPE / Candi... |
| Q19 | - |  |  | SI | Commence CPE and Ca.auris screening |
| Q20 | - |  |  | SI | Faeces specimen, or if not clinically or practical... |
| Q21 | - |  |  | SI | Groin and axilla swabs, as minimum (consider addit... |
| Q22 | - |  |  | SI | - Methicillin-resistant Staphylococcus aureus |
| Q23 | - |  |  | SI | - Vancomycin-Resistant Enterococcus |
| Q24 | - |  |  | SI | - Multi-Resistant Organisms |
| Q25 | - |  |  | SI | C.auris Screening: |
| Q26 | - |  |  | SI | CPE Screening: |
| Q27 | - |  |  | SI | MRSA |
| Q28 | - |  |  | SI | VRE |
| Q29 | - |  |  | SI | MRO |
| Q30 | - |  |  | SI | Faeces specimen, or if not clinically or practical... |
| Q31 | - |  |  | SI | Groin and axilla swabs, as minimum (consider addit... |
| Q32 | - |  |  | SI | Skin rash |
| Q33 | - |  |  | SI | Date |
| Q34 | - |  |  | SI | Time |
| Q35 | - |  |  | SI | Is isolation required? |
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