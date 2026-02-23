# SQLUser.ARC_PayAgreemBlackListCP

**Schema:** SQLUser
**Columnas:** 60
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Pagos**. Tarifas y facturación.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BLCP_ParRef | bigint | PK |  | NO | ARC_PaymentAgreement Parent Reference |
| BLCP_CareProv_DR | varchar |  | FK | SI | Des Ref CTCareProv |
| BLCP_Childsub | double |  |  | NO | Childsub |
| BLCP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| BLCP_CreatedDate | date |  |  | SI | Created Date |
| BLCP_CreatedTime | time |  |  | SI | Created Time |
| BLCP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| BLCP_DateFrom | date |  |  | SI | Date From |
| BLCP_DateTo | date |  |  | SI | Date To |
| BLCP_Hospital_DR | bigint |  | FK | SI | Des Ref CTHospital |
| BLCP_PostOffice_DR | bigint |  | FK | SI | Des Ref ARCPostOffice |
| BLCP_RowId | varchar |  |  | NO | - |
| BLCP_UpdatedDate | date |  |  | SI | Updated Date |
| BLCP_UpdatedTime | time |  |  | SI | Updated Time |
| BLCP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | 1. ¿Está básicamente satisfecho con su vida? |
| Q02 | - |  |  | SI | 2. ¿Se siente aburrido frecuentemente? |
| Q03 | - |  |  | SI | 3. ¿Con frecuencia se siente desamparado, que no v... |
| Q04 | - |  |  | SI | 4. ¿Prefiere quedarse en casa en vez de salir o ha... |
| Q05 | - |  |  | SI | 5. ¿Se siente inútil como está ahora? |
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