# SQLUser.ARC_BillGrpDesc

**Schema:** SQLUser
**Columnas:** 66
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DES_ParRef | bigint | PK |  | NO | ARC_BillGrp Parent Reference |
| DES_Childsub | double |  |  | NO | Childsub |
| DES_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DES_CreatedDate | date |  |  | SI | Created Date |
| DES_CreatedTime | time |  |  | SI | Created Time |
| DES_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DES_Desc | varchar |  |  | SI | Description |
| DES_InsType_DR | bigint |  | FK | SI | Des Ref InsType |
| DES_RowId | varchar |  |  | NO | - |
| DES_UpdatedDate | date |  |  | SI | Updated Date |
| DES_UpdatedTime | time |  |  | SI | Updated Time |
| DES_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | 1. Necesidad de cuidados complejos |
| Q02 | - |  |  | SI | Número de sistemas comprometidos |
| Q03 | - |  |  | SI | Necesidad de Polifarmacia |
| Q04 | - |  |  | SI | Necesidad vía alternativa de administración de fár... |
| Q05 | - |  |  | SI | Necesidad de fármacos poco accesibles |
| Q06 | - |  |  | SI | Necesidad de Alimentación especial |
| Q07 | - |  |  | SI | 2. Necesidad de apoyo respiratorio |
| Q08 | - |  |  | SI | Necesidad de oxigenoterapia |
| Q09 | - |  |  | SI | Necesidad de aspiración de secreciones |
| Q10 | - |  |  | SI | Necesidad de ventilación mecánica |
| Q11 | - |  |  | SI | 3. Necesidad de ayudas técnicas (AATT) |
| Q12 | - |  |  | SI | Necesidad de ayudas técnicas para la autonomía, pa... |
| Q13 | - |  |  | SI | Necesidad de ayudas técnicas para los cuidados, hi... |
| Q14 | - |  |  | SI | Necesidad de ayudas técnicas ortopédicas |
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