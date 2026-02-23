# SQLUser.BLC_ContractDetailsDate

**Schema:** SQLUser
**Columnas:** 66
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Detalle de la entidad padre.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DATE_ParRef | bigint | PK |  | NO | BLC_ContractDetails Parent Reference |
| DATE_Childsub | double |  |  | NO | Childsub |
| DATE_CreatedDate | date |  |  | SI | Created Date |
| DATE_CreatedTime | time |  |  | SI | Created Time |
| DATE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DATE_DateFrom | date |  |  | SI | Date From |
| DATE_DateTo | date |  |  | SI | Date To |
| DATE_RowId | varchar |  |  | NO | - |
| DATE_UpdatedDate | date |  |  | SI | Updated Date |
| DATE_UpdatedTime | time |  |  | SI | Updated Time |
| DATE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| DATE_VAT_DR | bigint |  | FK | SI | Override VAT |
| Q01 | - |  |  | SI | Fecha |
| Q02 | - |  |  | SI | Se verifica nombre completo |
| Q03 | - |  |  | SI | Comentarios se verifica nombre completo |
| Q04 | - |  |  | SI | Se cuenta con ficha clínica |
| Q05 | - |  |  | SI | Comentarios se cuenta con ficha clinica |
| Q06 | - |  |  | SI | Firma consentimiento informado |
| Q07 | - |  |  | SI | Comentarios firma consentimiento informado |
| Q08 | - |  |  | SI | Con antecedentes de alergia o contraindicaciones |
| Q09 | - |  |  | SI | Comentarios con antecedentes de alergia o contrain... |
| Q10 | - |  |  | SI | Recibe premedicación oral y/o endovenosa |
| Q11 | - |  |  | SI | Comentarios recibe premedicación oral y/o endoveno... |
| Q12 | - |  |  | SI | Ayuno > 6 horas |
| Q13 | - |  |  | SI | Comentarios ayuno > 6 horas |
| Q14 | - |  |  | SI | Responsable |
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