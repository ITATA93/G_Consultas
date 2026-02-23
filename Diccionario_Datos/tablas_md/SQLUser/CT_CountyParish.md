# SQLUser.CT_CountyParish

**Schema:** SQLUser
**Columnas:** 65
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CNTYPAR_RowId | bigint | PK |  | NO | - |
| CNTYPAR_Code | varchar |  |  | NO | Code |
| CNTYPAR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CNTYPAR_CreatedDate | date |  |  | SI | Created Date |
| CNTYPAR_CreatedTime | time |  |  | SI | Created Time |
| CNTYPAR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CNTYPAR_DateFrom | date |  |  | SI | Date From |
| CNTYPAR_DateTo | date |  |  | SI | Date To |
| CNTYPAR_Desc | varchar |  |  | NO | Description |
| CNTYPAR_Owner | varchar |  |  | SI | Owner |
| CNTYPAR_UpdatedDate | date |  |  | SI | Updated Date |
| CNTYPAR_UpdatedTime | time |  |  | SI | Updated Time |
| CNTYPAR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Piensa que debido al tiempo que dedica a su famili... |
| Q02 | - |  |  | SI | ¿Se siente agobiado por intentar compatibilizar el... |
| Q03 | - |  |  | SI | ¿Piensa que el cuidar de su familiar afecta negati... |
| Q04 | - |  |  | SI | ¿Piensa que su salud ha empeorado debido a tener q... |
| Q05 | - |  |  | SI | ¿Se siente tenso cuando está cerca de su familiar? |
| Q06 | - |  |  | SI | ¿Se siente que ha perdido el control de su vida de... |
| Q07 | - |  |  | SI | Globalmente, ¿qué grado de carga experimenta por e... |
| Q08 | - |  |  | SI | Resultado Test Zarit Abreviado |
| Q08ObsDR | - |  |  | SI | Resultado Test Zarit Abreviado DR |
| Q09 | - |  |  | SI | Nombre Cuidador |
| Q10 | - |  |  | SI | RUN |
| Q11 | - |  |  | SI | Parentesco |
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