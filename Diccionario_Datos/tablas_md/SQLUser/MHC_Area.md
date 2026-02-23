# SQLUser.MHC_Area

**Schema:** SQLUser
**Columnas:** 97
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Salud Mental**. Parámetros de psiquiatría.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| AREA_RowId | bigint | PK |  | NO | - |
| AREA_Code | varchar |  |  | NO | Code |
| AREA_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| AREA_CreatedDate | date |  |  | SI | Created Date |
| AREA_CreatedTime | time |  |  | SI | Created Time |
| AREA_CreatedUser_DR | bigint |  | FK | SI | Created User |
| AREA_DateFrom | date |  |  | SI | Date From |
| AREA_DateTo | date |  |  | SI | Date To |
| AREA_Desc | varchar |  |  | NO | Description |
| AREA_Owner | varchar |  |  | SI | Owner |
| AREA_UpdatedDate | date |  |  | SI | Updated Date |
| AREA_UpdatedTime | time |  |  | SI | Updated Time |
| AREA_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | MÉDICO - Hombres  - MENORES DE 15 AÑOS  -  TELECON... |
| Q02 | - |  |  | SI | MÉDICO - Hombres  - MENORES DE 15 AÑOS  -  TELECON... |
| Q03 | - |  |  | SI | MÉDICO - Hombres  - MENORES DE 15 AÑOS  -  TELECON... |
| Q04 | - |  |  | SI | MÉDICO - Hombres  - MENORES DE 15 AÑOS  -  TELECON... |
| Q05 | - |  |  | SI | MÉDICO - Hombres  - MENORES DE 15 AÑOS  -  TELECON... |
| Q06 | - |  |  | SI | MÉDICO - Hombres  - MENORES DE 15 AÑOS  -  TELECON... |
| Q07 | - |  |  | SI | MÉDICO - Hombres  - MENORES DE 15 AÑOS  -  TELECON... |
| Q08 | - |  |  | SI | MÉDICO - Hombres  - MENORES DE 15 AÑOS  -  TELECON... |
| Q12 | - |  |  | SI | CONSULTA URGENCIA OTROS |
| Q13 | - |  |  | SI | CONSULTA URGENCIA OTROS 1 |
| Q14 | - |  |  | SI | CONSULTA URGENCIA OTROS 2 |
| Q15 | - |  |  | SI | CONSULTA URGENCIA OTROS 3 |
| Q16 | - |  |  | SI | CONSULTA URGENCIA OTROS 4 |
| Q17 | - |  |  | SI | CONSULTA URGENCIA OTROS 5 |
| Q18 | - |  |  | SI | CONSULTA URGENCIA OTROS 6 |
| Q19 | - |  |  | SI | CONSULTA URGENCIA OTROS 7 |
| Q20 | - |  |  | SI | CONSULTA URGENCIA OTROS 8 |
| Q21 | - |  |  | SI | CONSULTA URGENCIA OTROS 9 |
| Q22 | - |  |  | SI | CONSULTA URGENCIA OTROS 10 |
| Q23 | - |  |  | SI | ACCIDENTE CEREBRO VASCULAR (ACV) |
| Q24 | - |  |  | SI | ACCIDENTE CEREBRO VASCULAR (ACV) 1 |
| Q25 | - |  |  | SI | ACCIDENTE CEREBRO VASCULAR (ACV) 2 |
| Q26 | - |  |  | SI | ACCIDENTE CEREBRO VASCULAR (ACV) 3 |
| Q27 | - |  |  | SI | ACCIDENTE CEREBRO VASCULAR (ACV) 4 |
| Q28 | - |  |  | SI | ACCIDENTE CEREBRO VASCULAR (ACV) 5 |
| Q29 | - |  |  | SI | ACCIDENTE CEREBRO VASCULAR (ACV) 6 |
| Q30 | - |  |  | SI | ACCIDENTE CEREBRO VASCULAR (ACV) 7 |
| Q31 | - |  |  | SI | ACCIDENTE CEREBRO VASCULAR (ACV) 8 |
| Q32 | - |  |  | SI | ACCIDENTE CEREBRO VASCULAR (ACV) 9 |
| Q33 | - |  |  | SI | ACCIDENTE CEREBRO VASCULAR (ACV) 10 |
| Q34 | - |  |  | SI | QUEMADOS |
| Q35 | - |  |  | SI | QUEMADOS 1 |
| Q36 | - |  |  | SI | QUEMADOS 2 |
| Q37 | - |  |  | SI | QUEMADOS 3 |
| Q38 | - |  |  | SI | QUEMADOS 4 |
| Q39 | - |  |  | SI | QUEMADOS 5 |
| Q40 | - |  |  | SI | QUEMADOS 6 |
| Q41 | - |  |  | SI | QUEMADOS 7 |
| Q42 | - |  |  | SI | QUEMADOS 8 |
| Q43 | - |  |  | SI | QUEMADOS 9 |
| Q44 | - |  |  | SI | QUEMADOS 10 |
| QA | - |  |  | SI | Año |
| QHR | - |  |  | SI | Establecimiento |
| QM | - |  |  | SI | Mes |
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