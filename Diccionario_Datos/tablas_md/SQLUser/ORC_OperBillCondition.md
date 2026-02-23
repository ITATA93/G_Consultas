# SQLUser.ORC_OperBillCondition

**Schema:** SQLUser
**Columnas:** 73
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OPBIL_RowId | bigint | PK |  | NO | - |
| OPBIL_Code | varchar |  |  | NO | Code |
| OPBIL_CreatedDate | date |  |  | SI | Created Date |
| OPBIL_CreatedTime | time |  |  | SI | Created Time |
| OPBIL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| OPBIL_Desc | varchar |  |  | NO | Description |
| OPBIL_UpdatedDate | date |  |  | SI | Updated Date |
| OPBIL_UpdatedTime | time |  |  | SI | Updated Time |
| OPBIL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q1 | - |  |  | SI | Diet Preferences |
| Q10 | - |  |  | SI | Therapeutic Diets |
| Q11 | - |  |  | SI | Diet type |
| Q12 | - |  |  | SI | Specify other diet type |
| Q13 | - |  |  | SI | Therapeutic diet |
| Q14 | - |  |  | SI | Clinical diet |
| Q15 | - |  |  | SI | Instructions and Feeding Aids |
| Q16 | - |  |  | SI | Special instructions |
| Q17 | - |  |  | SI | Special instructions comments |
| Q18 | - |  |  | SI | Feeding aids |
| Q19 | - |  |  | SI | Other feeding aid comments |
| Q2 | - |  |  | SI | Restrictions |
| Q20 | - |  |  | SI | Date |
| Q21 | - |  |  | SI | Time |
| Q22 | - |  |  | SI | Diet type |
| Q23 | - |  |  | SI | Special instructions |
| Q24 | - |  |  | SI | Feeding aids |
| Q3 | - |  |  | SI | Preferences |
| Q4 | - |  |  | SI | Specify |
| Q5 | - |  |  | SI | Diet modifiers |
| Q6 | - |  |  | SI | Modifiers |
| Q7 | - |  |  | SI | Fluid volume restriction |
| Q8 | - |  |  | SI | Food texture |
| Q9 | - |  |  | SI | Fluid consistency |
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