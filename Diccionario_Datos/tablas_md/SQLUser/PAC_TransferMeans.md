# SQLUser.PAC_TransferMeans

**Schema:** SQLUser
**Columnas:** 79
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TRANSM_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Ulcer location |
| Q03 | - |  |  | SI | Directions: |
| Q04 | - |  |  | SI | Observe and measure the pressure ulcer. Categorize... |
| Q06 | - |  |  | SI | Other location: |
| Q07 | - |  |  | SI | Length x Width: |
| Q08 | - |  |  | SI | Exudate Amount: |
| Q09 | - |  |  | SI | Tissue Type: |
| Q10 | - |  |  | SI | Measure the greatest length (head to toe) and the ... |
| Q11 | - |  |  | SI | : Do not guess! Always use a centimeter ruler and ... |
| Q12 | - |  |  | SI | Estimate the amount of exudate (drainage) present ... |
| Q13 | - |  |  | SI | This refers to the types of tissue that are presen... |
| Q14 | - |  |  | SI | Score as a “3” if there is any amount of slough pr... |
| Q15 | - |  |  | SI | Score as a “2” if the wound is clean and contains ... |
| Q16 | - |  |  | SI | A superficial wound that is reepithelializing is s... |
| Q17 | - |  |  | SI | Length x width |
| Q18 | - |  |  | SI | Exudate amount |
| Q19 | - |  |  | SI | Tissue Type |
| Q20 | - |  |  | SI | The National Pressure Ulcer Advisory Panel (NPUAP)... |
| Q21 | - |  |  | SI | The PUSH is a quick, reliable tool to monitor the ... |
| Q22 | - |  |  | SI | 0 :  Healed |
| Q23 | - |  |  | SI | 1 to 17: Severity of the wound |
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
| TRANSM_Code | varchar |  |  | NO | Code |
| TRANSM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| TRANSM_CreatedDate | date |  |  | SI | Created Date |
| TRANSM_CreatedTime | time |  |  | SI | Created Time |
| TRANSM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| TRANSM_DateFrom | date |  |  | SI | Date From |
| TRANSM_DateTo | date |  |  | SI | Date To |
| TRANSM_Desc | varchar |  |  | NO | Description |
| TRANSM_IconName | varchar |  |  | SI | Icon Name |
| TRANSM_IconPriority | varchar |  |  | SI | Icon Priority |
| TRANSM_NationalCode | varchar |  |  | SI | NationalCode |
| TRANSM_Owner | varchar |  |  | SI | Owner |
| TRANSM_Subregion_DR | bigint |  | FK | SI | Subregion  |
| TRANSM_UpdatedDate | date |  |  | SI | Updated Date |
| TRANSM_UpdatedTime | time |  |  | SI | Updated Time |
| TRANSM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*