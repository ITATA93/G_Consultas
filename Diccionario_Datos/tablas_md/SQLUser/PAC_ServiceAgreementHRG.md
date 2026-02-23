# SQLUser.PAC_ServiceAgreementHRG

**Schema:** SQLUser
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HRG_ParRef | bigint | PK |  | NO | PAC_ServiceAgreement Parent Reference |
| ChildQ01DR | - |  |  | SI | Child Reference: Peripheral Intravenous Catheter (... |
| HRG_Childsub | double |  |  | NO | Childsub |
| HRG_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| HRG_CreatedDate | date |  |  | SI | Created Date |
| HRG_CreatedTime | time |  |  | SI | Created Time |
| HRG_CreatedUser_DR | bigint |  | FK | SI | Created User |
| HRG_HRG_DR | bigint |  | FK | SI | Des Ref HRG |
| HRG_RowId | varchar |  |  | NO | - |
| HRG_UpdatedDate | date |  |  | SI | Updated Date |
| HRG_UpdatedTime | time |  |  | SI | Updated Time |
| HRG_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q02 | - |  |  | SI | Rationale for keeping cannula over 72 hours |
| Q03 | - |  |  | SI | Is the venous access required for longer |
| Q04 | - |  |  | SI | Consider referral to IV team for Peripheral Insert... |
| Q05 | - |  |  | SI | Nurse / Clinican |
| Q07 | - |  |  | SI | PIVC removal record |
| Q08 | - |  |  | SI | Removal date / time |
| Q09 | - |  |  | SI | Removal Time |
| Q10 | - |  |  | SI | Visual Infusion Phlebitis (VIP) score on removal |
| Q11 | - |  |  | SI | Reason for removal |
| Q12 | - |  |  | SI | If other please state |
| Q13 | - |  |  | SI | Nurse / Clinician |
| Q14 | - |  |  | SI | IMPORTANT NOTE |
| Q15 | - |  |  | SI | Ensure that this form is completed at each shift b... |
| Q16 | - |  |  | SI | Cannula site |
| Q17 | - |  |  | SI | Date |
| Q18 | - |  |  | SI | Time |
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