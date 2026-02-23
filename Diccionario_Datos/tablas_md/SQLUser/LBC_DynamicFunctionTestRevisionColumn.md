# SQLUser.LBC_DynamicFunctionTestRevisionColumn

**Schema:** SQLUser
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCDFTRC_ParRef | bigint | PK |  | NO | Parent Table |
| ChildQ10DR | - |  |  | SI | Child Reference: Persons not permitted to visit th... |
| LBCDFTRC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCDFTRC_Column | integer |  |  | SI | Column Number |
| LBCDFTRC_DisplayOnReport | varchar |  |  | SI | Display On Report |
| LBCDFTRC_Header | varchar |  |  | SI | Column Header
Text to appear in the column header... |
| LBCDFTRC_LBCTI_DR | bigint |  | FK | SI | Column TestItem
LBCTIDR for column, if Type="TI" |
| LBCDFTRC_RowID | varchar |  |  | NO | - |
| LBCDFTRC_SubCol1Header | varchar |  |  | SI | Column Header for Result
If type is "TI" this is ... |
| LBCDFTRC_SubCol1Width | integer |  |  | SI | Width of Column for Result
If type is "TI" this i... |
| LBCDFTRC_SubCol2Header | varchar |  |  | SI | Column Header for Units
If type is "TI" this is t... |
| LBCDFTRC_SubCol2Width | integer |  |  | SI | Width of Column for Units
If type is "TI" this is... |
| LBCDFTRC_SubCol3Header | varchar |  |  | SI | Column Header for Range
If type is "TI" this is t... |
| LBCDFTRC_SubCol3Width | integer |  |  | SI | Width of Column for Range
If type is "TI" this is... |
| LBCDFTRC_Type | varchar |  |  | SI | Column Type
CD = Collection Date
CT = Collection... |
| LBCDFTRC_Width | integer |  |  | SI | Column Width
The column width in characters, excl... |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Applies to children under the age of eighteen and ... |
| Q04 | - |  |  | SI | Boarder authorised to sign consent forms |
| Q05 | - |  |  | SI | Special family considerations |
| Q06 | - |  |  | SI | Consideration notes |
| Q07 | - |  |  | SI | Supporting documentation scanned to record |
| Q08 | - |  |  | SI | Documentation notes |
| Q11 | - |  |  | SI | Person who will take patient home on discharge if ... |
| Q12 | - |  |  | SI | Name of parent / legal guardian providing informat... |
| Q13 | - |  |  | SI | Notes |
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
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*