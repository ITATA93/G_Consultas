# SQLUser.PAC_Agency

**Schema:** SQLUser
**Columnas:** 88
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| AG_RowId | bigint | PK |  | NO | - |
| AG_Address | varchar |  |  | SI | Address |
| AG_City_DR | bigint |  | FK | SI | Des Ref City |
| AG_Code | varchar |  |  | NO | Code |
| AG_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| AG_CreatedDate | date |  |  | SI | Created Date |
| AG_CreatedTime | time |  |  | SI | Created Time |
| AG_CreatedUser_DR | bigint |  | FK | SI | Created User |
| AG_Desc | varchar |  |  | NO | Description |
| AG_Owner | varchar |  |  | SI | Owner |
| AG_UpdatedDate | date |  |  | SI | Updated Date |
| AG_UpdatedTime | time |  |  | SI | Updated Time |
| AG_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| AG_Zip_DR | bigint |  | FK | SI | Zip |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Indication |
| Q04 | - |  |  | SI | Other indication details |
| Q05 | - |  |  | SI | Wound onset date |
| Q06 | - |  |  | SI | Wound onset time |
| Q07 | - |  |  | SI | Evidence of macrovascular disease |
| Q08 | - |  |  | SI | Evidence of osteomyelitis |
| Q09 | - |  |  | SI | Relevant previous or planned surgical management |
| Q10 | - |  |  | SI | Previous hyperbaric treatment |
| Q11 | - |  |  | SI | Indication notes |
| Q12 | - |  |  | SI | Risk of pneumothorax (e.g. patient had a recent pn... |
| Q13 | - |  |  | SI | Risk of lowered seizure threshold (e.g. patient ha... |
| Q14 | - |  |  | SI | Risk of anxiety attack (e.g. patient suffers from ... |
| Q15 | - |  |  | SI | Risk of oxygen sensitivity and/or pneumonitis (e.g... |
| Q16 | - |  |  | SI | Risk of cardiotoxicity (e.g. patient is on Doxorub... |
| Q17 | - |  |  | SI | Risk of impaired wound healing (e.g. patient is on... |
| Q18 | - |  |  | SI | Risk of implanted device malfunction or deformatio... |
| Q19 | - |  |  | SI | Known cardiac defect with shunt |
| Q20 | - |  |  | SI | Possible contraindication notes |
| Q21 | - |  |  | SI | Description of wound |
| Q22 | - |  |  | SI | Peripheral circulation |
| Q23 | - |  |  | SI | Chest |
| Q24 | - |  |  | SI | Otoscopy |
| Q25 | - |  |  | SI | TcO2 |
| Q26 | - |  |  | SI | Examination notes |
| Q27 | - |  |  | SI | Investigations completed |
| Q28 | - |  |  | SI | Other investigations |
| Q29 | - |  |  | SI | Investigation notes |
| Q30 | - |  |  | SI | Hyperbaric indicated |
| Q31 | - |  |  | SI | Patient fit for hyperbaric |
| Q32 | - |  |  | SI | Outcome notes |
| Q33 | - |  |  | SI | Consent obtained |
| Q34 | - |  |  | SI | Consent notes |
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