# SQLUser.CT_PubHol

**Schema:** SQLUser
**Columnas:** 82
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTHOL_RowId | bigint | PK |  | NO | - |
| CTHOL_Code | date |  |  | NO | Public Holidays Code |
| CTHOL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CTHOL_CreatedDate | date |  |  | SI | Created Date |
| CTHOL_CreatedTime | time |  |  | SI | Created Time |
| CTHOL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CTHOL_Desc | varchar |  |  | NO | Public Holidays Description |
| CTHOL_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| CTHOL_NotUseFlag | varchar |  |  | NO | Not Use Flag |
| CTHOL_Owner | varchar |  |  | SI | Owner |
| CTHOL_UpdatedDate | date |  |  | SI | Updated Date |
| CTHOL_UpdatedTime | time |  |  | SI | Updated Time |
| CTHOL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| CTHOL_UseforOutpatientsOnly | varchar |  |  | SI | Use for Outpatients Only |
| Q01 | - |  |  | SI | Surgeon |
| Q02 | - |  |  | SI | Anesthetics |
| Q03 | - |  |  | SI | Perfusionist |
| Q04 | - |  |  | SI | Start time |
| Q05 | - |  |  | SI | Checklist |
| Q06 | - |  |  | SI | Cardiotomy & table line setup by |
| Q07 | - |  |  | SI | Cardiotomy & table line setup signature |
| Q07UDt | - |  |  | SI | Cardiotomy & table line setup signature Last Updat... |
| Q07UTm | - |  |  | SI | Cardiotomy & table line setup signature Last Updat... |
| Q08 | - |  |  | SI | Cell saver setup by |
| Q09 | - |  |  | SI | Cell saver setup signature |
| Q09UDt | - |  |  | SI | Cell saver setup signature Last Updated Date |
| Q09UTm | - |  |  | SI | Cell saver setup signature Last Updated Time |
| Q10 | - |  |  | SI | Volume collected (ml) |
| Q11 | - |  |  | SI | Anticoagulant solution (ml) |
| Q12 | - |  |  | SI | Wash volume (ml) |
| Q13 | - |  |  | SI | Red blood cells returned (ml) |
| Q14 | - |  |  | SI | Oximetrie value hct E (%) |
| Q15 | - |  |  | SI | Electrolyte value K+ (mmol/L) |
| Q16 | - |  |  | SI | End time	 |
| Q17 | - |  |  | SI | Total Time |
| Q18 | - |  |  | SI | Name |
| Q19 | - |  |  | SI | Signature |
| Q19UDt | - |  |  | SI | Signature Last Updated Date |
| Q19UTm | - |  |  | SI | Signature Last Updated Time |
| Q20 | - |  |  | SI | Date |
| Q21 | - |  |  | SI | Time |
| Q22 | - |  |  | SI | Cell Saver Notes |
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