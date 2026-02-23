# SQLUser.ORC_ReasonForProcedureVariance

**Schema:** SQLUser
**Columnas:** 71
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OTRFV_RowId | bigint | PK |  | NO | - |
| OTRFV_Code | varchar |  |  | NO | Code |
| OTRFV_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| OTRFV_DateFrom | date |  |  | SI | Date From |
| OTRFV_DateTo | date |  |  | SI | Date To |
| OTRFV_Desc | varchar |  |  | NO | Description |
| OTRFV_Owner | varchar |  |  | SI | Owner |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Admission date |
| Q04 | - |  |  | SI | Admission time |
| Q05 | - |  |  | SI | Admission nurse |
| Q06 | - |  |  | SI | Patient identity confirmed correct |
| Q07 | - |  |  | SI | Identity comments |
| Q09 | - |  |  | SI | Latest platelets result (x 109/L) |
| Q10 | - |  |  | SI | Date of platelets result |
| Q11 | - |  |  | SI | Intravascular access established |
| Q12 | - |  |  | SI | Last food date / time |
| Q13 | - |  |  | SI | Last food time |
| Q14 | - |  |  | SI | Last fluid date / time |
| Q15 | - |  |  | SI | Last fluid time |
| Q16 | - |  |  | SI | Metal in body |
| Q17 | - |  |  | SI | Metal in body details |
| Q18 | - |  |  | SI | Bowel preparation |
| Q19 | - |  |  | SI | Other bowel preparation |
| Q20 | - |  |  | SI | Additional bowel preparation augmentation |
| Q21 | - |  |  | SI | Augmentation details |
| Q22 | - |  |  | SI | Bowel preparation comments |
| Q23 | - |  |  | SI | Discharge plan |
| Q24 | - |  |  | SI | Post procedure transport arrangements confirmed |
| Q25 | - |  |  | SI | Transport arrangements |
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