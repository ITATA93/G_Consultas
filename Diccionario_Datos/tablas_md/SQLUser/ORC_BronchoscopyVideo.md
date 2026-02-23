# SQLUser.ORC_BronchoscopyVideo

**Schema:** SQLUser
**Columnas:** 72
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BROVID_RowId | bigint | PK |  | NO | - |
| BROVID_Code | varchar |  |  | NO | Code |
| BROVID_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| BROVID_CreatedDate | date |  |  | SI | Created Date |
| BROVID_CreatedTime | time |  |  | SI | Created Time |
| BROVID_CreatedUser_DR | bigint |  | FK | SI | Created User |
| BROVID_DateFrom | date |  |  | SI | Date From |
| BROVID_DateTo | date |  |  | SI | Date To |
| BROVID_Desc | varchar |  |  | NO | Description |
| BROVID_Owner | varchar |  |  | SI | Owner |
| BROVID_UpdatedDate | date |  |  | SI | Updated Date |
| BROVID_UpdatedTime | time |  |  | SI | Updated Time |
| BROVID_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Tipo 1 |
| Q02 | - |  |  | SI | Tipo 2 |
| Q03 | - |  |  | SI | Tipo 3 |
| Q04 | - |  |  | SI | Tipo 4 |
| Q05 | - |  |  | SI | Tipo 5 |
| Q06 | - |  |  | SI | Tipo 6 |
| Q07 | - |  |  | SI | Tipo 7 |
| Q08 | - |  |  | SI | Separate hard lumps, like nuts (hard to pass) |
| Q09 | - |  |  | SI | Sausage-shaped but lumpy |
| Q10 | - |  |  | SI | Like a sausage but with cracks on the surface |
| Q11 | - |  |  | SI | Like a sausage or snake, smooth and soft |
| Q12 | - |  |  | SI | Soft blobs with clear-cut edges |
| Q13 | - |  |  | SI | Fluffy pieces with ragged edges, a mushy stool |
| Q14 | - |  |  | SI | Watery, no solid pieces. Entirely liquid |
| Q16 | - |  |  | SI | O’Donnell LJ, Virjee J, Heaton KW. Detection of ps... |
| Q17 | - |  |  | SI | Date |
| Q18 | - |  |  | SI | Time |
| QOBS | - |  |  | SI | Escala de Bristol |
| QOBSObsDR | - |  |  | SI | Escala de Bristol DR |
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